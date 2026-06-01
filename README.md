# generate-names

A simple library to quickly generate names based on US census data, based on the dataset provided by this [1990 US Census.](https://www.census.gov/topics/population/genealogy/data/1990_census/1990_census_namefiles.html).

## Quick Start

### Installation

```bash
pip install generate-names
```

### Usage

```bash
>>> from generate_names import generate
>>> print(generate('male', True))
John Smith
>>> print(generate('female', True))
Jane Smith
>>> print(generate('', True))
Smith
```
