Introduction
================

This document will describe the WHP-Exchange formats used by the CCHDO for CTD and bottle.
The WHP-exchange formats provide simplified exchange and improved readability of hydrographic data.
WHP-exchange data files carry the essential information from CTD and water sample profiles.
WHP-exchange is a rigorously-described comma-delimited (csv) format designed to ease data exchange and simplify data import.


Overview
--------
The WHP-exchange bottle and CTD data formats include these features:

* UTF-8 Encoded
* Spreadsheet-like
* Comma-delimited values (csv)
* No special meaning to blank/empty spaces
* Station information in every line in the file (bottle) or in the top lines in each file (CTD)
* Only one missing data value defined for all parameters
* Missing data value format defined in the precision format of each parameter
* WHP quality flag, when provided, associated directly with its parameter
* Positions in decimal degrees
* Dates in ISO 8601 YYYYMMDD format


File Types and Names
--------------------
There are three types of WHP-exchange format files, each with a unique 8-character suffix:

============ ================== ===========
Data Type    Filename Suffix    Description
============ ================== ===========
CTD data     _ct1.csv           One CTD profile in WHP-exchange format
CTD data     _ct1.zip           Zip archive containing one or more _ct1.csv WHP-exchange CTD files
Bottle data  _hy1.csv           Data from one or more bottle profiles in WHP-exchange format
============ ================== ===========
