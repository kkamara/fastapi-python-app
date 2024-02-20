# FastAPI Python App



* [Using Thunder Client?](#thunder-client)

* [Installation](#installation)

* [Usage](#usage)

* [Documentation](#docs)

* [Contributing](#contributing)

* [License](#license)

<a name="thunder-client"></a>
## Using Thunder Client?

[Thunder client](https://www.thunderclient.com/) Visual Studio Code extension.

[thunder-collection_FastAPI Python App.json](https://github.com/kkamara/fastapi-python-app/blob/main/thunder-collection_FastAPI%20Python%20App.json)

## Installation

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload --port=3000
# http://localhost:3000
```

<a name="docs"></a>
## Documentation

```bash
uvicorn main:app --reload --port=3000
# http://localhost:3000/docs
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD](https://opensource.org/licenses/BSD-3-Clause)
