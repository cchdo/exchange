import unittest
import os
import json

from jsonschema import validate

this_path = os.path.abspath(__file__)
this_dir = os.path.dirname(this_path)
json_path = os.path.join(this_dir, "..", "meta/parameters.json")
json_path = os.path.normpath(json_path)
schema_path = os.path.join(this_dir, "..", "meta/parameters.schema.json")
schema_path = os.path.normpath(schema_path)

class TestParametersJSON(unittest.TestCase):
    def setUp(self):
        with open(json_path, 'r') as f:
            try:
                self.parameters = json.load(f)
            except ValueError:
                self.fail(msg="The paramters file is not valid JSON")
        with open(schema_path, 'r') as f:
            try:
                self.schema = json.load(f)
            except ValueError:
                self.fail(msg="The paramters schema is not valid JSON")

    def testValidateSchema(self):
        validate(self.parameters, self.schema)

    def testUniqueParameters(self):
        pairs = []
        for param in self.parameters:
           pairs.append((param['whp_name'], param['whp_unit']))

        self.assertEqual(len(pairs), len(set(pairs)), msg="Duplicate param "\
        "name/unit pairs")



if __name__ == "__main__":
    unittest.main()
