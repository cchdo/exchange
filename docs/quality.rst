.. _Quality Codes:

Quality Codes
=============

Most parameters may also have an associated column of numeric quality flags.
Quality flag columns appear as a normal parameter in the :ref:`parameter and unit lines`. They MUST NOT have any associated units.
The quality flag parameter name is constructed from the parameter name and the suffix _FLAG_W where the W stands for a WOCE flag. **(Is this correct about the meaning of W?  In the parameters section, you mention parameter names that don't have WOCE quality codes and so shouldn't have a parameter name followed by _FLAG_W such as BIONBR.  But does this mean it can have quality flags such as a suffix of _FLAG?)**
The quality flag parameter name requires parsing to determine which parameter it needs to be associated with.

The basic formula for constructing a quality flag parameter name is:

  .. code::
    
    <PARAMETER_NAME>_FLAG_W

where ``<PARAMETER_NAME>`` is the parameter for which the quality flags are for.

For example, the quality column for the parameter :ref:`CTDOXY (UMOL/KG)` would be ``CTDOXY_FLAG_W``.

The meaning of the flags is determined by the type of measurement it is.
Bottles have `Bottle Quality Codes`_, measurements from CTD based instruments use the `CTD Quality Codes`_, and discrete measurements from bottle use the `Water Quality Codes`_.
The quality codes to use for any specific parameter is also :ref:`listed with each parameter <Parameters>` in the parameters section.

All quality flag codes are single digit integers.

The following descriptions of each quality code is taken from the WOCE manual.

.. _Bottle Quality Codes:

WOCE Bottle Quality Codes
-------------------------

======= ===========
Code    Description
======= ===========
1       Bottle information unavailable.
2       No problems noted.
3       Leaking.
4       Did not trip correctly.
5       Not reported.
\(6\)   (Significant discrepancy in measured values between Gerard and Niskin bottles.)
\(7\)   (Unknown problem.)
\(8\)   (Pair did not trip correctly. Note that the Niskin bottle can trip at an unplanned depth while the Gerard trips correctly and vice versa.)
9       Samples not drawn from this bottle.
======= ===========


.. _Water Quality Codes:

WOCE Water Sample Quality Codes
-------------------------------

======= ===========
Code    Description
======= ===========
1       Sample for this measurement was drawn from water bottle but analysis not received. 
2       Acceptable measurement.
3       Questionable measurement.
4       Bad measurement.
5       Not reported.
6       Mean of replicate measurements (Number of replicates should be specified in the .DOC file and the replicate data tabulated there).
7       Manual chromatographic peak measurement.
8       Irregular digital chromatographic peak integration.
9       Sample not drawn for this measurement from this bottle.
======= ===========

.. note::
  Note that if water is drawn for any measurement from a water bottle, the quality code for that parameter should be set equal to 1 initially to help ensure that all water samples are accounted for.

.. _CTD Quality Codes:

WOCE CTD Quality Codes
----------------------

======= ===========
Code    Description
======= ===========
1       Not calibrated.
2       Acceptable measurement.
3       Questionable measurement.
4       Bad measurement.
5       Not reported.
6       Interpolated over a pressure interval larger than 2 dbar.
7       Despiked.
\(8\)   Not used for CTD data.
9       Not sampled.
======= ===========

..
    .. _CTD Quality Codes:
    
    Time Quality Codes
    ------------------
    
    .. warning::
      Time flags are a proposed way of disambiguating the source of time information.
      They are not final, do not use time flags until this warning is removed.
    
    ============= =============
    Flag Value    Definition
    ============= =============
    1             Time is cast start (typical for CTD files)
    2             Time is cast bottom (typical for Bottle files)
    3             Time reference is unknown (probably ok, do not use for time resolutions less than 6 hours)
    4             Times might be bad (don't use for applications needing exact time)
    5             No time in original (times set to 0000, times not to be used)
    6             Time is cast end (uncommon)
    7             Time is bottle close
    ============= =============
    
    Quality Code Mappings
    ---------------------
