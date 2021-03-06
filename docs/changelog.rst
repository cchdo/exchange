Changelog
=========

2016-01-08 (1.2)
----------------
* Add section on missing values (-999).
  This was a major ommission from the 1.0 release.

2016-01-06 (1.1)
----------------
* Add an ``ARBITRARY`` unit that any parameter MAY use.

2015-11-16 (1.0.1)
------------------
* Added Parameters

  * XMISS [0-5VDC]
  * FLUOR [0-5VDC]
  * CTDNOBS
  * CTDETIME [SECONDS]

2015-10-29
----------
* Organized the text encoding requirements better.
* Added note about requirement levels following RFC 2119.

2015-04-27
----------
* Define the structure of a ``_ct1.zip`` archive.

2015-01-21
----------
* Paramters no longer will have a print format, now will just have a data type

2014-08-18
----------
* Less restrictive parameter names and units.
* Specify how numerical data should appear.
* CCHDO now keeps numerical precsion of data found in files

2014-07-24
----------
* Require parameter names in an exchange file to be unique.

2014-07-16
----------
* Changed stated file encoding to UTF-8 rather than ASCII.
  Some of the WHP-exchange bottle files have non-ASCII in the citations.
