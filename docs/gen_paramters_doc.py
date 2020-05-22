import json
import itertools

flag_refs = {
    "woce_ctd": ":ref:`CTD Quality Codes`",
    "woce_discrete": ":ref:`Water Quality Codes`",
    "woce_bottle": ":ref:`Bottle Quality Codes`",
}

with open("../meta/parameters.json", 'r') as f:
    parameters = json.load(f)


## group the params that only are only different by units into a single param
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

with open('_autogen_paramlist', 'w') as f:
    f.write('''
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

''')

# Make the 3 column list of params at the top of the page
    for param in params:
        name = param["whp_name"]
        unit = param.get('whp_unit')
        if unit is None:
            f.write(f"  * {name}_\n")
        else:
            f.write(f"  * `{name} ({unit})`_\n")

    for param in params:
        name = param["whp_name"]
        unit = param.get('whp_unit')

        ## make the ref and title
        if unit is None:
            f.write(f"\n.. _{name}:\n\n{name}\n")
        else:
            f.write(f"\n.. _{name} ({unit}):\n\n{name}\n")

        ## Underline that title
        f.write("^" * len(param["whp_name"]) + '\n\n')
        data_type = param['data_type']
        quality_flags = str(param['flag_w'])

        f.write(f":Units: {unit}\n")
        f.write(f":Data Type: {data_type}\n")
        if quality_flags != "None":
            flag_ref = flag_refs[quality_flags]
            f.write(f":{param['whp_name']}_FLAG_W Definitions: {flag_ref}\n")
        if "alt_units" in param:
            f.write(f":Alternate Units: {', '.join(param['alt_units'])}\n")
        if "error_name" in param:
            f.write(f":Error Column Label: {param.get('error_name', '')}\n")
        if "cf_name" in param:
            f.write(f":CF Standard Name: {param['cf_name']}\n")
        if "cf_unit" in param:
            f.write(f":CF Units: {param['cf_unit']}\n")

        f.write(f"\n{param.get('description', '')}\n")

        if quality_flags == "None":
            f.write((f"\n.. warning::\n"
                       f"  ``{name}`` does not have woce quality codes."
                       f"  ``{name}_FLAG_W`` should not appear in data file"
                       f"  :ref:`parameter and unit lines`.\n"))
        if param.get('note'):
            f.write("\n.. note::\n")
            for line in param['note'].split("\n"):
                f.write(f"  {line}\n")
        if param.get('warning'):
            f.write("\n.. warning::\n")
            for line in param['warning'].split("\n"):
                f.write(f"  {line}\n")

        f.write("\n.. raw:: html\n\n  <hr />\n")

