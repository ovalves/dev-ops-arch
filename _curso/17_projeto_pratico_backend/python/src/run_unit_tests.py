import unittest

loader = unittest.TestLoader()
test_modules = [
    '__shared.tests.unit.domain.test_unit_value_objects',
    '__shared.tests.unit.domain.test_unit_entities',
    'category.tests.unit.domain.test_unit_entities'
]

suite = unittest.TestSuite()
for test in test_modules:
    try:
        mod = __import__(test, globals(), locals(), ['suite'])
        suite_fn = getattr(mod, 'suite')
        suite.addTest(suite_fn())
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

unittest.TextTestRunner().run(suite)