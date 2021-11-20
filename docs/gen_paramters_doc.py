import json
import itertools
from textwrap import indent, dedent
from cchdo.params import WHPNames

flag_refs = {
    "woce_ctd": ":ref:`CTD Quality Codes`",
    "woce_discrete": ":ref:`Water Quality Codes`",
    "woce_bottle": ":ref:`Bottle Quality Codes`",
}

parameters = WHPNames.legacy_json
schema = WHPNames.legacy_json_schema

with open("parameters.json", "w") as f:
    json.dump(parameters, f, indent=2)
with open("parameters.schema.json", "w") as f:
    json.dump(schema, f, indent=2)


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
                first["alt_units"].append(str(alt["whp_unit"]))
                first["alt_cf_units"].append(str(alt.get("cf_unit",)))
                first["alt_cf_names"].append(str(alt.get("cf_name",)))
            except KeyError:
                first["alt_units"] = [str(alt["whp_unit"])]
                first["alt_cf_units"] = [str(alt.get("cf_unit", ))]
                first["alt_cf_names"] = [str(alt.get("cf_name", ))]
        else:
            params.append(alt)

def gen_cf_table(param):
    whp_units = [param.get("whp_unit"), *param.get("alt_units", [])]
    cf_units = [param.get("cf_unit"), *param.get("alt_cf_units", [])]
    cf_names = [param.get("cf_name"), *param.get("alt_cf_names", [])]

    rows = []
    for whp, unit, name in zip(whp_units, cf_units, cf_names):
        rows.append(dedent(f"""\
        * - ``{whp}``
          - ``{unit}``
          - ``{name}``\
        """))
    table_body = "\n".join(rows)
    table_header = dedent("""\
        .. list-table::
            :header-rows: 1

            * - ``whp_unit``
              - ``units``
              - ``standard_name``\
        """)

    return "\n".join([table_header, indent(table_body, "    ")])


with open('_autogen_paramlist', 'w') as f:
    f.write('''
.. _parameters-list:

Parameters
----------
This section was generated automatically from a 
:download:`machine readable list of parameters <parameters.json>`,
there is also a
:download:`validation schema <parameters.schema.json>` for the
parameters json.

.. hlist::
  :columns: 3

''')


# Make the 3 column list of params at the top of the page
    for param in params:
        name = param["whp_name"]
        f.write(f"  * `{name}`_\n")

    for param in params:
        name = param["whp_name"]
        unit = param.get('whp_unit')

        ## make the ref and title
        f.write(f"\n.. _{name}:\n\n{name}\n")

        ## Underline that title
        f.write("^" * len(param["whp_name"]) + '\n\n')
        data_type = param['data_type']
        quality_flags = str(param['flag_w'])

        f.write(f":Units:\n  * {unit}\n")
        if "alt_units" in param:
            for alt_unit in param["alt_units"]:
                f.write(f"  * {alt_unit}\n")

        f.write(f":Data Type: {data_type}\n")
        if quality_flags != "None":
            flag_ref = flag_refs[quality_flags]
            f.write(f":{param['whp_name']}_FLAG_W Definitions: {flag_ref}\n")

        if "error_name" in param:
            f.write(f":Error Column Label: {param.get('error_name', '')}\n")

        f.write(f"\n:CF/netCDF Attributes:\n{indent(gen_cf_table(param), '  ')}\n")

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

