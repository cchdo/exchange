Changelog
=========
2022-03-22
----------
Update CCHDO params list to 0.1.17

2022-01-25
----------
This is a list of all the relevant changes which have occurred since the last time this log was edited, it was shamefully neglected by the lead author.

Major Changes
``````````````
* Added parameter scope as a property, parameters must now have a scope of "cruise", "profile", or "sample".
  Cruise scoped parameters must be constant for an entire cruise (currently no parameters have this property, including Expocode)
  Profile scoped parameters must be constant for an entire profile (e.g. date, time, lat, lon, etc..).
  Sample scoped parameters may vary within a profile, these are normal data.
  Parameters appearing in CTD headers are now required to have a "profile" scope.
  This removes the ability for undocumented "user" headers to appear in the CTD headers section.
  Use comments instead for these extra bits of information.

* Removed "ARBITRARY" as a valid unit for any parameter.
  This was originally added to deal with some turbidity parameters which had "arbitrary" units, this was later discovered to be FNU/NTU which, while "arbitrary", are very specific.
  Additionally "ARBITRARY" was starting to be used erroneously for parameters which are unitless (e.g. counts and ratios).
  Going forward, specific parameters, if any, will be documented as ARBITRARY on a case by case basis in the parameters database.

* The parameters database was spun off into a separate project (parameter updates are `documented elsewhere now <https://cchdo.github.io/params/changelog.html>`_)

Minor Changes
`````````````
* Added digit characters to allowed list of chars in STNNBR, SAMPNO, and BTLNBR.
* Added GEOTR_EVENT and GEOTR_SAMPNO parameter names
* A bunch of technical changes to how the params list page is generated.
* Misc spelling corrections
* Added CTDXMISSCP as a name
* Prefixed most ctd parameters with CTD
* Removed BTLNBR as part of the sample identifying composite key to align with WOCE documentation
* Added BIOS_CASTID definition
* Linked a parameters uncertainty name to the parameter itself (e.g. DELC14 and C14ERR)
* Added a bunch of CF standard names
* Added some WHP Parameter ID numbers, these are the numbers seen in sumfiles.
* Added a "reference_scale" attribute to temperature and practical salinity parameters.
* Started on a table to display the various options/known units for each parameter.

2016-01-08 (1.2)
----------------
* Add section on missing values (-999).
  This was a major omission from the 1.0 release.

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
* Parameters no longer will have a print format, now will just have a data type

2014-08-18
----------
* Less restrictive parameter names and units.
* Specify how numerical data should appear.
* CCHDO now keeps numerical precision of data found in files

2014-07-24
----------
* Require parameter names in an exchange file to be unique.

2014-07-16
----------
* Changed stated file encoding to UTF-8 rather than ASCII.
  Some of the WHP-exchange bottle files have non-ASCII in the citations.
