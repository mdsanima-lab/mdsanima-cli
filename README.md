# mdsanima-cli

The package will provide command-line tools for images processing, generating pixel art, adding logo to images, and much more.

## Package Installation

Install or update the latest version using pip:

```shell
python3 -m pip install --upgrade mdsanima-cli
```

The package is now installed, and you can start using it.

## CLI Terminal Commands

After installing the package, you can now use the `mdsanima` command in the terminal, and the response will provide instructions on how to use these command-line tools. You can also use the `mds` alias, which has the same functionality.

Below are the available commands that have been marked as completed, along with some ideas for commands that we would like to implement in this package:

- [x] `mdsanima` main command showing help
- [x] `mdsanima check` print directory info
- [x] `mdsanima uuid` rename to uuid
- [x] `mdsanima number` rename to seq numbers
- [x] `mdsanima logo` append a logo
- [x] `mdsanima watermark` append a watermark
- [x] `mdsanima jpg` convert to jpg
- [x] `mdsanima png` convert to png
- [x] `mdsanima webp` convert to webp
- [x] `mdsanima pixelart` generate pixel art 32px
- [x] `mdsanima grid` generate grid 2x2
- [x] `mdsanima thumbnail` generate jpeg thumbnail 128px
- [x] `mdsanima gifmaker` generate gif animation pixel art
- [x] `mdsanima resize` resizing to 512px width
- [ ] `mdsanima multi` generate multi resolution
- [ ] `mdsanima caption` adding caption
- [ ] `mdsanima bg` adding background
- [ ] `mdsanima filter` adding filter
- [ ] `mdsanima crop` cropping image

The `pixelart` command works in a folder that contains only `.png` images and converts these images into pixel art by creating a new file and appending the suffix `pixelart` to the original file name. After executing this command, all image files in the folder you are in will be processed. The command does not delete any files in the folder, it only adds new ones and displays directory information.

## Development

Here are some helpful instructions in the development process of this Python package.

### Python Setup

This package is built using specific tools and will be published on PyPI using Twine. Instructions on how to activate the **virtual environment** for this project and how to configure and build the package. We will use specific package versions and **Python 3.11** for now.

#### Virtual Environment

Creating and activating the development environment, and then installing the necessary packages, enter the following commands in the terminal:

```shell
virtualenv --setuptools=68.2.2 --wheel=0.41.2 --pip=23.2.1 --python=python3.11 .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

All dependencies for this project are specified in the `requirements.*` files and in the project's TOML configuration.

You can install these dependencies using the `pip install .` command, which will build our package and install the basic dependencies along with the new version of our package. To install dev dependencies, you can use the `pip install ".[dev]"` command instead of specifying a `-r` flag and file as mentioned earlier.

After following the above instructions, we can start writing the program. You can also refer to the instructions regarding the configuration of the development environment, which are included in this [workflow](https://mdsanima-dev.github.io/mdsanima-dev/development/workflow/) guide.

#### Build Package

Building our **Python** package is done using the `build` module, which was previously installed as a requirement in the `requirements-dev.txt` file when activating the development environment.

To build the package, enter the following command in the terminal:

```shell
python -m build
```

After building, the package will be placed in a folder named `dist`, and the filename will have the `.whl` extension, including the package name and version.

#### Install Package

After building the package, you can install it by entering the following command in the terminal:

```shell
pip install --force-reinstall dist/mdsanima_cli-0.2.0-py3-none-any.whl
```

The `--force-reinstall` flag is necessary when installing the package because if you have a previous version installed, the installation will fail. Please note that the above command may change depending on the version you are currently building.

#### Testing Package

After building and installing our package, we can test it. You can use the appropriate **CLI** command mentioned above or test individual modules by entering the following command in the terminal:

```shell
python -m mdsanima_cli.commands.pixelart
```

You can also run and test before building and installing the package, type in the terminal:

```shell
python3 src/mdsanima_cli/commands/pixelart.py
```

After running the above command, you will test only the selected module.

#### Extracts Version

The _setuptools-scm_ tool allows you to extract the **Python** package version from _git_ instead of declaring it as a version argument.

If you need to confirm which version string is being generated, you can use the _setuptools-scm_ tool, which will display the current version you are working with. Enter the following command in the terminal:

```shell
python -m setuptools_scm
```

Check the [pyproject.toml](pyproject.toml) file and this [instruction](https://pypi.org/project/setuptools-scm/) for more info.

### Creating Release

Below is the instruction on how to create a release version of our Python package.

Here are the steps to create a release version:

1. Add new code to the package
2. Test new functionality
3. Commit the changes
4. Bump the package version
5. Generate the CHANGELOG.md file
6. Commit the release
7. Add and push the new tag
8. Update on PyPI

This is done manually for now, but we plan to set up a _GitHub Action_ workflow for testing and automatic release version creation in the future.

#### Conventional Commits

In this project, we use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) - a specification for adding human and machine readable meaning to commit messages.

Therefore, a crucial step is to commit your code changes using this specification. A commit message should look like this:

```shell
git commit -m "feat: generating pixel art command"
```

Always use this format for committing to Git, as it enables generating a changelog from the commit message.

#### Standard Version

Check the [package.json](package.json) file in the **standard-version** section and in the types lists for the first string that you can use in the commit message or check the [examples](https://www.conventionalcommits.org/en/v1.0.0/#examples) from _Conventional Commits_ documentation.

Bump the package version in the [package.json](package.json) file and generate the [CHANGELOG.md](CHANGELOG.md) file with new release information, type the `standard-version` command in the terminal, and then add these changes to Git, committing the release like this:

```shell
git commit -am "chore(release): v0.2.0"
```

The version above is the result of the `standard-version` command, and this is just an example version. The version must always be changed when a new release is made.

The next step is to create a tag and push the changes to the remote repository with the tag. The command should look like this:

```shell
git tag v0.1.2
git push origin --tag
```

After completing the above steps, you can verify the package version by entering this command in the terminal:

```shell
python -m setuptools_scm
```

Finally, create the build and update this build on [test.pypi.org](https://test.pypi.org/project/mdsanima-cli/) and [pypi.org](https://pypi.org/project/mdsanima-cli/), but first, make sure to check everything, and then proceed with the update.

Enter the following commands in the terminal:

```shell
rm -rf dist
python -m build
twine check dist/*
twine upload -r testpypi dist/*
twine upload dist/*
```

Remember, only the package owner can perform this operation and must have the secrets configured in the `.pypirc` file in the system.
