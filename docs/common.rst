Common Format Features
======================
Certain format specifications are shared between the bottle and CTD WHP-exchange files.
All WHP-exchange text files must be UTF-8 encoded.
Unix style line endings (LF) are preferred, DOS line endings (CR+LF) are acceptable, other line endings should be avoided.

.. note::
  UTF-8 was chosen as the encoding for WHP-Exchange files because it is backwards compatable with ASCII.
  Valid ASCII files are also valid UTF-8 files.
  UTF-8 allows for the full range of unicode points to display non ASCII text.
  Non ASCII text should only be encountered in the comment lines of an enchnage file.

.. warning::
  Be careful if editing or creating files on Windows as the default text encoduing is UTF-16.
  UTF-16 is not compatable with UTF-8 or ASCII.

For both CTD and Bottle files the first rows must be the following and in the presented order:

1) A REQUIRED `File Identification Stamp`_
2) Optional `comment line(s)`_

.. _File Identification Stamp:

File Identification Stamp
---------------------------------
The first line of a WHP-exchange file contains the file identifier and a creation stamp seperated by a comma.
The file itendifier will be either ``BOTTLE`` in the case of water samples or ``CTD`` in the case of a CTD profile.
The creation stamp contains information on when the file was created and who created it.


A bottle file identifier will look like::
  
  BOTTLE,20140716CCHSIOSCD

A CTD file identifier will look like::

  CTD,20140716CCHSIOSCD

.. note::
  If while attempting to read a WHP-exchange file and the first line does not start with ``BOTTLE`` or ``CTD`` an attempt to read the rest of the file will likely fail.
  When writing a WHP-exchange format reader, always check if this identification stamp is present and has a valid value.

The creation stamp contians the following information:

1) **20140716**\ CCHSIOSCD: A date stamp in the from of YYYYMMDD (ISO 8601)
2) 20140716\ **CCH**\ SIOSCD: The division (or group) of the instituion that wrote the file, typically three charicters.
   The CCHDO uses CCH as the division.
3) 20140716CCH\ **SIO**\ SCD: The instituion that the group is associated with, typically three charicters.
   The CCHDO is locaded at the Scripps Instituion of Oceanography, thus SIO is used.
4) 20140716CCHSIO\ **SCD**: The initials of the person who wrote the file, typically three charicters.
   Use only ASCII for the initials. In this example, SCD.

.. warning::
  Do not rely on the creation stamp to be the same legnth in every WHP-exchange file.
  While all the same elemnts will be present, their lengths may vary.

.. _comment line(s):

Optional Comment Lines
----------------------
After the `File Identification Stamp`_ any number of comment line, including none may appear.
Comment lines start with a hash or pound sign: ``#``.
Comment lines typically contain information about the file history and will often contain data citation information.

An example::

  # This is one line of comments
  # An additional line of comments

An example of the begining of a file, including the `File Identification Stamp`_::

  BOTTLE,20140716CCHSIOSCD
  # This is a comment line
  # BOTTLE,20130215CCHSIOSCD

.. note::
  Notice that an older `File Identification Stamp`_ is in a comment line.
  This is a convention often used by the CCHDO to record when changes were made to files

.. warning::
  Comments may contain non-ASCII charicters, especially in proper names that may be present with data citation information.
  If writing your own WHP-exchange reader, ensure that it can handle non-ASCII UTF-8 charicters or have it skip comment lines without trying to read them.

.. _parameter and unit lines:

Parameter and Unit Lines
-------------------------
.. warning::
  There are additional headers specific to CTD WHP-exchange files.
  See the :ref:`CTD Specific Headers` section for details on these additional headers.

After any format specific headers, the parameter and unit lines are next.
The parameter names are first, units are second.

Parameter names are comma (``,``) seperated values that define the columns the exchange file will contain.
The names must be unique, capitalized, contain no empty fields, and not end with a trailing comma.
The parameter names must contain only ASCII letters, numbers, and symbols with the exception of a comma.
A trailing comma, or a comma that occurs at the end of the line with nothing else after it, MUST NOT be included on the parameter line.
Certain parameter names, or parameter combinations, are required to be present.
See the respective sections on :ref:`bottle required headers` and :ref:`CTD required headers` for information specific to each format.

