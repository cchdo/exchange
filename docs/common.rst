Common Format Features
======================
Certain format specifications are shared between the bottle and CTD WHP-exchange files.
All WHP-exchange text files must be UTF-8 encoded.
Unix style line endings (LF) are preferred, DOS line endings (CR+LF) are acceptable, other line endings should be avoided.

.. note::
  UTF-8 was choisen as the encoding for WHP-Exchange files because it is backwards compatable with ASCII.
  Valid ASCII files are also valid UTF-8 files.
  UTF-8 allows for the full range of unicode points to display non ASCII text.
  Non ASCII text should only be encountered in the comment lines of an enchnage file.

.. warning::
  Be careful if editing or creating files on Windows as the default text encoduing is UTF-16.
  UTF-16 is not compatable with UTF-8 or ASCII.

For both CTD and Bottle the first two elements must be the following and in the presented order:

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
  Comment may contain non-ASCII charicters, especially in proper names that may be present with data citation information.
  If writing your own WHP-exchange reader, ensure that it can handle non-ASCII charicters or have it skip comment lines without trying to read them.

Parameter and Units Lines
-------------------------
.. warning::
  There are additional headers specific to CTD WHP-exchange files.
  See the :ref:`CTD Specific` section for details on these additional headers.

Data Lines
----------

Post Data Content
-----------------
