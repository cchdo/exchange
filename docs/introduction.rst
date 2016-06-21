Introduction
================

This document will describe the WHP-Exchange formats used by the CCHDO for CTD and bottle data where CTD files store conductivity, temperature, and depth profiles and bottle files store water sample profiles.
WHP-Exchange is a rigorously-described comma-delimited (csv) format designed to ease data exchange and simplify data import.
WHP-Exchange data files carry the essential information from CTD and bottle profiles.
The WHP-Exchange formats provide improved readability and a simplified exchange of hydrographic data.


Overview
--------
The WHP-Exchange CTD and bottle data formats include these features:

* UTF-8 Encoded
* Spreadsheet-like
* Comma-delimited values (csv)
* No special meaning to blank/empty spaces
* Station information added in the top lines for a CTD file
* Station information added in every line for a bottle file
* Only one missing data value defined for all parameters **(What does this mean?)**
* Positions in decimal degrees
* Dates in ISO 8601 YYYYMMDD format


File Types and Names
--------------------
There are three types of WHP-Exchange format files, each with a unique 8-character suffix:

============ ================== ===========
Data Type    Filename Suffix    Description
============ ================== ===========
CTD data     _ct1.csv           One CTD profile in WHP-Exchange format
CTD data     _ct1.zip           Zip archive containing one or more _ct1.csv WHP-Exchange CTD files
Bottle data  _hy1.csv           Data from one or more bottle profiles in WHP-Exchange format
============ ================== ===========

Requirement Levels
------------------
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in 
this document are to be interpreted as described in :rfc:`2119`.

About Text Encodings and UTF-8
------------------------------

Text on Computers
^^^^^^^^^^^^^^^^^
As strange as it may seem, there is no such thing in computing as 'plain text'.
Computers only understand binary, on or off, commonly represented by zeros and ones.
For a series of zeros and ones to have meaning to humans, there needs to be an agreed upon standard for what any specific set of binary data represents.
As an example, in 8-bit ASCII (ANSI X3.4-1986), the capital letter A is represented by the binary 01000001 (hex 41).
7-bit ASCII is limited to representing 127 characters, which is fine for most English speaking countries.

As the use of computers spread to non english speaking countries, it became nessessary to extend the encodings to support other characters needed.
However, most systems still only supported 8-bit bytes, with a maximum of 255 different characters it could represent.
With more characters needing to be represented than space avaiable, a proliferation of incompatible encoding standards occured.
There are at least 15 parts of ISO 8859, 6 JIS standards for Japanese, 3 for Chinese, 9 encodings specific to the Windows operating system, and 16 DOS code pages.
Unicode was created to provide a unified way of representing all the characters which occur in most writing systems, including those of dead languages.

The unicode standard itself is not an encoding standard, but rather a list characters with a number assigned to each one. 
These numbers are what are called code points.
For example, the capital letter A is the 65th letter in unicode, usually written in the hex 41.
In the standard way of writing code points, this would be written as U+0041.
You may notice that the unicode code point for the capital letter A is the same as in ASCII.
This feature was exploited to create the most common text encoding on the internet, UTF-8.

Character encodings were created to represent, in binary, all the code points allowed within unicode.
One encoding in particular has become the dominant one for text on the internet [#f1]_, UTF-8.
UTF-8 is a variable length encoding, meaning a character can take anywhere from 1 to 6 bytes to represent.
In UTF-8, the first 127 characters of unicode are encoded with only one byte.
Since the first 127 code points in unicode are exactly the same as in ASCII, the UTF-8 representation of any unicode character less than 128 is ASCII.
This allows forward compatability of ASCII with UTF-8, and if containing only code points below 128, a UTF-8 file will be backwards compatable with ASCII.

Unicode Representation in this Document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Characters in this document will be defined as unicode code points in the format U+#### where the # symbols are hexidecimal numbers.
Since exchange files are defined to be UTF-8 encoded, this unambigiously specifies the exact bits which may occur in a file.

**(Could be helpful to have a table of the unicode code points and the character glyphs from U+0021 to U+007E as on this** `wikipedia page`_ **or this other page** http://www.utf8-chartable.de/unicode-utf8-table.pl?number=128 **)**

.. _wikipedia page: https://en.wikipedia.org/wiki/List_of_Unicode_characters#Basic_Latin

.. [#f1] As of March 2015, 83.7% of the text on the internet is encoded with UTF-8.
