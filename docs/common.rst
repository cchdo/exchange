Common Format Features
======================
Certain format specifications are shared between the bottle and CTD WHP-exchange files.
Those common features are described in this section.

File Requirements
-----------------

Encoding
````````
WHP-exchange text files MUST be UTF-8 encoded.

.. note::
  UTF-8 was chosen as the encoding for WHP-Exchange files because it is backwards compatible with ASCII.
  Valid ASCII files are also valid UTF-8 files.
  UTF-8 allows for the full range of unicode points to display non ASCII text.

.. warning::
  Be careful if editing or creating files on Windows as the default text encoding is UTF-16.
  UTF-16 is not compatible with UTF-8 or ASCII.

Byte Order Marks
````````````````
The UTF-8 encoded files MUST NOT include a BYTE ORDER MARK (U+FEFF).

.. note::
  Not including a byte order mark ensures backwards compatibility with ASCII when the file contains only code points less than U+007F.

Line Endings
````````````
Lines in an exchange text file MUST end with a LINE FEED (U+000A) ``\n``.
Lines MUST NOT use any other form of line ending.

.. versionchanged:: 1.3
  Disallow non "unix style" line endings.


.. _File Identification Stamp:

File Format Indicator
---------------------------------
The first bytes of a WHP-exchange file MUST contain a file identifier and SHOULD have a creation stamp separated by a :unicode_info:`,`.

Bottle File Indicator
`````````````````````
The first bytes of a WHP-exchange bottle file must be the following 6 byte sequence ``42 4F 54 54 4C 45``.
This is equivalent to ``BOTTLE`` when encoded in UTF-8.

CTD File Indicator
``````````````````
The first bytes of a WHP-exchange CTD file must be the following 3 byte sequence ``43 54 44``.
This is equivalent to ``CTD`` when encoded in UTF-8.


.. note::
  If while attempting to read a WHP-exchange file and the first line does not start with either byte sequence listed above an attempt to read the rest of the file will likely fail.
  When writing a WHP-exchange format reader, always check if this identification stamp is present and has a valid value.

Creation Stamp Convention
`````````````````````````
The creation stamp SHOULD contain the following information in the order presented, using the stamp ``20140716CCHSIOSCD`` as an example:

1) **20140716**\ CCHSIOSCD: A date stamp in the from of YYYYMMDD (ISO 8601)
2) 20140716\ **CCH**\ SIOSCD: The division (or group) of the institution that wrote the file, typically three characters.
   The CCHDO uses CCH as the division.
3) 20140716CCH\ **SIO**\ SCD: The institution that the group is associated with, typically three characters.
   The CCHDO is located at the Scripps Institution of Oceanography, thus SIO is used.
4) 20140716CCHSIO\ **SCD**: The initials of the person who wrote the file, typically three characters.
   Use only code points U+0041 to U+005A and for the initials. In this example, SCD.

.. warning::
  Do not rely on the creation stamp to be the same length in every WHP-exchange file.
  While all the same elements SHOULD be present, their lengths may vary.

Examples
````````
A bottle file identifier including a creation stamp  might look like::
  
  BOTTLE,20140716CCHSIOSCD

A CTD file identifier including a creation stamp might look like::

  CTD,20140716CCHSIOSCD

.. versionchanged:: 1.3
  Made explicit the exact bytes which should appear at the start of a file.
  Demote the file creation stamp to a strong reccomendation.

.. _comment line(s):

Optional Comment Lines
----------------------
After the `File Identification Stamp`_ any number of comment line, including none may appear.
Comment lines start with a :unicode_info:`#`.
Comment lines typically contain information about the file history and will often contain data citation information.

An example::

  # This is one line of comments
  # An additional line of comments

An example of the beginning of a file, including the `File Identification Stamp`_::

  BOTTLE,20140716CCHSIOSCD
  # This is a comment line
  # BOTTLE,20130215CCHSIOSCD

.. note::
  Notice that an older `File Identification Stamp`_ is in a comment line.
  This is a convention often used by the CCHDO to record when changes were made to files

.. warning::
  Comments may contain UTF-8 encoded code points above U+007F, especially in proper names that may be present with data citation information.
  If writing your own WHP-exchange reader, ensure that it can handle code points above U+007F or have it skip comment lines without trying to read them.

.. _parameter and unit lines:

Parameter and Unit Lines
-------------------------
.. warning::
  There are additional headers specific to CTD WHP-exchange files.
  See the :ref:`CTD Specific Headers` section for details on these additional headers.

After any format specific headers, the parameter and unit lines are next.
The parameter names are first, units are second.

Parameter names are :unicode_info:`,` separated values that define the columns the exchange file will contain.
The names must be unique, capitalized, contain no empty fields, and not end with a trailing comma.
The parameter names must contain only code points in the range U+0021 to U+007E except a :unicode_info:`,`.
A trailing comma, or a comma that occurs at the end of the line with nothing else after it, MUST NOT be included on the parameter line.
Certain parameter names, or parameter combinations, are required to be present.
See the respective sections on :ref:`bottle required headers` and :ref:`CTD required headers` for information specific to each format.

