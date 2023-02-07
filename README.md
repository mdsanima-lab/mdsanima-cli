# mdsanima-cli

Command Line Tools for Processing Images.

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
