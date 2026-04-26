import ast
import os
import re
import argparse
from pathlib import Path
from collections import defaultdict

# --- Config ---
SKIP_FILES  = {"strings.py"}  # Don't process the output file itself

def make_constant_name(s: str) -> str:
    """Turn a string value into a SCREAMING_SNAKE_CASE constant name."""
    s = s.strip()
    # Replace non-alphanumeric runs with underscores
    name = re.sub(r"[^a-zA-Z0-9]+", "_", s)
    name = name.strip("_").upper()
    # Truncate long names
    if len(name) > 60:
        name = name[:60].rstrip("_")
    return name or "STRING"

def load_existing_strings(output_path: str) -> dict[str, str]:
    """
    Parse an existing strings.py and return a value -> name mapping.
    Returns an empty dict if the file doesn't exist yet.
    """
    path = Path(output_path)
    if not path.exists():
        return {}

    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError:
        print(f"Warning: could not parse existing {output_path}, starting fresh.")
        return {}

    value_to_name = {}
    for node in ast.walk(tree):
        # Look for top-level assignments like MY_CONSTANT = 'some value'
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if not isinstance(node.value, ast.Constant):
            continue
        if not isinstance(node.value.value, str):
            continue
        value_to_name[node.value.value] = target.id

    return value_to_name

def extract_strings(project_dir: str, existing: dict[str, str] = {}) -> dict:
    """
    Returns a dict mapping constant_name -> {value, locations: [(file, line), ...]}.
    Handles name collisions by appending _2, _3, etc.
    Seeds from existing value->name mapping so prior names are preserved.
    """
    value_to_name: dict[str, str] = dict(existing)  # seed with existing
    constants: dict[str, dict] = {}
    used_names: dict[str, int] = defaultdict(int)

    # Seed used_names from existing so we don't generate colliding names
    for name in existing.values():
        base = re.sub(r"_\d+$", "", name)  # strip any trailing _2, _3 suffix
        used_names[base] += 1

    # Pre-populate constants dict for existing entries (no locations yet)
    for value, name in existing.items():
        constants[name] = {"value": value, "locations": []}

    py_files = sorted(Path(project_dir).rglob("*.py")) if Path(project_dir).is_dir() else [Path(project_dir)]

    for filepath in py_files:
        if filepath.name in SKIP_FILES:
            continue

        source = filepath.read_text(encoding="utf-8")
        try:
            tree = ast.parse(source, filename=str(filepath))
        except SyntaxError as e:
            print(f"Skipping {filepath} (syntax error: {e})")
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.Constant):
                continue
            if not isinstance(node.value, str):
                continue
            value = node.value
            if not value.strip():
                continue

            location = (str(filepath), node.lineno)

            if value in value_to_name:
                name = value_to_name[value]
                constants[name]["locations"].append(location)
            else:
                base_name = make_constant_name(value)
                used_names[base_name] += 1
                count = used_names[base_name]
                name = base_name if count == 1 else f"{base_name}_{count}"

                value_to_name[value] = name
                constants[name] = {"value": value, "locations": [location]}

    return constants

def write_strings_file(constants: dict, output_path: str):
    lines = [
        "# Auto-generated strings file",
        "# Do not edit manually — re-run extract_strings.py to regenerate",
        "",
    ]

    for name, info in sorted(constants.items()):
        # Emit source locations as comments
        for filepath, lineno in info["locations"]:
            lines.append(f"# {filepath}:{lineno}")
        # Emit the constant
        value = info["value"]
        # Use triple-quoted strings for multiline values
        if "\n" in value:
            escaped = value.replace('"""', r'\"\"\"')
            lines.append(f'{name} = """{escaped}"""')
        else:
            escaped = value.replace("'", r"\'")
            lines.append(f"{name} = '{escaped}'")
        lines.append("")  # blank line between constants

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(constants)} constants to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract string literals into a constants file.")
    parser.add_argument("input_path", help="Path to a .py file or project directory to scan")
    parser.add_argument("output_file", help="Path for the output strings file (e.g. strings.py)")
    args = parser.parse_args()

    input_path = Path(args.input_path)
    if not input_path.exists():
        print(f"Error: '{input_path}' does not exist.")
        exit(1)
    if input_path.is_file() and input_path.suffix != ".py":
        print(f"Error: '{input_path}' is not a .py file.")
        exit(1)

    # Keep the output file out of its own scan
    SKIP_FILES.add(Path(args.output_file).name)

    existing = load_existing_strings(args.output_file)
    if existing:
        print(f"Loaded {len(existing)} existing constants from {args.output_file}")

    constants = extract_strings(args.input_path, existing)
    write_strings_file(constants, args.output_file)
