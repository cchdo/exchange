.. _Quality Codes:

Quality Codes
=============

Bottle Quality Codes
--------------------

============= =============
Flag Value    Definition
============= =============
1             Bottle information unavailable.
2             No problems noted.
3             Leaking.
4             Did not trip correctly.
5             Not reported.
\(6\)         (Significant discrepancy in measured values between Gerard and Niskin bottles.)
\(7\)         (Unknown problem.)
\(8\)         (Pair did not trip correctly. Note that the Niskin bottle can trip at an unplanned depth while the Gerard trips correctly and vice versa.)
9             Samples not drawn from this bottle.
============= =============

Water Sample Quality Codes
--------------------------

============= =============
Flag Value    Definition
============= =============
1             Sample for this measurement was drawn from water bottle but analysis not received. 
2             Acceptable measurement.
3             Questionable measurement.
4             Bad measurement.
5             Not reported.
6             Mean of replicate measurements (Number of replicates should be specified in the .DOC file and the replicate data tabulated there).
7             Manual chromatographic peak measurement.
8             Irregular digital chromatographic peak integration.
9             Sample not drawn for this measurement from this bottle.
============= =============

.. note::
  Note that if water is drawn for any measurement from a water bottle, the quality code for that parameter should be set equal to 1 initially to help ensure that all water samples are accounted for.

CTD Quality Codes
-----------------

============= =============
Flag Value    Definition
============= =============
1             Not calibrated.
2             Acceptable measurement.
3             Questionable measurement.
4             Bad measurement.
5             Not reported.
6             Interpolated over a pressure interval larger than 2 dbar.
7             Despiked.
\(8\)         (Not used for CTD data.)
9             Not sampled.
============= =============

Quality Code Mappings
---------------------
