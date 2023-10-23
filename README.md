[![CI](https://github.com/nogibjj/djl_mini_project_7/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/djl_mini_project_7/actions/workflows/cicd.yml)

# My Data ET Tool

My Data ETL Tool is a Python package that simplifies the process of extracting, transforming, and loading (ETL) data from a remote source into a local SQLite3 database. It's designed to make data processing tasks more efficient and user-friendly.

## Features

- **Data Extraction:** The tool can download data from a given URL and save it to a local file.

- **Data Transformation and Loading:** It transforms and loads the downloaded data into a local SQLite3 database, allowing for easy querying and analysis.

- **Data Querying:** It provides functions for querying data within the SQLite3 database, such as counting occurrences of different values and aggregating data.

## Installation

To install the tool, follow these steps:

1. Open a Python environment (e.g., a virtual environment).

2. Run the following command to install the tool from PyPI:

*pip install et_tool*

3. The tool is now ready to use.

## Usage

To use the tool in your Python scripts, follow these steps:

```python
from et_tool import extract, load, queryCountIMECAS

# Extract data
extract()

# Transform and load data
load()

# Query data
queryCountIMECAS()
```
## Configuration

The tool is pre-configured to work with a specific URL and file paths. If you need to customize these settings, you can modify the source URL and file paths directly in the source code of the tool.

## Dependencies

- requests: For making HTTP requests.
- prettytable: For formatting tables.


## Issues and Support

If you encounter any issues or have questions about using the tool, please create an issue in the GitHub issue tracker.



For inquiries, you can contact us at email@example.com.
