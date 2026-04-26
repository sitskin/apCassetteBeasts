import ast
import argparse
from pathlib import Path

# --- Config ---
SKIP_FILES = {"extract_strings.py", "replace_strings.py"}


def load_strings_file(strings_path: str) -> dict[str, str]:
    """
    Parse the strings file and return a value -> constant_name mapping.
    """
    path = Path(strings_path)
    if not path.exists():
        print(f"Error: strings file '{strings_path}' does not exist.")
        exit(1)

    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"Error: could not parse '{strings_path}': {e}")
        exit(1)

    value_to_name = {}
    for node in ast.walk(tree):
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

    print(f"Loaded {len(value_to_name)} constants from {strings_path}")
    return value_to_name


def get_docstring_ranges(tree: ast.AST) -> set[int]:
    """
    Return a set of line numbers that are part of docstrings,
    so we can skip replacing literals inside them.
    """
    docstring_lines = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not node.body:
            continue
        first = node.body[0]
        if not isinstance(first, ast.Expr):
            continue
        if not isinstance(first.value, ast.Constant):
            continue
        if not isinstance(first.value.value, str):
            continue
        for lineno in range(first.lineno, first.end_lineno + 1):
            docstring_lines.add(lineno)
    return docstring_lines


def get_existing_import_constants(tree: ast.AST, module_name: str) -> set[str]:
    """
    Find any existing 'from .<module_name> import ...' line and return
    the set of constants already imported.
    """
    for node in ast.walk(tree):
        if not isinstance(node, ast.ImportFrom):
            continue
        if node.module != module_name:
            continue
        if node.level != 1:
            continue
        return {alias.name for alias in node.names}
    return set()


def get_existing_import_lineno(tree: ast.AST, module_name: str) -> int | None:
    """
    Return the line number of an existing 'from .<module_name> import ...' statement,
    or None if it doesn't exist yet.
    """
    for node in ast.walk(tree):
        if not isinstance(node, ast.ImportFrom):
            continue
        if node.module != module_name:
            continue
        if node.level != 1:
            continue
        return node.lineno
    return None


def build_import_line(constants: set[str], module_name: str) -> str:
    names = ", ".join(sorted(constants))
    return f"from .{module_name} import {names}"


def get_source_offset(source: str, lineno: int, col_offset: int) -> int:
    """Convert a 1-based line number and 0-based col offset to a flat source offset."""
    lines = source.splitlines(keepends=True)
    offset = sum(len(lines[i]) for i in range(lineno - 1))
    return offset + col_offset


def find_import_insert_position(tree: ast.AST) -> int:
    """
    Return the line index (0-based) after which to insert the new import.
    Places it after the last existing import, or after the module docstring,
    or at line 0 if neither exists.
    """
    last_import_line = 0

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            last_import_line = node.lineno
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
            last_import_line = node.end_lineno
        else:
            break

    return last_import_line


def replace_strings_in_file(filepath: Path, value_to_name: dict[str, str], module_name: str) -> int:
    """
    Replace string literals in a single file with their constant references.
    Updates or adds the import line as needed.
    Returns the number of replacements made.
    """
    source = filepath.read_text(encoding="utf-8")

    try:
        tree = ast.parse(source, filename=str(filepath))
    except SyntaxError as e:
        print(f"  Skipping {filepath} (syntax error: {e})")
        return 0

    docstring_lines = get_docstring_ranges(tree)
    existing_import_constants = get_existing_import_constants(tree, module_name)
    existing_import_lineno = get_existing_import_lineno(tree, module_name)

    replacements = []
    constants_used = set(existing_import_constants)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant):
            continue
        if not isinstance(node.value, str):
            continue
        if not node.value.strip():
            continue
        if node.lineno in docstring_lines:
            continue
        if node.value not in value_to_name:
            continue

        constant_name = value_to_name[node.value]
        constants_used.add(constant_name)

        start = get_source_offset(source, node.lineno, node.col_offset)
        end = get_source_offset(source, node.end_lineno, node.end_col_offset)

        replacements.append((start, end, constant_name))

    if not replacements and constants_used == existing_import_constants:
        print(f"  No changes needed: {filepath}")
        return 0

    # Apply replacements in reverse order so offsets stay valid
    replacements.sort(key=lambda r: r[0], reverse=True)
    source_chars = list(source)
    for start, end, replacement in replacements:
        source_chars[start:end] = list(replacement)
    new_source = "".join(source_chars)

    # Update or insert the import line
    new_import_line = build_import_line(constants_used, module_name)
    lines = new_source.splitlines(keepends=True)

    if existing_import_lineno is not None:
        lines[existing_import_lineno - 1] = new_import_line + "\n"
    else:
        insert_at = find_import_insert_position(tree)
        lines.insert(insert_at, new_import_line + "\n")

    filepath.write_text("".join(lines), encoding="utf-8")

    replacement_count = len(replacements)
    print(f"  {filepath}: {replacement_count} replacement(s), import -> {new_import_line}")
    return replacement_count


def process(input_path: str, strings_path: str):
    module_name = Path(strings_path).stem
    value_to_name = load_strings_file(strings_path)

    path = Path(input_path)
    py_files = sorted(path.rglob("*.py")) if path.is_dir() else [path]

    total_replacements = 0
    total_files = 0

    for filepath in py_files:
        if filepath.name in SKIP_FILES:
            continue
        count = replace_strings_in_file(filepath, value_to_name, module_name)
        if count > 0:
            total_files += 1
            total_replacements += count

    print(f"\nDone. {total_replacements} replacement(s) across {total_files} file(s).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace string literals with constants from a strings file.")
    parser.add_argument("input_path", help="Path to a .py file or project directory to process")
    parser.add_argument("strings_file", help="Path to the strings file to import constants from")
    args = parser.parse_args()

    input_path = Path(args.input_path)
    if not input_path.exists():
        print(f"Error: '{input_path}' does not exist.")
        exit(1)
    if input_path.is_file() and input_path.suffix != ".py":
        print(f"Error: '{input_path}' is not a .py file.")
        exit(1)

    SKIP_FILES.add(Path(args.strings_file).name)

    process(args.input_path, args.strings_file)