The unit line contains information for the units of each parameter listed in the parameter line.
The unit line, like the parameters, are comma separated values.
Like the parameter names, units must contain only code points in the range U+0021 to U+007E except a :unicode_info:`,`.
A trailing comma MUST NOT be included in the unit line.
Units may contain empty fields if the parameter has no units.
Units for a parameter must be in the same column as that parameter, essentially, the same number of commas occur before the parameter name and its unit.

.. warning::
  Parameter names and units MUST NOT contain commas as part of the name or unit.
  Commas are reserved for separating the, names, units, and data into columns.


The parameter and unit lines of a CTD file might look like this::

  CTDPRS,CTDPRS_FLAG_W,CTDTMP,CTDSAL,CTDOXY
  DBAR,,ITS-90,PSS-78,UMOL/KG

Note the presence of quality flag column (suffixed with ``_FLAG_W``) which has the corresponding units of nothing denoted by two commas next to each other.
For more information on quality flags, see the :ref:`Quality Codes` section.
White space MUST have no meaning in the exchange format so it may be included for purely aesthetic reasons.
The parameter and units could very easily have looked like::

  CTDPRS, CTDPRS_FLAG_W, CTDTMP, CTDSAL, CTDOXY
    DBAR,              , ITS-90, PSS-78, UMOL/KG

.. note::
  Some technical details for formatting the whitespace.

  While not strictly required, parameter, units, and data lines may contain whitespace matching the length of the print format of the parameter.
  This is a convention followed by the CCHDO to ease reading of files by humans.
  Quality flag columns usually have a 1 character width which will often cause the parameter/units and data to not be aligned into pretty columns.

.. _data lines:

Data Lines
----------
The data lines occur directly after the unit line.
Each line of data contains :unicode_info:`,` separated values of related data.
Each data point of the data line may contain any combination of characters from U+0020 to U+007F except a :unicode_info:`,`.
Like the `Parameter and Unit Lines`_, a trailing comma MUST NOT be included at the end of each line.
Data points for each parameter of the `Parameter and Unit Lines`_ must be in the same column as that parameter, i.e. the same number of commas occur before the parameter label and the datum.

Numeric data which occurs on the data lines MUST only contain numbers, spaces, an optional decimal marker, and an optional negative sign.
All whitespace within data lines has no semantic meaning.
Integers may be represented as bare numerals with no decimal marker.
All real numeric data (i.e. data that are real numbers) MUST be decimal and MUST represent their decimal mark using a :unicode_info:`.`.
For both negative real numbers and integers, prepend a :unicode_info:`-` to the numeric portion, positive real numbers MUST NOT be prefixed by a :unicode_info:`+`.

The validity of each datum is determined by the parameter column in which it occurs.
For example, the `EXPOCODE` column may contain any combination of letter, numbers, or symbols (except a comma).
A `CTDPRS` column may only contain real decimal numbers (U+0030 to U+0039) using a :unicode_info:`.` as the decimal mark.

.. note::
  Parameters may have a different precision depending on how the measurement was made.
  The CCHDO maintains a list of parameter names which includes precisions for historic reasons.
  Previous versions of the Exchange format specification stated the CCHDO would pad "meaningless" zeros to the end of any data without enough precision.
  Newer software allows the CCHDO to keep the precision as reported, both less and more precise.
  For these and other reasons, a mix of precisions may occur in a column of data.
  
  **Always report the precision as measured.**

.. warning::
  The exchange format currently has no support for quoted strings within the parameter, unit, and data lines.
  This means it is not possible for any meaningful whitespace to be included.

After all data lines, the end of the data is indicated by a line containing only ``END_DATA``.
Here is a short example of what exchange data might look like::

  2.0,2,  19.1840,  34.6935,    220.8
  4.0,2,  19.1992,  34.6924,    220.7
  6.0,2,  19.2002,  34.6922,    220.5
  8.0,2,  19.2022,  34.6920,    220.5
  END_DATA

Missing Data Values
```````````````````
Missing data may occur in any position of a column of data, including all positions.
When data are missing from a column, a fill value must be used to indicate "no data".
The fill value in exchange files is :unicode_info:`-` followed by three :unicode_info:`9`, i.e. ``-999``.
No other characters other than whitespace should occur within the missing data position.

Missing data values MAY still have :ref:`Quality Codes` associated which can give information as to why the data are missing.

Here is an example of exchange data with missing values::

  2.0,2,  19.1840,  34.6935,    220.8
  4.0,2,     -999,  34.6924,    220.7
  6.0,2,  19.2002,  34.6922,     -999
  8.0,2,  19.2022,  34.6920,    220.5
  END_DATA

.. note::
  Previous versions of the exchange format specified that the fill value should be in the precision of the rest of the column.
  For example, if a salinity was missing from a column, it would have the fill value of ``-999.0000``.
  This has changed for several reasons:

  * The precision of the data within a column is not fixed.
  * A few parameters have valid range which includes -999 as a numeric value.

  When encountering older exchange files, the fill value might contain the extra zeros after the decimal point.
  In the majority of cases, these are fill values and not numeric values.


Post Data Content
-----------------
After the ``END_DATA`` line, any additional content may be included without format restriction.
Additional content after ``END_DATA`` MUST continue to be UTF-8 encoded.


Examples
--------
Full examples of data in exchange format are presented in their specific sections:

* :ref:`Example Bottle Data`
* :ref:`Example CTD Data`
