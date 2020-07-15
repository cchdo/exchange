.. _Parameters:

Parameters
==========

About Parameters
----------------
The CCHDO works frequently with many parameters common in hydrography.
Provided here is a description of many common parameters encountered in exchange files.

.. warning::
  This list may not contain every parameter which may be encountered in an exchange file.
  CCHDO is working on providing a machine readable list of ALL parameters which may be encountered in all files.
  This list will include parameters which CCHDO lacks a description for (known unknown parameters).

  Until that time, parameters may appear in exchange formats from the CCHDO which are not documented here.
  No undocumented parameter or field will cause data integrity or usefulness issues (i.e. all undocumented parameters may be safely ignored).

Definitions
^^^^^^^^^^^
Provided with each parameter is a set of information in a table, the information included in that table should be interpreted as follows:

:Units: 
    These are the common units encountered for this parameter as it will appear in the exchange document itself.
    The special units of "None" means the field will be either blank or contain only whitespace.
:Data Type: 
    Specifies the allowed type of data in the data records for this parameter.
    There are three types of data, string (str), integers (int), and decimal.
    String data types may be any printing character except a comma ``,`` which is the field seperator.
    Integer data types may only contain numbers without a decimal point, quality flags are usually integers.
    Decimal data types may be any real number (including an integer) and may include decimal point, the precision is not specified.
:Quality Flags: 
    Specifies which set of quality flag definitions should be used to interpret a quality flag column for this parameter (if present).
    Current quality flags are: :ref:`bottle <Bottle Quality Codes>`, :ref:`water <Water Quality Codes>`, :ref:`ctd <CTD Quality Codes>`.
    See the :ref:`Quality Codes` section for more information
:Alternate Units:
    Some parameters might have alternate units which might also be in data files.
:Error Column Label:
    A parameter might contain an error or uncertanty value associated with it.
    The column which contains the error/uncertanty values for this parameter will have the name listed in this field.


Unlisted Parameters
-------------------
Otherwise valid exchange files which contain parameters, units, or parameter/unit pairs that are
not listed in the :ref:`common-parameters` list SHALL NOT cause the file to be
invalid so long as the rest of the specification is adhered to.

Pass Through
^^^^^^^^^^^^
Authors of software which read and write exchange files SHOULD pass though unlisted parameters, units, parameter/unit pairs, and the associated data columns.

.. note::
    This section is intended for software which is used in data management, it does not impose a requirement on authors only wishing to do analysis.


.. include:: _autogen_paramlist
