Bottle Specific
===============
Exchange Bottle files follow all the common format specifications for their structure.
The :ref:`File Identification Stamp` of an exchange bottle file starts with ``BOTTLE``.
Each :ref:`data line <data lines>` in an exchange bottle file represents a single bottle closure.

When ctd parameters are encountered within exchange bottle files (e.g. :ref:`CTDPRS (DBAR)`) they represent the corrected values being read by the CTD at the time of bottle closure, usually averaged over some interval.

In bottle files, specific parameters are REQUIRED to be present and have non fill values.

.. _bottle required headers:

Required Bottle Parameters
--------------------------

The following parameters are REQUIRED to be present in exchange bottle files where the parameter name occurs within the :ref:`parameter and unit lines` and their values be present in the :ref:`data lines`.

* :ref:`EXPOCODE`
* :ref:`STNNBR`
* :ref:`CASTNO`
* :ref:`DATE`
* :ref:`LATITUDE`
* :ref:`LONGITUDE`
* :ref:`CTDPRS (DBAR)`
* :ref:`SAMPNO`


.. versionchanged:: 1.3
  Removed :ref:`BTLNBR` as being one of two options for required columns.

Unique Line Identification
--------------------------

Since each :ref:`data line <data lines>` of an exchange bottle file represents a single bottle closure, enough information must be present on each line to uniquely identify closure event.
This is to allow the integration of all the measurements of samples taken from that bottle at a later time.
The identification is done by requiring a combination of values from specific parameters to be unique throughout the file.

The following combination of parameters must have unique values:

* :ref:`EXPOCODE`
* :ref:`STNNBR`
* :ref:`CASTNO`
* :ref:`SAMPNO`

.. versionchanged:: 1.3
  Since :ref:`BTLNBR` as a being a valid identifier for samples.

Unique Line Identification Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In these examples, the long parameter, unit, and data lines truncated by ``[...]``.

The following example exchange bottle data is all from the same cruise
indicated by the expocode: ``33RO20131223``, the same station: ``1``, the same cast ``2``, but the bottle number and sample numbers
differ (``24`` and ``23``).

.. code-block:: none
  :linenos:

    BOTTLE,20150327CCHSIORJL
    # From submitted file a16s_2013_final_discrete_o2.csv: 
    # Merged parameters: OXYGEN_FLAG_W
    EXPOCODE,STNNBR,CASTNO,SAMPNO,BTLNBR[...]
    ,,,,[...]
    33RO20131223,       1,          2,         24,         24[...]
    33RO20131223,       1,          2,         23,         23[...]
    END_DATA

The following example shows an example of duplicated unique identification parameter values.
More than one line contains the exact same values for :ref:`EXPOCODE`, :ref:`STNNBR`, :ref:`CASTNO`, and :ref:`SAMPNO`.

.. code-block:: none
  :linenos:

    BOTTLE,20150327CCHSIORJL
    # From submitted file a16s_2013_final_discrete_o2.csv: 
    # Merged parameters: OXYGEN_FLAG_W
    EXPOCODE,STNNBR,CASTNO,SAMPNO,BTLNBR[...]
    ,,,,[...]
    33RO20131223,       1,          2,         24,         24[...]
    33RO20131223,       1,          2,         24,         23[...]
    END_DATA

.. _example bottle data:

Example Bottle Data
-------------------

