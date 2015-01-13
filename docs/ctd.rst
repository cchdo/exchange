.. _CTD Specific:

CTD Specific
============
Exchange CTD files follow all the common format specifications with the addition of some header information.
They MUST only contain one profile per file.

.. _CTD Specific Headers:

Additional CTD Headers
----------------------
Rather than encode information which would remain constant throughout the cast with the :ref:`data lines`, Exchange CTD files store this information in headers that appear after the :ref:`comment line(s)`, but before the :ref:`parameter and unit lines`.
These headers follow the basic form::

  PARAM = VALUE

Where the ``PARAM`` is some paramter name (e.g. ``DEPTH``) and the ``VALUE`` is the value for that paramter (e.g. ``4523``).
Each param-value pair ends end with a line-ending charicter.
Here is an example of a complete set of CTD headers (note that we have included line numbers, these are not part of the header):

.. code-block:: ini
  :linenos:

  NUMBER_HEADERS = 11
  EXPOCODE = 318M20130321
  SECT_ID = P02W
  STNNBR = 1
  CASTNO = 2
  DATE = 20130322
  TIME = 2205
  LATITUDE =  32.5068
  LONGITUDE =  133.0297
  DEPTH =   166
  INSTRUMENT_ID = 796

Notice three things: the special ``NUMBER_HEADERS`` paramter, the paramter names are all caps, and none of the paramters have units.

The ``NUMBER_HEADERS`` paramter is an integer describing how many lines the headers will be before the paramter and unit lines.
The value of ``NUMBER_HEADERS`` includes itself and MUST be the first line after any :ref:`comment line(s)`.
The units for each parameter are defined by convention rather than explicitly stated in each file, see the :ref:`CTD required headers` for information on the units and which headers are required.

.. warning::
  The most common mistake with Exchange CTD Headers is not including the ``NUMBER_HEADERS`` line in the calculation of the number of lines the headers occupy.
  It would be incorrect in the above example to have ``NUMBER_HEADERS = 10``.

.. _CTD required headers:

CTD Header Descriptions
-----------------------
This list is not all inclusive, any number of user submitted headers may occur so long as the follow the ``PARAM = VALUE`` format and the ``NUMBER_HEADERS`` value all header lines.

* NUMBER_HEADERS_
* EXPOCODE_
* SECT_ID_
* STNNBR_
* CASTNO_
* DATE_
* TIME_
* LATITUDE_
* LONGITUDE_
* DEPTH_

NUMBER_HEADERS
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          I2
Required        YES
=============== =========

EXPOCODE
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          A14
Required        YES
=============== =========

The expedition code for the cruise.
See :ref:`expocode` on the paramters page for more information.


SECT_ID
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          A6
Required        No
=============== =========

If present, the WHP Section Identifier.
See :ref:`sect_id` on the paramters page for more information.

.. note::
  Previous versions of the exchange format specification included both ``SECT_ID`` and ``SECT``.
  The canonical paramter name is ``SECT_ID``.
  However, ``SECT`` may still be encountered in exchange CTD files from the CCHDO.

STNNBR
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          A6
Required        YES
=============== =========

The origionators station number.
See :ref:`stnnbr` on the paramters page for more information.

CASTNO
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          A6
Required        YES
=============== =========

The origionator's cast number.
See :ref:`castno` on the paramters page for more information.

DATE
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          I8
Required        YES
=============== =========

The UTC date in YYYYMMDD format.
Usually the reported date is for the bottom of the cast.

TIME
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          I4
Required        YES
=============== =========

The UTC time in HHMM format.
Usually the reported time is for the bottom of the cast.

LATITUDE
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          F8.4
Required        YES
=============== =========

The latitude in decimal degrees.
Values are positive in the northern hemisphere, negative in the southern hemisphere.
Must contain only numeric charicters and an ASCII hyphen (``-``) to indicate negative values.

.. note::
  Previous versions of the exchange format specification requried positions not reliable to the ten-thousandths place should be padded with zeros to conform to the format specification.
  This changes the significant figures and is no longer reccomended, ALWAYS report data to the precision measured.
  Implimenters of CTD exchange file readers should be able to handle any valid signed number in this field.

LONGITUDE
^^^^^^^^^^^^^^

=============== =========
Units           None
Format          F8.4
Required        YES
=============== =========

The longitude in decimal degrees.
Values are positive in the eastern hemisphere, negative in the western hemisphere.
Must contain only numeric charicters and an ASCII hyphen (``-``) to indicate negative values.

DEPTH
^^^^^^^^^^^^^^

=============== =========
Units           Meters
Format          I4
Required        No
=============== =========

The bottom depth in meters.
The CCHDO preferrs corrected depths.
Often there will be a comment field describing how the depth was calcualted.
For example, "Depth is CTD_DEPTH + DISTANCE_ABOVE_BOTTOM at max pressure".

.. _preferred order:

Preferred Header Order
-----------------------
The only header which must come first is ``NUMBER_HEADERS``.
Other header paramters may come in any order, however, there is a preferred order.
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

Followed by any extra user submitted headers.
  

.. _example ctd data:

Example CTD Data
----------------
Here is an example of a complete exchange CTD file (though very short for a profile):

.. code-block:: none

  CTD,20130709ODF
  # REPORTED CAST DEPTH IS CTD_DEPTH + DISTANCE_ABOVE_BOTTOM AT MAX PRESSURE
  NUMBER_HEADERS = 11
  EXPOCODE = 318M20130321
  SECT_ID = P02W
  STNNBR = 1
  CASTNO = 2
  DATE = 20130322
  TIME = 2205
  LATITUDE =  32.5068
  LONGITUDE =  133.0297
  DEPTH =   166
  INSTRUMENT_ID = 796
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

Notice the stricture is:

1. :ref:`File Identification Stamp`
2. :ref:`comment line(s)`
3. :ref:`CTD Specific Headers` with the user defined ``INSTRUMENT_ID``
4. :ref:`parameter and unit lines`
5. Finally :ref:`data lines`.

.. _ctd zip archive:

Structure of ZIP CTD Archives
-----------------------------
Since exchange CTD files only contain one profile, it is convient to package them into entire an archive containing an entire cruise.
The archve format exchange uses is zip, specifically PKZIP 2.0.
The zip archive allows for a large varity of structure so it is nessessary to define the structure here.

TODO: Confirm if documentation should be allowed in the zip archives, historicaly yes, but it might break JOA. It is easy to just say "only attempt to read the _ct1.csv files".

WORKING DRAFT:
Exchange CTD zip files MUST contain a flattened structure, that is, only files with no directory paths.
The files within the zip should be in the same order in which the stations were done.
Usually this means the filenames contain numerical information reguarding the station order.
All the files within the zip MUST have the ``_ct1.csv`` file extention. (fix if documentation is allowed)
