# Development Infos

** The content of that repos is published. Therefore, do not store any passwords or other sensitive data in this
repository.**

## Release

The release is done by the following steps:

* increase the version in the pyproject.toml
* git commit
* git tag 'stable-<version>' use Semantic Versioning. Remember that a version can't be deleted or overwritten once it's
  published on pypi.org
* git push



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

