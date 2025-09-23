# Release checklist

## Prior to creating a new release branch make sure that you have done these things

- In the metadata.tres file in the archipelago\_companion folder increment the version code by 1, and update the version string to the release version
- Update the changelog to create a release header and include any items that were not already added

## Prior to creating a new release version in github make sure that you have done these things

- You have pulled down the release branch and copied the entire archipelago\_client folder over to your testing cassette beasts instance
- You have then exported the mod through Project > Tools > Export Mod...
- You have zipped up the cassette\_beasts folder and renamed it from .zip to .apworld
- You have zipped up the cassette\_beasts\_tracker folder

## When creating the release in github

- The tag and name of the version should be v#.#.# following the semantic version of that release
- The description should at minimum include the auto generated release notes
- The 3 files above should be added to the release assets (at least until we have CD doing it for us)
