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

alias_json_path = os.path.join(this_dir, "..", "meta/aliases.json")
alias_json_path = os.path.normpath(alias_json_path)
alias_schema_path = os.path.join(this_dir, "..", "meta/aliases.schema.json")
alias_schema_path = os.path.normpath(alias_schema_path)

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

        with open(alias_json_path, 'r') as f:
            try:
                self.aliases = json.load(f)
            except ValueError:
                self.fail(msg="The alias file is not valid JSON")
        with open(alias_schema_path, 'r') as f:
            try:
                self.alias_schema = json.load(f)
            except ValueError:
                self.fail(msg="The alias schema is not valid JSON")

    def testValidateSchema(self):
        validate(self.parameters, self.schema)

    def testValidateAliasSchema(self):
        validate(self.aliases, self.alias_schema)

    def testUniqueParameters(self):
        pairs = []
        for param in self.parameters:
           pairs.append((param['whp_name'], param['whp_unit']))

        self.assertEqual(len(pairs), len(set(pairs)), msg="Duplicate param "\
        "name/unit pairs")

    def testAliasMapsToCanonical(self):
        pairs = {((param['whp_name'], param['whp_unit'])) for param in self.parameters}
        for alias in self.aliases:
            self.assertIn((alias['canonical_name'], alias["canonical_unit"]), pairs)




if __name__ == "__main__":
    unittest.main()