The unit line contains information for the units of each parameter listed in the parameter line.
The unit line, like the paramters, are comma seperated values.
Like the parameter names, units must contain only ASCII letters, numbers, and symbols with the exception of a comma.
A trailing comma MUST NOT be included in the unit line.
Units may contain empty fields if the parameter has no units.
Units for a paramter must be in the same column as that paramter, essentialy, the sname number of commas occur before the parameter name and its unit.

.. warning::
  Parameter names and units MUST NOT contain commas as part of the name or unit.
  Commas are reserved for seperating the, names, units, and data into columns.


The parameter and unit lines of a CTD file might look like this::

  CTDPRS,CTDPRS_FLAG_W,CTDTMP,CTDSAL,CTDOXY
  DBAR,,ITS-90,PSS-78,UMOL/KG

Note the presence of quality flag column (suffixed with ``_FLAG_W``) which has the corrisponding units of nothing denoted by two commas next to each other.
For more information on quality flags, see the :ref:`Quality Codes` section.
White space has no meaning in the exchange format and can be included for purly asthetic reasons.
The parameter and units could very easially have looked like::

  CTDPRS, CTDPRS_FLAG_W, CTDTMP, CTDSAL, CTDOXY
    DBAR,              , ITS-90, PSS-78, UMOL/KG

.. note::
  Some technical details for formatting the whitespace.

  While not strictly requiered, parameter, units, and data lines may contain white space matching the length of the print format of the paramter.
  This is a convention followed by the CCHDO to ease reading of files by humans.
  Quality flag columns usually have a 1 charicter width which will often cause the parameter/units and data to not be aligned into pretty columns.

.. _data lines:

Data Lines
----------
The data lines occur directly after the unit line.
Each line of data contains comma (``,``) seperated values of related data.
Each data point of the data line may contain any combination of ASCII letter, numbers, and symbols with the exception of a comma.
Like the `Parameter and Unit Lines`_, a trailing comma MUST NOT be included at the end of each line.
Data points for each parameter of the `Parameter and Unit Lines`_ must be in the same column as that paratemer, i.e. the same number of commas occur before the parameter label and the datum.

Numeric data which occurs on the data lines MUST only contain numbers, spaces, an optional decimal marker, and an optional negative sign.
All whitespace within numerical data is ignored and has no meaning.
Integers may be represented as bare numerals with no decimal marker.
All real numeric data (i.e. data that are real numbers) MUST be decimal and MUST represent their decimal mark using an ASCII period (``.``).
For both negative real numbers and integers, prepend an ASCII hyphen (``-``) to the numeric portion, positive real numbers MUST not be prefixed by a plus sign (``+``).

The validity of each datum is determined by the parameter column in which it occurs.
For example, the `EXPOCODE` column may contain any combination of letter, numbers, or symbols (except a comma).
A `CTDPRS` column may only contain real decimal numbers using an ASCII period (``.``) as the decimal mark.

.. note::
  Parameters may have a different precision depending on how the measurement was made.
  The CCHDO maintains a list of parameter names which includes precisions for historic reasons.
  Previous versions of the Exchange format specification stated the CCHDO would pad "meaningless" zeros to the end of any data without enough precision.
  Newer software allows the CCHDO to keep the precision as reported, both less and more precise.
  For these and other reasons, a mix of precisions may occur in a column of data.
  
  Always report the precision as measured.

After all datalines, the end of the data is indicated by a line containing only ``END_DATA``.
Here is a short example of what exchange data might look like::

  2.0,2,  19.1840,  34.6935,    220.8
  4.0,2,  19.1992,  34.6924,    220.7
  6.0,2,  19.2002,  34.6922,    220.5
  8.0,2,  19.2022,  34.6920,    220.5
  END_DATA


Post Data Content
-----------------
After the ``END_DATA`` line, any additional content may be included without format restriction.
Additional content after ``END_DATA`` MUST continue to be UTF-8 encoded.


Examples
--------
Full examples of data in exchange format are presented in their speciifc sections:

* :ref:`Example Bottle Data`
* :ref:`Example CTD Data`
