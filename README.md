BCP Reader
==========

![Test status](https://github.com/drkane/bcp-reader/workflows/tests/badge.svg)
[![PyPI version](https://badge.fury.io/py/bcp-reader.svg)](https://pypi.org/project/bcp-reader/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bcp-reader)
![PyPI - License](https://img.shields.io/pypi/l/bcp-reader)

A reader for BCP-format data files. BCP files are similar to CSV files but 
contain a multi-character line and field delimiters. The default delimiters
used are:

 - field delimiter: `@**@`
 - line delimiter: `*@@*`

Python's csv module can only deal with single character delimiters, so this 
module has a `reader` function and `DictReader` class which should be drop-in
replacements for python's `csv` module equivalents.

## Credits

The author of the main method is [Gertjan van den Burg](https://github.com/GjjvdBurg)
of the Alan Turing Institute. It was based on a method originally developed
by [David Kane](https://dkane.net) at NCVO.

## Installation

Install with `pip install bcp-reader`

## Usage

The module can be used by importing from the `bcp` module in a python script:

```python
import bcp

with open('path_to_bcp_file.bcp') as f:
    bcpreader = bcp.reader(f)
    for row in bcpreader:
        print(row)
        # ["Value 1", "Value 2"]

with open('path_to_bcp_file.bcp') as f:
    bcpreader = bcp.DictReader(f, fieldnames=["field 1", "field 2"])
    for row in bcpreader:
        print(row)
        # {"field 1": "Value 1", "field 2": "Value 2"}
```

You can also use it via the command line to convert a BCP file to CSV:

```sh
bcp path_to_bcp_file.bcp > csv_output.csv
```
