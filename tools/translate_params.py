import json

with open("old_params.json") as f:
    parameters = json.load(f)

new_list = []
for param in parameters:

    remove = ("udunits", "whp_tier", "string_format")
    remove_if_empty = ("note", "warning", "description", )
    remove_if_null = ("cf_name", "numeric_max", "numeric_min")

    null_if_empty = ("whp_unit", )

    string_format = param["string_format"]

    for prop in remove:
        del param[prop]

    for prop in remove_if_empty:
        if len(param[prop].strip()) == 0:
            del param[prop]

    for prop in remove_if_null:
        if param[prop] is None:
            del param[prop]

    for prop in null_if_empty:
        if len(param[prop].strip()) == 0:
            param[prop] = None


    if param["data_type"] == "string":
        param["field_width"] = int(string_format[1:-1])

    if param["data_type"] == "integer":
        param["field_width"] = int(string_format[1:-1])

    if param["data_type"] == "decimal":
        width, precision = string_format[1:-1].split(".")

        param["field_width"] = int(width)
        param["numeric_precision"] = int(precision)



    new_list.append(param)

with open("../meta/parameters.json", 'w') as f:
    json.dump(new_list, f, indent=2, sort_keys=True)
