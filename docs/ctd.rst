.. _CTD Specific:

CTD Specific
============
Exchange CTD files follow all the common format specifications with the addition of some header information.
Exchange CTD files MUST only contain one CTD profile per file. 
A zip archive can be created out of multiple CTD files for one cruise.

.. _CTD Specific Headers:

Additional CTD Headers
----------------------
Rather than encode information which would remain constant throughout the cast within the :ref:`data lines`, Exchange CTD files store this information in a block of headers that appear after the :ref:`comment line(s)`, but before the :ref:`parameter and unit lines`.

.. _NUMBER_HEADERS:

Each CTD header block must start with a line labeled NUMBER_HEADERS = integer number where integer number is the total number of additional CTD header lines defining constants plus 1.  
The 1 added accounts for the NUMBER_HEADERS line itself as this count is specifying the total number of lines appearing after optional comments and before the parameter line. 
This line takes the following form::

  NUMBER_HEADERS = integer number

The ``NUMBER_HEADERS`` parameter is an integer describing how many lines of headers there are before the parameter and unit lines and after any optional comments.
The value of ``NUMBER_HEADERS`` includes itself and is REQUIRED and MUST be the first line after any :ref:`comment line(s)`.


Additional CTD headers after the NUMBER_HEADERS count follow the basic form::

  PARAM = VALUE

Where the ``PARAM`` is some parameter name (e.g. ``DEPTH``) and the ``VALUE`` is the value for that parameter (e.g. ``4523``).
The ``PARAM``, with the exception of NUMBER_HEADERS, MAY be any parameter in the :ref:`Parameters` section.
The format of ``VALUE`` must conform to the data type listed for the parameter in the :ref:`Parameters` section.
The ``PARAM`` and ``VALUE`` are seperated by an :unicode_info:`=` and there is no meaning to any whitespace.
Each param-value pair ends with a line-ending character.
There is no limit to how many headers may be present, as long the NUMBER_HEADERS value is set correctly.

.. note::
  Any parameter which has a constant value for the entire cast MAY appear in the CTD Headers.

Here is an example of a complete set of CTD headers (note that we have included line numbers, these are not part of the header):

.. code-block:: ini
  :linenos:

  NUMBER_HEADERS = 10
  EXPOCODE = 318M20130321
  SECT_ID = P02W
  STNNBR = 1
  CASTNO = 2
  DATE = 20130322
  TIME = 2205
  LATITUDE =  32.5068
  LONGITUDE =  133.0297
  DEPTH =   166

Notice three things: the special ``NUMBER_HEADERS`` parameter at the beginning of the headers block, the parameter names are all caps, and none of the parameters have units.

The units for each parameter are defined by convention rather than explicitly stated in each file. See the :ref:`CTD required headers` section for information on which headers are required.

.. warning::
  The most common mistake with Exchange CTD Headers is not including the ``NUMBER_HEADERS`` line in the calculation of the number of lines the headers occupy.
  It would be incorrect in the above example to have ``NUMBER_HEADERS = 9``.


.. _CTD required headers:

CTD required headers
--------------------

The following CTD headers are REQUIRED, see the :ref:`Parameters` section for the description of each, except for the `NUMBER_HEADERS`_ which is described above:

* `NUMBER_HEADERS`_
* :ref:`EXPOCODE`
* :ref:`STNNBR`
* :ref:`CASTNO`
* :ref:`DATE`
* :ref:`LATITUDE`
* :ref:`LONGITUDE`

.. note::
  :ref:`TIME` is not a required parameter, this is not an omission from the list above.

.. warning::
  There is no support for including units in the CTD headers and it is not reccomended that any parameters which could have multiple units be included in the CTD headers.

  Usually the optional :ref:`DEPTH <DEPTH (METERS)>` parameter is the only one with units commonly found in CTD headers, and it MUST be in meters when included in the CTD headers.


.. _CTD Optional Headers:

CTD Optional Headers
--------------------

The following CTD headers are optional, but encountered frequently within ctd exchange files:

* :ref:`SECT_ID`
* :ref:`TIME`
* :ref:`DEPTH <DEPTH (METERS)>`


.. _preferred order:

Preferred Header Order
-----------------------
The only header which must come first is ``NUMBER_HEADERS``.
Other header parameters may come in any order, however, there is a preferred order.
The preferred order after ``NUMBER_HEADERS`` is::

  EXPOCODE
  SECT_ID
  STNNBR
  CASTNO
  DATE
  TIME
  LATITUDE
  LONGITUDE
  DEPTH


