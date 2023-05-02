# mdsanima-cli

The package will provide command-line tools for image processing, generating pixel art, adding logos
to images, and much more.

## Installation

Install latest version:

```shell
python3 -m pip install mdsanima-cli
```

Updating to latest version:

```shell
python3 -m pip install --upgrade mdsanima-cli
```

## Terminal Commands

Now you can use this command in terminal:

```shell
mdsanima
```

The response is printing help how to use this command-line tools.

You can use the `mdsanima` command or the `mds` alias, which have the same functionality.

### CLI

Avaiable command for this package:

- `mdsanima` main command showing help
- `mdsanima check` print directory info
- `mdsanima uuid` rename to uuid
- `mdsanima number` rename to seq numbers
- `mdsanima logo` append a logo
- `mdsanima watermark` append a watermark
- `mdsanima jpg` convert to jpg
- `mdsanima png` convert to png
- `mdsanima webp` convert to webp
- `mdsanima pixelart` generate pixel art 32px
- `mdsanima grid` generate grid 2x2
- `mdsanima thumbnail` generate jpeg thumbnail 128px

The `pixelart` command works in folder that have only `.png` images and convert this images to pixel
art with creating the new file and appending the suffix `pixelart` to original file name.

After executing this command, all image files in the folder you are in will be processed.
The command does not delete any files in the folder, it only adds new ones and showing the directory
info.

## Development Setup

Instruction step how to setup development environent is here on this
[workflow](https://mdsanima-dev.github.io/mdsanima-dev/development/workflow/) instruction.

Creating isolated environment with specific pip version then activate and install requirements, type
in terminal:

```shell
virtualenv --setuptools 67.7.2 --wheel 0.40.0 --pip 23.1.2 .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Build Package

Install build tools for creating distribution, type in terminal:

```shell
pip install --upgrade build
```

Now you can run:

```shell
python -m build
```

### Install Package

Now you can run:

```shell
pip install --force-reinstall dist/mdsanima_cli-0.2.0-py3-none-any.whl
```

### Testing Package

Finally you can run this command:

```shell
python -m mdsanima_cli.command.pixelart
```

Also you can run this command before you build and install:

```shell
python3 src/mdsanima_cli/command/pixelart.py
```

### Extracts Version Package

This `setuptools-scm` tools allow to extract **Python** package version from `git` instead declaring
them as the version argument.

Check the `pyproject.toml` file and this
[instruction](https://pypi.org/project/setuptools-scm/) for more info.

If you need to confirm which version string is being generated or debug the configuration, you can
install `setuptools-scm` directly in your working environment `pip install setuptools-scm` and run:

```shell
python -m setuptools_scm
```

### Creating Release

Here are the steps to create a release version:

- Add new code to the package.
- Test new functionality.
- Commit the change.
- Bump the package version.
- Generate CHANGELOG.md file.
- Commit the release.
- Add and push new tag.
- Update pypi.

Important steps is commit the change like this, type in terminal:

```shell
git commit -m "feat: generating pixel art command"
```

Always use this format for commiting to git, becouse this allows to generate changelog from the
commit message. Check the `package.json` file on `standard-version` section and types lists for
fist string thats you can type in commit message.

The next step is bumping version on `package.json` file and generate `CHANGELOG.md` file with new
release information, type in terminal:

```shell
standard-version
```

Next is a add this changes to git, type in terminal:

```shell
git commit -am "chore(release): 0.1.2"
```

The version abowe is a from `standard-version` command and this is a only example version.
The version must always be changed when a new version is released.

The next steps is a creating a tag and pushing the change to origin with tag, type in terminal:

```shell
git tag 0.1.2
git push origin && git push origin --tag
```

Checking the extracts version, type in terminal:

```shell
python -m setuptools_scm
```

Finally create the build and update this build to
[test.pypi.org](https://test.pypi.org/project/mdsanima-cli/) and
[pypi.org](https://pypi.org/project/mdsanima-cli/) but first you must check and then update.

```shell
python -m build
twine check dist/*
twine upload -r testpypi dist/*
twine upload dist/*
```
