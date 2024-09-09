# CONTRIBUTING GUIDE

We are happy to receive any contributions to this library. Feel free to open an issue or a pull request.
We will review the pull requests and issues as time permits. 



## Project Goals

* Provide a simple wrapper around the ELO Indexserver API
* Assume default configurations (bitsets, paths, ...) as good as possible
* Allow the user to override the default configurations
* Be backwards compatible with the previous version of the client. Therefore, method signatures should if possible only
  add new parameters, not remove or change existing ones.
* stick to the OPENAPI specification as close as possible (exceptions when the spec does not always match the actual
  API)

## Development

Install poetry: https://python-poetry.org/docs/#installation

```bash
# Install dependencies
poetry install

# activate shell
poetry shell

# Run tests
python -m unittest discover test
```

## Available documentations to start with

There are two main sources of documentation:
* The [ELO Rest API PDF](eloRestAPI/dev-programming_elo-rest-snapshot-16_5_24.pdf) documentation
* The [OpenAPI](eloRestAPI/openapi_v23.json) specification. Also see the [Readme](eloRestAPI/Readme.md) for more information.

## Building / publishing this package

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging. Here are the basics:

1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI,
   just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:

1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
1. Build a wheel with `poetry build -f wheel`
1. Install that wheel from the other project `pip install <path-to-wheel>`

## Project Structure

### eloRestAPI

Contains openapi.json as well as a [Readme](eloRestAPI/Readme.md) on how to generate the client.

### eloclient

Contains the generated client. The client is generated with
the [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) tool.

### eloservice

Contains the wrapper around the generated client.
The wrapper is a simple class that initializes the client and exposes only a handful of features that cover the most
common use cases. Main file is [elo_service.py](eloservice/elo_service.py).

### test

automated tests that run on the CI/CD pipeline. Uses a pre-configured ELO server to run the tests against.

**If you know a way to setup an ELO instance via testcontainers or similar, please let us know.**

### Documentation

The documentation is automatically generated and published
to [GitHub Pages](https://treskon.github.io/elo-indexserver-client/).
We use SPHINXBUILD to generate the documentation.
Relevant files are:

* conf.py
* index.rst
* make.bat
* Makefile

## Release

The release is done by the following steps:

* increase the version in the pyproject.toml
* update the CHANGELOG.md
* git commit
* git tag 'releases/stable-<version>' use Semantic Versioning. Remember that a version can't be deleted or overwritten
  once it's
  published on pypi.org
* git push

The rest is done by the CI/CD pipeline. It will build and publish the package to the configured repository.
See the [GitHub Actions](.github/workflows/release.yml) for more details.