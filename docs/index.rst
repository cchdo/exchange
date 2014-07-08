.. Exchange Format documentation master file, created by
   sphinx-quickstart on Mon Jul  7 15:13:12 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Description of WHP-Exchange Format for CTD/Hydrographic Data
============================================================

Summary
-------
Exchange formats for the CCHDO CTD and bottle data are described.
The WHP-exchange formats provide simplified exchange and improved readability of hydrographic data.
WHP-exchange data files carry the essential information from CTD and water sample profiles in rigorously-described comma-delimited (csv) ASCII formats designed to ease data exchange and simplify data import.


Overview of WHP-exchange file formats
-------------------------------------
The WHP-exchange bottle and CTD data formats include these features:

* ASCII, spreadsheet-like
* comma-delimited values (csv)
* no special meaning to blank/empty spaces
* station information in every line in the file (bottle) or in the top lines in each file (CTD)
* only one missing data value defined for all parameters
* missing data value format defined in the format for each parameter
* WHP quality flag, when provided, associated directly with its parameter
* positions in decimal degrees
* dates in YYYYMMDD format

There are three types of WHP-exchange format files, each with a unique 8-character suffix:


============ ================== ===========
Data Type    8-character Suffix Description
============ ================== ===========
CTD data     _ct1.csv           one CTD profile in WHP-exchange format
CTD data     _ct1.zip           zipped directory holding one or more _ct1.csv WHP-exchange CTD profiles
bottle data  _hy1.csv           data from one or more bottle profiles in WHP-exchange format
============ ================== ===========


Format description for WHP-exchange bottle data ( 8-character suffix _hy1.csv)
------------------------------------------------------------------------------
.. note::

  To better understand this section please refer to one of the WHP-Exchange bottle data files available from the CCHDO.
  The file `a24_hy1.csv`_ from the CCHDO from `http://cchdo.ucsd.edu/data/onetime/atlantic/a24/a24_hy1.csv`_ is a good example.
  It is recommended that the reader examine `a24_hy1.csv`_ both in a text editor application - in order to see all characters - and also in a spreadsheet application - in order to view overall layout.
  
  .. _a24_hy1.csv: http://cchdo.ucsd.edu/data/onetime/atlantic/a24/a24_hy1.csv
  .. _http://cchdo.ucsd.edu/data/onetime/atlantic/a24/a24_hy1.csv: http://cchdo.ucsd.edu/data/onetime/atlantic/a24/a24_hy1.csv

The overall layout of a _hy1.csv bottle data file is described in Table 1.

The first line ("line" = "row") of a WHP-exchange format file is a single word which describes the file type, in this case "BOTTLE", followed by a comma and a date/time stamp.

The format next provides for 0-N optional information lines, each beginning with a "#" character, near the beginning of a _hy1.csv file.
The CCHDO uses "#" lines to hold file history and data citation information referring to the data originators.

A description of the station information columns of a _hy1.csv file is in Table 2.

A description of the remaining data columns and preferred parameter names is in Table 3. 

A line with "END_DATA" signals the end of the data lines.

After that line, a bottle data file may hold other file-specific documentation.
The primary documentation for WHP data will, however, remain in the ".doc" file (or zipped directory).


General rules for WHP-exchange_hy1.csv data files:
``````````````````````````````````````````````````

Each line must end with a carriage return or end-of-line.

With the exception of (1) the file type line, (2) lines starting with a "#" character, or (2) including and following a line which reads "END_DATA", each line in a _hy1.csv file must have exactly the same number of commas as do all other lines in that file.

The number and names of the parameters in a _hy1.csv file is not specifically addressed, except that for WHP data certain parameters are noted as REQUIRED.
For example, it is not necessary that a bottle data file contain columns for CFC measurements when there are no CFC data.

