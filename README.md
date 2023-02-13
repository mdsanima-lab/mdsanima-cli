# mdsanima-cli

Command line tools for images processing, generating pixel art, adding logo to
images and many more.

## Installation

Install latest version:

```bash
python3 -m pip install mdsanima-cli
```

## Terminal Commands

Now you can use this command in terminal:

```bash
mdsanima
```

The response is printing help how to use this command line tools.

### CLI

Avaiable command for this package.

```bash
mdsanima pixelart
```

This command works in folder that have only `.png` images and convert this
image to pixel art with creating new file with append suffix `pixelart` to
original file name.

## Development Setup

Instruction step how to setup development environent is here on this
[workflow](https://mdsanima-dev.github.io/mdsanima-dev/development/workflow/)
instruction.

Creating isolated environment with specific pip version then activate and
install requirements, type in terminal:

```bash
virtualenv --pip 23.0 .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Build Package

Install buil tools for creating distribution, type in terminal:

```bash
pip install --upgrade build
```

Now you can run:

```bash
python -m build
```

### Install Package

Now you can run:

```bash
pip install --force-reinstall dist/mdsanima_cli-0.1.0-py3-none-any.whl
```

### Testing Package

Finally you can run this command:

```bash
python -m mdsanima_cli.pixelart
```

Also you can run this command before you build and install:

```bash
python3 src/mdsanima_cli/pixelart.py
```

### Extracts Version Package

This `setuptools-scm` tools allow to extract **Python** package version from
`git` instead declaring them as the version argument.

Check the `pyproject.toml` file and this
[instruction](https://pypi.org/project/setuptools-scm/) for more info.

If you need to confirm which version string is being generated or debug the
configuration, you can install `setuptools-scm` directly in your working
environment `pip install setuptools-scm` and run:

```bash
python -m setuptools_scm
```

### Creating Release

This is a steps for creating release version.

First add new code to the package and test this. Second steps is commit change
like this command `git commit -m "feat: new feature generating pixelart"` and
next is type this in terminal:

```bash
standard-version
```

This command create the new version and generate `CHANGELOG.md` file.

Next is a add this changes to git, type in terminal:

```bash
git commit -am "chore(release): 0.1.2"
```

The version abowe is a from `standard-version` command and this is a only
example version. The version must always be changed when a new version is
released.

The next steps is a creating a tag and pushing the change to origin with tag,
type in terminal:

```bash
git tag 0.1.2
git push origin --tag
```

Checking the extracts version, type in terminal:

```bash
python -m setuptools_scm
```

Finally create the build and update to
[test.pypi.org](https://test.pypi.org/project/mdsanima-cli/) and
[pypi.org](https://pypi.org/project/mdsanima-cli/) first you can check and then
update.

```bash
python -m build
twine check dist/*
twine upload -r testpypi dist/*
twine upload dist/*
```
