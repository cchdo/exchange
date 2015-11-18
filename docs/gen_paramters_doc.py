import json

with open("metadata/parameters.json", 'r') as f:
    param_list = json.load(f)

output = '''.. _Parameters:

Parameters
==========

About Paramters
---------------
The CCHDO works frequently with many parameters common in hydrography.
Provided here is a description of many common parameters encountered in exchange files.

.. warning::
  This list may not contain every parameter which may be encountered in an exchange file.
  CCHDO is working on providing a machine readable list of ALL parameters which may be encountered in all files.
  This list will include parameters which CCHDO lacks a descirption for (known unknown parameters).
  When this list becomes available, we intend to tie the generation of this parameter list with the machine readable list of parameters.

  Until that time, parameters may appear in exchange formats from the CCHDO which are not documented here.
  No undocumented parameter or field will cause data integrity or usefulness issues (i.e. all undocumented parameters may be safely ignored).

Definitions
^^^^^^^^^^^
Provided with each parameter is a set of information in a table, the information included in that table should be interpreted as follows:

* Units: 
    These are the common units encountered for this parameter as it will appear in the exchange document itself.
    The special units of "None" means the field will be either blank or contain only whitespace.
* Data Type: 
    Specifies the allowed type of data in the data records for this parameter.
    There are three types of data, string (str), integers (int), and decimal.
    String data types may be any printing character except a comma ``,`` which is the field seperator.
    Integer data types may only contain numbers without a decimal point, quality flags are usually integers.
    Decimal data types may be any real number (including an integer) and may include decimal point, the precision is not specified.
* Quality Flags: 
    Specifies which set of quality flag definitions should be used to interpret a quality flag column for this parameter (if present).
    Current quality flags are: :ref:`bottle <Bottle Quality Codes>`, :ref:`water <Water Quality Codes>`, :ref:`ctd <CTD Quality Codes>`.
    See the :ref:`Quality Codes` section for more information

Common Parameters
-----------------
This section was generated automatically from a 
:download:`machine readable list of parameters <metadata/parameters.json>`.

.. hlist::
  :columns: 3

'''
import itertools
params = []
groups = itertools.groupby(param_list["parameters"], key=lambda x: x["whp_name"])
for group in groups:
    first = next(group[1])
    params.append(first)
    for alt in group[1]:
        # we only care about the human readable stuff for this
        tests = [
                alt["description"] == first["description"],
                alt["note"] == first["note"],
                alt["warning"] == first["warning"]
                ]
        if all(tests):
            try:
                first["alt_units"].append(alt["whp_unit"])
            except KeyError:
                first["alt_units"] = [alt["whp_unit"]]
        else:
            params.append(alt)
for param in params:
    unit = param['whp_unit']
    if unit == '':
        output += "  * {0}_\n".format(param["whp_name"])
    else:
        output += "  * `{0} ({1})`_\n".format(param["whp_name"], param['whp_unit'])

for param in params:
    unit = param['whp_unit']
    if unit == '':
        output += '''
.. _{0}:

{0}\n'''.format(param["whp_name"])
    else:
        output += '''
.. _{0} ({1}):

{0}\n'''.format(param["whp_name"], unit)

    output += "^" * len(param["whp_name"]) + '\n\n'
    if unit == '':
        unit = "None"
    data_type = param['data_type']
    quality_flags = str(param['flag_w'])

    units_label = "Units"
    data_label = "Data Type"
    quality_label = "{}_FLAG_W Definitions".format(param['whp_name'])

    try:
        alternate_units = ",".join(param["alt_units"])
    except KeyError:
        alternate_units = ""

    if quality_flags == "woce_ctd":
        quality_flags = ":ref:`CTD Quality Codes`"
    if quality_flags == "woce_discrete":
        quality_flags = ":ref:`Water Quality Codes`"
    if quality_flags == "woce_bottle":
        quality_flags = ":ref:`Bottle Quality Codes`"

    first_col = max(len(units_label), len(data_label), len(quality_label))
    second_col = max(len(unit), len(data_type), len(quality_flags), len(alternate_units))



    output += "=" * first_col + ' ' + "=" * second_col + '\n'
    output += units_label.ljust(first_col) + ' ' + unit + '\n'
    output += data_label.ljust(first_col) + ' ' + data_type + '\n'
    if quality_flags != "None":
        output += quality_label.ljust(first_col) + ' ' + quality_flags + '\n'
    if "alt_units" in param:
        output += "Alternate Units".ljust(first_col) + ' ' + alternate_units + '\n'
    output += "=" * first_col + ' ' + "=" * second_col + '\n'

    output += """
{0}
""".format(param['description'])
    if quality_flags == "None":
        output += ("\n.. warning::\n"
                   "  ``{name}`` does not have woce quality codes."
                   "  ``{name}_FLAG_W`` should not appear in data file"
                   "  :ref:`parameter and unit lines`.\n").format(
                name=param["whp_name"]
                )
    if param['note'] != "":
        output += """\n.. note::\n"""
        for line in param['note'].split("\n"):
            output += "  {}\n".format(line)
    if param['warning'] != "":
        output += """\n.. warning::\n"""
        for line in param['warning'].split("\n"):
            output += "  {}\n".format(line)

with open('parameters.rst', 'wb') as f:
    f.write(output)