The order of the header and bottle data parameters in a _hy1.csv file is preferred to be similar to that shown in the example "a24_hy1.csv", especially for the first 13 columns, but is not strictly required.
Although the _hy1.csv files should be as consistent as feasible in this regard, data users are urged to use "read" statements that are sensitive to parameter names rather than position of the parameter in the data files.
Here is the order used in " a24_hy1.csv"::

  EXPOCODE, SECT_ID, STNNBR, CASTNO, SAMPNO, BTLNBR, BTLNBR_FLAG_W, DATE, TIME, LATITUDE, LONGITUDE, DEPTH, CTDPRS, CTDTMP, CTDSAL, CTDSAL_FLAG_W, SALNTY, SALNTY_FLAG_W, CTDOXY, CTDOXY_FLAG_W, OXYGEN, OXYGEN_FLAG_W, SILCAT,  SILCAT_FLAG_W, NITRAT, NITRAT_FLAG_W, NITRIT, NITRIT_FLAG_W, PHSPHT, PHSPHT_FLAG_W, CFC-11, CFC-11_FLAG_W, CFC-12, CFC-12_FLAG_W, TRITUM, TRITUM_FLAG_W, HELIUM, HELIUM_FLAG_W, DELHE3, DELHE3_FLAG_W, TCARBN, TCARBN_FLAG_W, PCO2, PCO2_FLAG_W, ALKALI, ALKALI_FLAG_W, PH, PH_FLAG_W, PCO2TMP, CTDRAW, HELIER, DELHER, THETA, TRITER

All parameters defined as alphanumeric (e.g.,"A14") and integer (e.g., "I4") will be shown in the full defined width and will be right-justified, meaning that entries shorter than the defined width  will be padded with meaningless spaces to the left of the first character (for example, EXPOCODEs are usually shorter than the defined maximum of 14 alphanumeric characters).

The bottle data parameter names should follow those listed in Table 3 when feasible.
Data providers are urged to use caution, however, and list their actual parameter name rather than a WHP parameter name whenever there is any question on this matter.

Each data parameter listed in Table 3 - except for all flags, which are "I1" - will be listed in "F9.x" floating point format, where "x" indicates the number of decimal places.
For each parameter, the CCHDO will pad with meaningless zeros data received with fewer decimal places and round data received with extra decimal places to the number of decimal places specified in Table 3.

When a quality flag is available for a parameter, that quality flag shall be placed in the column immediately to the right of the parameter. 
The name of a quality flag always begins with the name of the parameter with which it is associated, followed by an underscore character, followed by "FLAG", followed by an underscore, and then followed by an alphanumeric character indicating the flag type.
(Also see Appendix, "Parameter Quality Codes".)

The "missing value" for a data value is always defined as -999, but written in the decimal place format of the parameter in question.
For example, a missing salinity would be written -999.0000 or a missing phosphate -999.00.
The value -999 was chosen because it is out of range for all WOCE-era parameters.

.. table:: Table 1. General description of _hy1.csv file layout.

  ===========  ==========================================================================================================================================
  1st line     File type, here BOTTLE, followed by a comma and a DATE_TIME stamp

               YYYYMMDDdivINSwho

               YYYY
                  4 digit year
               MM
                  2 digit month
               DD
                  2 digit day
               div
                  division of Institution
               INS
                  Institution name
               who
                  initials of responsible person

               example:  20000711CCHSIOSCD
  #lines       A file may include 0-N optional lines, typically at the start of a data file, but after the file type line, each beginning with a "#" character and each ending with carriage return or end-of-line.
               Information relevant to file change/update history of the file itself may be included here, for example.
  2nd line     Column headings.
               A list of column headings approved and used by the CCHDO is found in Table 2.
               A list of parameter headings approved and used by the CCHDO is found in Table 3.
               Data originators are urged, however, to be careful to supply their **correct** column headings rather than to simply copy 'approved' column headings into their files.
  3rd line     Units.
               A list of parameter units used by the CCHDO is found in Tables 2 and 3.
               Data originators are urged, however, to be careful to supply their **correct** units rather than to simply copy the units used by the CCHDO.
  data lines   As many data lines may be included in a single file as is convenient for the user, with the proviso that the number and order of parameters, parameter order, headings, units, and commas remain absolutely consistent throughout a single file.
               Thus a single data file may contain data lines for as little as one bottle from one cruise to as much as many bottles from many cruises.
  END_DATA     The line after the last data line must read END_DATA, and be followed by a carriage return or end of line.
  other lines  Users may include any information they wish in 0-N optional lines at the end of a data file, after the END_DATA line.
  ===========  ==========================================================================================================================================


.. note::
  Within a _hy1.csv file it is very strongly preferred that data from each station be contiguous, it is recommended that data from each cast at a station be contiguous, and it is preferred that the data from each cast be sorted from lowest pressure to highest pressure.


.. toctree::
   :maxdepth: 2