.. only:: latex

  An example bottle exchange file is provided on the next page.

  .. raw:: latex
  
    \begin{landscape}
     \tiny
    \begin{verbatim}
      BOTTLE,20150327CCHSIORJL
      # From submitted file a16s_2013_final_discrete_o2.csv: 
      # Merged parameters: OXYGEN_FLAG_W
      #|
      #|
      #| Analysis                  Institution    Principal Investigator   email
      #| ____________________________________________________________________________________
      #| Chief Scientist           AOML           Rik Wanninkhof           rik.wanninkhof@noaa.gov
      #| Co-Chief Scientist        AOML/CIMAS     Leticia Barbero          leticia.barbero@noaa.gov
      #| CTDO                      NOAA/PMEL      Gregory Johnson          Gregory.C.Johnson@noaa.gov
      #|                           NOAA/AOML      Molly Baringer           Molly.Baringer@noaa.gov
      #| Salinity                  NOAA/AOML      Molly Baringer           Molly.Baringer@noaa.gov
      #| UW & Discrete pCO2        NOAA/AOML      Rik Wanninkhof           Rik.Wanninkhof@noaa.gov
      #| Total CO2 (DIC)           NOAA/PMEL      Richard Feely            Richard.A.Feely@noaa.gov
      #|                           NOAA/AOML      Rik Wanninkhof           Rik.Wanninkhof@noaa.gov
      #| Nutrients                 NOAA/AOML      Jia-Zhong Zhang          Jia-Zhong.Zhang@noaa.gov
      #|                           NOAA/PMEL      Calvin Mordy             Calvin.W.Mordy@noaa.gov
      #| Dissolved O2              NOAA/AOML      Molly Baringer           Molly.Baringer@noaa.gov
      #|                           RSMAS          Chris Langdon            clangdon@rsmas.miami.edu 
      #| Total Alkalinity/pH       RSMAS          Frank Millero            fmillero@rsmas.miami.edu
      #| CFCs/SF6                  NOAA/PMEL      John Bullister           John.L.Bullister@noaa.gov
      #| 3He/Tritium               LDEO           Peter Schlosser          peters@ldeo.columbia.edu
      #|                           WHOI           William Jenkins          wjenkins@whoi.edu
      #| CDOM                      UCSB/MSI       Craig Carlson            carlson@lifesci.ucsb.edu
      #| Chipod                    OSU            Jonathan Nash            nash@coas.oregonstate.edu
      #| ADCP/Lowered ADCP         U Hawaii       Eric Firing              efiring@hawaii.edu
      #| Trace Metals              FSU            William Landing          wlanding@fsu.edu
      #|                           UH             Chris Measures           measures@hawaii.edu 
      #| 14C/DIC                   WHOI           Ann McNichols            amcnichol@whoi.edu
      #|                           PU             Robert Key               key@princeton.edu
      #| DOC                       RSMAS          Dennis Hansell           dhansell@rsmas.miami.edu
      #| Data Management           SIO            James Swift              jswift@ucsd.edu
      #|                           SIO            Susan Becker             sbecker@ucsd.edu
      #|
      #|  Following American Geophysical Union recommendations, the data should be
      #|  cited as: "data provider(s), cruise name or cruise ID, data file name(s),
      #|  CLIVAR and Carbon Hydrographic Data Office, La Jolla, CA, USA, and data
      #|  file date." For further information, please contact one of the parties
      #|  listed above or cchdo@ucsd.edu. Users are also requested to acknowledge
      #|  the NSF/NOAA-funded U.S. Repeat Hydrography Program in publications resulting
      #|  from their use.
      #|
      #
      EXPOCODE,SECT_ID,STNNBR,CASTNO,SAMPNO,BTLNBR,BTLNBR_FLAG_W,DATE,TIME,LATITUDE,LONGITUDE,DEPTH,CTDPRS,CTDTMP,CTDSAL,CTDSAL_FLAG_W,SALNTY,SALNTY_FLAG_W,CTDOXY,CTDOXY_FLAG_W,OXYGEN,OXYGEN_FLAG_W
      ,,,,,,,,,,,METERS,DBAR,ITS-90,PSS-78,,PSS-78,,UMOL/KG,,UMOL/KG,
      33RO20131223,       A16S,       1,          2,         24,         24,2,20131226,       0706,    -6.0016,   -24.9998,       5809,     3.9,  26.2239,  36.3097,2,  36.3082,2,    199.1,2,   201.2,2
      33RO20131223,       A16S,       1,          2,         23,         23,2,20131226,       0704,    -6.0016,   -24.9998,       5809,    22.5,  26.2331,  36.3090,2,  36.3171,2,    199.4,2,   201.3,2
      33RO20131223,       A16S,       1,          2,         22,         22,2,20131226,       0702,    -6.0016,   -24.9998,       5809,    47.4,  26.2335,  36.3078,2,  36.3080,2,      200,2,   201.9,2
      33RO20131223,       A16S,       1,          2,         21,         21,2,20131226,       0700,    -6.0016,   -24.9998,       5809,    72.1,  26.2112,  36.3044,2,  36.3055,2,    200.6,2,     201,2
      33RO20131223,       A16S,       1,          2,         20,         20,2,20131226,       0658,    -6.0016,   -24.9998,       5809,    97.5,  24.2160,  36.1165,2,  36.1258,2,    193.2,2,   190.1,2
      33RO20131223,       A16S,       1,          2,         19,         19,2,20131226,       0656,    -6.0016,   -24.9998,       5809,   147.3,  15.5167,  35.6384,2,  35.6247,2,    104.9,2,   103.3,2
      33RO20131223,       A16S,       1,          2,         18,         18,2,20131226,       0654,    -6.0016,   -24.9998,       5809,   222.8,  12.0808,  35.1686,2,  35.1586,2,    109.3,2,   108.6,2
      33RO20131223,       A16S,       1,          2,         17,         17,2,20131226,       0651,    -6.0016,   -24.9998,       5809,   296.4,   9.8716,  34.8809,2,  34.8809,2,      124,2,     125,2
      33RO20131223,       A16S,       1,          2,         16,         16,2,20131226,       0648,    -6.0016,   -24.9998,       5809,   406.5,   8.4675,  34.7567,2,  34.7520,2,     83.8,2,    81.4,2
      33RO20131223,       A16S,       1,          2,         15,         15,2,20131226,       0645,    -6.0016,   -24.9998,       5809,   517.9,   7.1433,  34.6371,2,  34.6366,2,     93.8,2,    88.6,2
      33RO20131223,       A16S,       1,          2,         14,         14,2,20131226,       0642,    -6.0016,   -24.9998,       5809,   647.7,   5.5545,  34.5066,2,  34.5046,2,    139.4,2,   130.5,2
      33RO20131223,       A16S,       1,          2,         13,         13,2,20131226,       0638,    -6.0016,   -24.9998,       5809,   791.9,   4.6390,  34.4845,2,  34.4826,2,    158.6,2,   148.5,2
      33RO20131223,       A16S,       1,          2,         12,         12,2,20131226,       0633,    -6.0016,   -24.9998,       5809,  1047.4,   4.2414,  34.6431,2,  34.6429,2,    163.9,2,   163.7,2
      33RO20131223,       A16S,       1,          2,         11,         11,2,20131226,       0627,    -6.0016,   -24.9998,       5809,  1347.9,   4.3278,  34.8700,2,  34.8698,2,    197.4,2,   197.1,2
      33RO20131223,       A16S,       1,          2,         10,         10,2,20131226,       0619,    -6.0016,   -24.9998,       5809,  1747.8,   3.8921,  34.9665,2,  34.9664,2,    238.6,2,   238.3,2
      33RO20131223,       A16S,       1,          2,          9,          9,2,20131226,       0611,    -6.0016,   -24.9998,       5809,  2147.8,   3.2522,  34.9412,2,  34.9420,2,    242.7,2,   243.6,2
      33RO20131223,       A16S,       1,          2,          8,          8,2,20131226,       0602,    -6.0016,   -24.9998,       5809,  2597.5,   2.8568,  34.9202,2,  34.9188,2,    242.6,2,   242.3,2
      33RO20131223,       A16S,       1,          2,          7,          7,3,20131226,       0553,    -6.0016,   -24.9998,       5809,  3097.5,   2.6784,  34.9194,2,  34.9176,2,    251.1,2,   251.7,2
      33RO20131223,       A16S,       1,          2,          6,          6,3,20131226,       0544,    -6.0016,   -24.9998,       5809,  3598.4,   2.4902,  34.9073,2,  34.9727,4,    255.1,2,   235.6,4
      33RO20131223,       A16S,       1,          2,          5,          5,2,20131226,       0534,    -6.0016,   -24.9998,       5809,  4098.5,   1.8197,  34.8364,2,  34.8340,2,    242.3,2,   243.2,2
      33RO20131223,       A16S,       1,          2,          4,          4,2,20131226,       0524,    -6.0016,   -24.9998,       5809,    4598,   0.9865,  34.7443,2,  34.7432,2,    225.6,2,   226.4,2
      33RO20131223,       A16S,       1,          2,          3,          3,2,20131226,       0515,    -6.0016,   -24.9998,       5809,  5097.2,   0.7993,  34.7170,2,  34.7167,2,    220.1,2,   221.9,2
      33RO20131223,       A16S,       1,          2,          2,          2,2,20131226,       0505,    -6.0016,   -24.9998,       5809,  5597.3,   0.7292,  34.7031,2,  34.7024,2,    219.8,2,   219.9,2
      33RO20131223,       A16S,       1,          2,          1,          1,3,20131226,       0459,    -6.0016,   -24.9998,       5809,  5904.3,   0.7651,  34.7023,2,  34.7049,2,    219.9,2,   220.9,2
      33RO20131223,       A16S,       2,          1,         24,         24,2,20131226,       1421,    -6.4977,   -24.9999,       5628,     3.1,  26.2387,  36.2430,2,  36.2424,2,    201.5,2,   202.1,2
      33RO20131223,       A16S,       2,          1,         23,         23,2,20131226,       1419,    -6.4977,   -24.9999,       5628,    27.9,  26.1705,  36.2402,2,  36.2394,2,    202.2,2,   202.2,2
      33RO20131223,       A16S,       2,          1,         22,         22,3,20131226,       1417,    -6.4977,   -24.9999,       5628,    67.9,  26.1326,  36.2369,2,  36.2353,2,    201.5,2,   202.3,2
      33RO20131223,       A16S,       2,          1,         21,         21,2,20131226,       1415,    -6.4977,   -24.9999,       5628,   107.1,  22.8199,  36.1452,2,  36.1454,2,    168.2,2,   170.3,2
      33RO20131223,       A16S,       2,          1,         20,         20,2,20131226,       1412,    -6.4977,   -24.9999,       5628,   172.4,  15.2580,  35.6092,2,  35.6393,4,      112,2,   112.6,2
      33RO20131223,       A16S,       2,          1,         19,         19,2,20131226,       1410,    -6.4977,   -24.9999,       5628,   257.5,  10.8796,  35.0258,2,  35.0261,2,     92.4,2,    92.3,2
      33RO20131223,       A16S,       2,          1,         18,         18,2,20131226,       1407,    -6.4977,   -24.9999,       5628,   367.8,   9.2106,  34.8337,2,  34.8338,2,     75.2,2,    75.6,2
      END_DATA
    \end{verbatim}
    \end{landscape}

