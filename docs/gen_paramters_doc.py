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

params_sorted = list(
            dict.fromkeys(sorted(WHPNames.values(), key=lambda x: x.rank)).keys()
        )

with open("parameters.json", "w") as f:
    json.dump(parameters, f, indent=2)
with open("parameters.schema.json", "w") as f:
    json.dump(schema, f, indent=2)


## group the params that only are only different by units into a single param
params = []
groups = itertools.groupby(params_sorted, key=lambda x: getattr(x, "whp_name"))
for group in groups:
    first = next(group[1])
    params.append(first)
    for alt in group[1]:
        # we only care about the human readable stuff for this
        tests = [
                getattr(alt, "description") == getattr(first, "description"),
                getattr(alt, "note") == getattr(first, "note"),
                getattr(alt, "warning") == getattr(first, "warning"),
                ]
        if all(tests):
            try:
                first.__dict__["alt_units"].append(str(alt.whp_unit))
                first.__dict__["alt_cf_units"].append(str(alt.cf_unit))
                first.__dict__["alt_cf_names"].append(str(alt.cf_name))
                first.__dict__["alt_nc_name"].append(str(alt.nc_name))
            except KeyError:
                first.__dict__["alt_units"] = [str(alt.whp_unit)]
                first.__dict__["alt_cf_units"] = [str(alt.cf_unit)]
                first.__dict__["alt_cf_names"] = [str(alt.cf_name)]
                first.__dict__["alt_nc_name"] = [str(alt.nc_name)]
        else:
            params.append(alt)

def gen_cf_table(param):
    whp_units = [param.whp_unit, *param.__dict__.get("alt_units", [])]
    cf_units = [param.cf_unit, *param.__dict__.get("alt_cf_units", [])]
    cf_names = [param.cf_name, *param.__dict__.get("alt_cf_names", [])]
    cf_vars = [param.nc_name, *param.__dict__.get("alt_nc_name", [])]

    rows = []
    for nc_var, whp, unit, name in zip(cf_vars, whp_units, cf_units, cf_names):
        rows.append(dedent(f"""\
        * - ``{nc_var}``
          - ``{whp}``
          - ``{unit}``
          - ``{name}``\
        """))
    table_body = "\n".join(rows)
    table_header = dedent("""\
        .. list-table::
            :header-rows: 1

            * - ``nc_var`` name
              - ``whp_unit``
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
        name = param.whp_name
        f.write(f"  * `{name}`_\n")

    for param in params:
        name = param.whp_name
        unit = param.whp_unit

        ## make the ref and title
        f.write(f"\n.. _{name}:\n\n{name}\n")

        ## Underline that title
        f.write("^" * len(param.whp_name) + '\n\n')
        data_type = param.dtype
        quality_flags = param.flag_w

        f.write(f":Units:\n  * {unit}\n")
        if "alt_units" in param.__dict__:
            for alt_unit in param.__dict__["alt_units"]:
                f.write(f"  * {alt_unit}\n")

        f.write(f":Data Type: {data_type}\n")
        if quality_flags != "no_flags":
            flag_ref = flag_refs[quality_flags]
            f.write(f":{param.whp_name}_FLAG_W Definitions: {flag_ref}\n")

        if param.error_name is not None:
            f.write(f":Error Column Label: {param.error_name}\n")

        f.write(f"\n:CF/netCDF Attributes:\n{indent(gen_cf_table(param), '  ')}\n")

        f.write(f"\n{param.description}\n")

        if quality_flags == "None":
            f.write((f"\n.. warning::\n"
                       f"  ``{name}`` does not have woce quality codes."
                       f"  ``{name}_FLAG_W`` should not appear in data file"
                       f"  :ref:`parameter and unit lines`.\n"))
        if param.note is not None:
            f.write("\n.. note::\n")
            for line in param.note.split("\n"):
                f.write(f"  {line}\n")
        if param.warning is not None and param.warning != "":
            f.write("\n.. warning::\n")
            for line in param.warning.split("\n"):
                f.write(f"  {line}\n")

        f.write("\n.. raw:: html\n\n  <hr />\n")

