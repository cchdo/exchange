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

    # Basic Root level tests
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

    # Paramter key tests
    def testParameterItemsType(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param, dict)

    def testUniqueParameterItems(self):
        pairs = []
        for param in self.p['parameters']:
            pairs.append((param['whp_name'], param['whp_unit']))

        self.assertEqual(len(pairs), len(set(pairs)), msg="Duplicate param "\
        "name/unit pairs")

    def testWHPNameIsUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['whp_name'], unicode)

    def testWHPUnitIsUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['whp_unit'], unicode)

    def testFlagWisUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['flag_w'], unicode)

    def testFlagWinQualityList(self):
        quality_flags = self.p['quality'].keys()
        for param in self.p['parameters']:
            if isinstance(param['flag_w'], unicode):
                self.assertIn(param['flag_w'], quality_flags)
            else:
                assert True

    def testCFNameisUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['cf_name'], unicode)

    def testUdunitsIsUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['udunits'], unicode)

    def testDataTypeisUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['data_type'], unicode)

    def testDataTypeIsAllowedValue(self):
        allowed_values = [u'string', u'integer', u'decimal']
        for param in self.p['parameters']:
            self.assertIn(param['data_type'], allowed_values)

    def testNumericMinIsNumberOrNull(self):
        for param in self.p['parameters']:
            is_number = isinstance(param['numeric_min'], float)
            is_null = param['numeric_min'] is None
            self.assertTrue(is_number or is_null)

    def testNumericMaxIsNumberOrNull(self):
        for param in self.p['parameters']:
            is_number = isinstance(param['numeric_max'], float)
            is_null = param['numeric_max'] is None
            self.assertTrue(is_number or is_null)

    def testStringFormatIsUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['string_format'], unicode)

    def testStringFormatValueIsOK(self):
        for param in self.p['parameters']:
            self.assertTrue(param['string_format'].startswith('%'))
            if param['data_type'] == u'string':
                self.assertTrue(param['string_format'].endswith('s'))
            if param['data_type'] == u'integer':
                self.assertTrue(param['string_format'].endswith('i'))
            if param['data_type'] == u'decimal':
                self.assertTrue(param['string_format'].endswith('f'))
            try:
                float(param['string_format'][1:-1])
                assert True
            except ValueError:
                assert False

    def testDescriptionIsUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['description'], unicode)

    def testNoteIsUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['note'], unicode)

    def testWarningIsUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['warning'], unicode)

    def testWhpTierIsUnicode(self):
        for param in self.p['parameters']:
            self.assertIsInstance(param['whp_tier'], unicode)

    def testWhpTierValue(self):
        allowed_values = [u'primary', u'secondary', u'tertiary']
        for param in self.p['parameters']:
            self.assertIn(param['whp_tier'], allowed_values)

if __name__ == "__main__":
    unittest.main()
