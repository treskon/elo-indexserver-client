# ELO Indexserver Client

Developed by [Treskon GmbH](https://treskon.at/) 
* published on PyPI: https://pypi.org/project/elo-indexserver-client/ 
* [Documentation](https://treskon.github.io/elo-indexserver-client/)
* Sourcecode [GitHub repository](https://github.com/treskon/elo-indexserver-client)

A client library for accessing Indexserver component of [ELO Digital Office GmbH](https://www.elo.com/de-at.html) via
REST API.

## Motivation

The motivation for this project was to provide a simple and easy to use client library for accessing the Indexserver
REST API.
While ELO provides an OpenAPI specification for the Indexserver REST API, it appears to be a port of the Java SDK.
Which allows to use all the features of the Java SDK, similar to what we could do in the ELO Java Client itself.
This comes in favor for people who already have experience in working with the ELO Java SDK.
However, for people who are not familiar with the ELO ecosystem the naming conventions, structure, method names, BSET
Flags, etc. are far from intuitive and easy to understand.

**Therefore, we decided to create a client library that wraps the original OpenAPI specification and exposes only a
handful of features that cover the most common use cases.**

## Installation

```bash
pip install elo-indexserver-client
```

## Usage

First, init the Service with the baseurl, user and password of the Indexserver REST API.

```python
from eloservice.elo_service import EloService

rest_baseurl = "http://localhost:9090/ix-Archive/rest/"
rest_user = "elo"
rest_password = "elo"
elo_service = EloService(url=rest_baseurl, user=rest_user, password=rest_password)
```

**Known issue: Due to encoding issues the user and password should not contain special characters.**

Then you can use the service to access the Index server REST API.
Here are often examples:

```python
# Create Folder 
folder_id = elo_service.create_folder(path="¶Foodplaces", separator="¶")
# upload_file
file_id = elo_service.upload_file(sord_id=folder_id, file_path="test.jpg", file_name="ichiran_ramen.jpg")
# overwrite_mask_fields
elo_service.overwrite_mask_fields(sord_id=file_id, mask_name="Images", metadata={
    "LATITUDE": "35.73258119685775",
    "LONGITUDE": "139.71412884357233",
    "ITEMDOCDATE": "2023-12-26"
})
# search
search_result = elo_service.search(search_mask_fields={"LATITUDE": "35.73258119685775"}, max_results=1)
print(f"sordID of the found file: {search_result[0]}")
```

For more information visit the [Documentation](https://treskon.github.io/elo-indexserver-client/) or see the
docstrings in the code.

There are also some demos via juptyer notebook in the examples folder.
See [Readme](examples/Readme.md) for more information.

## Technical Details

The client library is based on the OpenAPI specification provided by ELO Indexserver. Downloaded from the ELO Server
under the url http://eloIndexServer:9090/ix/resources/openapi.json.
The used ELO version was 20.0.0.111.

Based on the OpenAPI specification, the client library was generated using
the [openapi-python-client tool](https://github.com/openapi-generators/openapi-python-client).

## Contributing and Support

We are happy to receive any contributions to this library. Feel free to open an issue or a pull request in our
[GitHub repository](https://github.com/treskon/elo-indexserver-client). To get started read the [Contributing Guide](CONTRIBUTING.md).

We're not able to offer any commercial assistance for this library, but we're always happy to hear your thoughts and
assist you with any issues, as time permits.

Feel free to open an issue in our [GitHub repository](https://github.com/treskon/elo-indexserver-client) or contact us
via mail at: internal-dev@treskon.at.

## License

Copyright 2024 Treskon GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
