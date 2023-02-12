# mdsanima-cli

Command line tools for images processing, generating pixelart, adding logo to
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

The response is printing help.

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
