'''Tests the format of the paramters json.

Uses only the standard library. This is so no special env is needed for running
the tests. Alternative was to use a third party library such as JSONSchema, it
is better (and easier to control) if this is not the case.
'''
import os
import json
import unittest

this_path = os.path.abspath(__file__)
this_dir = os.path.dirname(this_path)
json_path = os.path.join(this_dir, "..", "parameters.json")
json_path = os.path.normpath(json_path)

class TestParametersJSON(unittest.TestCase):
    def setUp(self):
        with open(json_path, 'r') as f:
            try:
                self.p = json.load(f)
            except ValueError:
                self.fail(msg="The paramters file is not valid JSON")

    def testRootKeys(self):
        self.assertIn("parameters", self.p)
        self.assertIn("quality", self.p)
        self.assertIn("formats", self.p)
        self.assertEqual(len(self.p.keys()), 3, msg="Additional object keys "\
        "found at root level of paramters json")

    def testParamtersKeyType(self):
        self.assertIsInstance(self.p["parameters"], list)

    def testQualityKeyType(self):
        self.assertIsInstance(self.p["quality"], dict)

    def testFormatsKeyType(self):
        self.assertIsInstance(self.p["formats"], dict)

if __name__ == "__main__":
    unittest.main()
