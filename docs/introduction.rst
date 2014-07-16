General Overview
================

Exchange formats for the CCHDO CTD and bottle data are described.
The WHP-exchange formats provide simplified exchange and improved readability of hydrographic data.
WHP-exchange data files carry the essential information from CTD and water sample profiles in rigorously-described comma-delimited (csv) UTF-8 formats designed to ease data exchange and simplify data import.


Overview of WHP-exchange file formats
`````````````````````````````````````
The WHP-exchange bottle and CTD data formats include these features:

* UTF-8 Encoded
* Spreadsheet-like
* comma-delimited values (csv)
* no special meaning to blank/empty spaces
* station information in every line in the file (bottle) or in the top lines in each file (CTD)
* only one missing data value defined for all parameters
* missing data value format defined in the precision format for each parameter
* WHP quality flag, when provided, associated directly with its parameter
* positions in decimal degrees
* dates in ISO 8601 YYYYMMDD format

There are three types of WHP-exchange format files, each with a unique 8-character suffix:


============ ================== ===========
Data Type    8-character Suffix Description
============ ================== ===========
CTD data     _ct1.csv           one CTD profile in WHP-exchange format
CTD data     _ct1.zip           zip containing one or more _ct1.csv WHP-exchange CTD profiles
bottle data  _hy1.csv           data from one or more bottle profiles in WHP-exchange format
============ ================== ===========
