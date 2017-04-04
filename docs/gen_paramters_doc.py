import json

with open("../meta/parameters.json", 'r') as f:
    parameters = json.load(f)

output = '''
.. _common-parameters:

Common Parameters
-----------------
This section was generated automatically from a 
:download:`machine readable list of parameters <../meta/parameters.json>`,
there is also a
:download:`validation schema <../meta/parameters.schema.json>` for the
parameters json.

.. hlist::
  :columns: 3

'''
import itertools
params = []
groups = itertools.groupby(parameters, key=lambda x: x["whp_name"])
for group in groups:
    first = next(group[1])
    params.append(first)
    for alt in group[1]:
        # we only care about the human readable stuff for this
        tests = [
                alt.get("description") == first.get("description"),
                alt.get("note") == first.get("note"),
                alt.get("warning") == first.get("warning"),
                ]
        if all(tests):
            try:
                first["alt_units"].append(alt["whp_unit"])
            except KeyError:
                first["alt_units"] = [alt["whp_unit"]]
        else:
            params.append(alt)
for param in params:
    unit = param.get('whp_unit')
    if unit is None:
        output += "  * {0}_\n".format(param["whp_name"])
    else:
        output += "  * `{0} ({1})`_\n".format(param["whp_name"], unit)

for param in params:
    unit = param.get('whp_unit')
    if unit is None:
        output += '''
.. _{0}:

{0}\n'''.format(param["whp_name"])
    else:
        output += '''
.. _{0} ({1}):

{0}\n'''.format(param["whp_name"], unit)

    output += "^" * len(param["whp_name"]) + '\n\n'
    data_type = param['data_type']
    quality_flags = str(param['flag_w'])

    unit = str(unit)
    units_label = "Units"
    data_label = "Data Type"
    quality_label = "{}_FLAG_W Definitions".format(param['whp_name'])

    aliases = param.get("aliases")

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
    if aliases:
        output += "Aliases".ljust(first_col) + ' ' + ", ".join(aliases) + '\n'
    output += "=" * first_col + ' ' + "=" * second_col + '\n'

    output += """
{0}
""".format(param.get('description', ""))

    if quality_flags == "None":
        output += ("\n.. warning::\n"
                   "  ``{name}`` does not have woce quality codes."
                   "  ``{name}_FLAG_W`` should not appear in data file"
                   "  :ref:`parameter and unit lines`.\n").format(
                name=param["whp_name"]
                )
    if param.get('note'):
        output += """\n.. note::\n"""
        for line in param['note'].split("\n"):
            output += "  {}\n".format(line)
    if param.get('warning'):
        output += """\n.. warning::\n"""
        for line in param['warning'].split("\n"):
            output += "  {}\n".format(line)

    output += "\n.. raw:: html\n\n  <hr />\n"

with open('_autogen_paramlist', 'w') as f:
    f.write(output)
