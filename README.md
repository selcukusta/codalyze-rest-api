<p align="center">
  <img width="120" height="120" src="https://selcukusta.com/images/extension-logo.png">
</p>

# Codalyze: Code Complexity REST API

[![The MIT License](https://flat.badgen.net/badge/license/MIT/orange)](http://opensource.org/licenses/MIT)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/selcukusta/code-analyzer)

[![Visual Studio Marketplace](https://vsmarketplacebadge.apphb.com/version/selcuk-usta.code-complexity-report-generator.svg)](https://marketplace.visualstudio.com/items?itemName=selcuk-usta.code-complexity-report-generator)
[![Visual Studio Marketplace](https://vsmarketplacebadge.apphb.com/downloads-short/selcuk-usta.code-complexity-report-generator.svg)](https://marketplace.visualstudio.com/items?itemName=selcuk-usta.code-complexity-report-generator)
[![Visual Studio Marketplace](https://vsmarketplacebadge.apphb.com/installs-short/selcuk-usta.code-complexity-report-generator.svg)](https://marketplace.visualstudio.com/items?itemName=selcuk-usta.code-complexity-report-generator)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=selcukusta_codalyze-rest-api&metric=alert_status)](https://sonarcloud.io/dashboard?id=selcukusta_codalyze-rest-api)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=selcukusta_codalyze-rest-api&metric=sqale_index)](https://sonarcloud.io/dashboard?id=selcukusta_codalyze-rest-api)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=selcukusta_codalyze-rest-api&metric=bugs)](https://sonarcloud.io/dashboard?id=selcukusta_codalyze-rest-api)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=selcukusta_codalyze-rest-api&metric=code_smells)](https://sonarcloud.io/dashboard?id=selcukusta_codalyze-rest-api)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=selcukusta_codalyze-rest-api&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=selcukusta_codalyze-rest-api)

Create code complexity (Cyclomatic complexity, Lines Of Code, Parameter Count, etc.) report for the activated code file.

Supported languages;

- C++
- C#
- Java
- Javascript
- Objective C
- PHP
- Python
- Ruby
- Swift
- Golang

## Preview of VSCode Extension

![VSCode Extension Preview](.github/images/preview.png)

## Run locally

```bash
pip install -r requirements.txt
pip install uvicorn
uvicorn main:app --reload
```

## Run via Docker

```bash
docker image build -t [YOUR_REPOSITORY_NAME]/[YOUR_IMAGE_NAME]:latest .
docker container run -d --name analyzer -p 8000:80 [YOUR_REPOSITORY_NAME]/[YOUR_IMAGE_NAME]:latest
```

## Usage

Application has 3 specific endpoints:

### Summary Endpoint

#### Request

`curl --location --request GET 'http://127.0.0.1:8000/'`

#### Response

```json
{
  "Title": "Codalyze: Code Complexity Report",
  "Description": "Create code complexity (Cyclomatic complexity, Lines Of Code, Parameter Count, etc.) report for the activated code file.",
  "Support": "selcukusta(at)gmail(dot)com",
  "API Documentation": "https://codalyze-api.selcukusta.com/docs",
  "Credits": {
    "lizard": "https://github.com/terryyin/lizard",
    "fastapi": "https://github.com/tiangolo/fastapi"
  }
}
```

### Analyze Endpoint

#### Request

```bash
curl --location --request POST 'http://127.0.0.1:8000/analyze/go' \
--header 'Content-Type: application/json' \
--data-raw '{
    "html": "[PASTE_YOUR_CODE]",
    "threshold": {
        "cyclomatic_complexity": 200,
        "lines_of_code": 50,
        "parameter_count": 4
    }
}'
```

#### Response

```json
{
  "total_lines_of_code": 73,
  "functions": [
    {
      "name": "AzureBlobHandler",
      "cyclomatic_complexity": 6,
      "lines_of_code": 52,
      "start_line": 27,
      "end_line": 86,
      "parameter_count": 2
    }
  ]
}
```

### HTML Output Endpoint

#### Request

```bash
curl --location --request POST 'http://127.0.0.1:8000/output/go' \
--header 'Content-Type: application/json' \
--data-raw '{
    "html": "[PASTE_YOUR_CODE]",
    "threshold": {
        "cyclomatic_complexity": 200,
        "lines_of_code": 50,
        "parameter_count": 4
    }
}'
```

#### Response

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Codalyze: Code Complexity Report</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
  </head>
  <body>
    ...
  </body>
</html>
```

## Credits

- [terryyin/lizard](https://github.com/terryyin/lizard) for complexity calculation
- [tiangolo/fastapi](https://github.com/tiangolo/fastapi) for web framework