.. _example ctd data:

Example CTD Data
----------------
Here is an example of a complete exchange CTD file (though a very shallow profile):

.. code-block:: none
  :linenos:

  CTD,20130709ODF
  # REPORTED CAST DEPTH IS CTD_DEPTH + DISTANCE_ABOVE_BOTTOM AT MAX PRESSURE
  NUMBER_HEADERS = 10
  EXPOCODE = 318M20130321
  SECT_ID = P02W
  STNNBR = 1
  CASTNO = 2
  DATE = 20130322
  TIME = 2205
  LATITUDE =  32.5068
  LONGITUDE =  133.0297
  DEPTH =   166
  CTDPRS,CTDPRS_FLAG_W,CTDTMP,CTDTMP_FLAG_W,CTDSAL,CTDSAL_FLAG_W,CTDOXY,CTDOXY_FLAG_W
  DBAR,,ITS-90,,PSS-78,,UMOL/KG,
        2.0,2,  19.1840,2,  34.6935,2,    220.8,2
        4.0,2,  19.1992,2,  34.6924,2,    220.7,2
        6.0,2,  19.2002,2,  34.6922,2,    220.5,2
        8.0,2,  19.2022,2,  34.6919,2,    220.5,2
       10.0,2,  19.2033,2,  34.6918,2,    220.6,2
       12.0,2,  19.2039,2,  34.6919,2,    220.8,2
       14.0,2,  19.2033,2,  34.6919,2,    220.9,2
       16.0,2,  19.2029,2,  34.6916,2,    220.6,2
  END_DATA

The structure is:

* Line 1: :ref:`File Identification Stamp`
* Line 2: :ref:`comment line(s)`
* Lines 3-12: :ref:`CTD Specific Headers`
* Lines 13, 14: :ref:`parameter and unit lines`
* Lines 15-23: :ref:`data lines`.

.. _ctd zip archive:

Structure of ZIP CTD Archives
-----------------------------
Since Exchange CTD files only contain one profile, it is convient to package them into an archive containing an entire cruise.
The archve format exchange uses is zip, specifically PKZIP 2.0.
The zip archive allows for a large varity of structure so it is nessessary to define the structure here.

Exchange CTD zip files MUST contain a flattened structure, that is, only files with no directory paths.
The files within the zip SHOULD be in the same order in which the stations were done.
Usually this means the filenames contain numerical information regarding the station order.
All the files within the zip MUST have the ``_ct1.csv`` file extention.

Here is an example a correct ctd exchange zip archive (the output of ``unzip -l``):

.. code-block:: none

  Archive:  33RO20131223_ct1.zip
    Length     Date   Time    Name
   --------    ----   ----    ----
     401802  04-10-14 17:27   33RO20131223_00001_00002_ct1.csv
     388950  04-10-14 17:27   33RO20131223_00002_00001_ct1.csv
     385278  04-10-14 17:27   33RO20131223_00003_00002_ct1.csv
     400573  04-10-14 17:27   33RO20131223_00004_00001_ct1.csv
     395069  04-10-14 17:27   33RO20131223_00005_00002_ct1.csv
   --------                   -------
    1971672                   5 files

Notice the lack of directory paths in the archive names, it is simply filenames.
The following is an example of an incorrectly packaged archive, which has archive names containing directory structure (notice the ``/`` in the names):

.. code-block:: none

  Archive:  33RO20131223_ct1.zip
    Length     Date   Time    Name
   --------    ----   ----    ----
     401802  04-10-14 17:27   33RO20131223_ct1/33RO20131223_00001_00002_ct1.csv
     388950  04-10-14 17:27   33RO20131223_ct1/33RO20131223_00002_00001_ct1.csv
     385278  04-10-14 17:27   33RO20131223_ct1/33RO20131223_00003_00002_ct1.csv
     400573  04-10-14 17:27   33RO20131223_ct1/33RO20131223_00004_00001_ct1.csv
     395069  04-10-14 17:27   33RO20131223_ct1/33RO20131223_00005_00002_ct1.csv
   --------                   -------
    1971672                   5 files



.. note::
  Currently, the behavior when other files or directories are present is undefined.
  The recommended bahavior when encountering directories or other (non _ct1.csv) files is to ignore the extra files while warning the user of their presence.