.. only:: html

  .. code-block:: none
    :linenos:
  
    BOTTLE,20150327CCHSIORJL
    # From submitted file a16s_2013_final_discrete_o2.csv: 
    # Merged parameters: OXYGEN_FLAG_W
    EXPOCODE,SECT_ID,STNNBR,CASTNO,SAMPNO,BTLNBR,BTLNBR_FLAG_W,DATE,TIME,LATITUDE,LONGITUDE,DEPTH,CTDPRS,CTDTMP,CTDSAL,CTDSAL_FLAG_W,SALNTY,SALNTY_FLAG_W,CTDOXY,CTDOXY_FLAG_W,OXYGEN,OXYGEN_FLAG_W
    ,,,,,,,,,,,METERS,DBAR,ITS-90,PSS-78,,PSS-78,,UMOL/KG,,UMOL/KG,
    33RO20131223,       A16S,       1,          2,         24,         24,2,20131226,       0706,    -6.0016,   -24.9998,       5809,     3.9,  26.2239,  36.3097,2,  36.3082,2,    199.1,2,   201.2,2
    33RO20131223,       A16S,       1,          2,         23,         23,2,20131226,       0704,    -6.0016,   -24.9998,       5809,    22.5,  26.2331,  36.3090,2,  36.3171,2,    199.4,2,   201.3,2
    33RO20131223,       A16S,       1,          2,         22,         22,2,20131226,       0702,    -6.0016,   -24.9998,       5809,    47.4,  26.2335,  36.3078,2,  36.3080,2,      200,2,   201.9,2
    33RO20131223,       A16S,       1,          2,         21,         21,2,20131226,       0700,    -6.0016,   -24.9998,       5809,    72.1,  26.2112,  36.3044,2,  36.3055,2,    200.6,2,     201,2
    33RO20131223,       A16S,       1,          2,         20,         20,2,20131226,       0658,    -6.0016,   -24.9998,       5809,    97.5,  24.2160,  36.1165,2,  36.1258,2,    193.2,2,   190.1,2
    END_DATA

The basic strucutre is:

* Line 1: :ref:`File Identification Stamp` starting with ``BOTTLE``
* Line 2, 3: :ref:`comment line(s)`
* Lines 3, 4: :ref:`parameter and unit lines`
* Lines 6-11: :ref:`data lines`.
