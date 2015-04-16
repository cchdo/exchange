Infrequently Changing CCHDO Metadata
====================================
Has the following metadata sets:

* Paramter Nmaes/Descriptions
* Ship/platform codes
* ISO Alpha-2 and ISO Alpha-3 country codes

Project contains the canonical set of paramters used by CCHDO for data
processing, the paramter list in the exchange documentation is
automatically generated from this data. The internal processing software
also uses this data.

This project also contains the ICES ship codes used to generate
expocodes from ship names. The ship name could be determined from the
expocode as well (by using this data).

The metadata are in JSON formats with a specific structure described
here.

Paramter Descriptions
---------------------
TODO: Write ths

Ship/Platform Codes
-------------------
TODO: Write this


ISO Country Codes
-----------------
No pull requests accepted, TODO: Write a description of the format.
(Uses third party dataset)

Test Suite Status
-----------------
Tests have been written to verify the structure and data integrity of
the json files contained within this project, this allows for the
automatic validation of any proposed changes (in pull requests).

The following badge indicates the status of the most recent commit to
the master branch:
[![Build Status](https://travis-ci.org/cchdo/hdo-metadata.svg?branch=master)](https://travis-ci.org/cchdo/hdo-metadata)
