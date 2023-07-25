import unittest
from src.__shared.application.usecases import UseCase


class TestBaseUsecasesUnit(unittest.TestCase):
    def test_throw_error_when_methods_not_implemented(self):
        with self.assertRaises(TypeError) as assert_error:
            UseCase()

        self.assertEqual(
            assert_error.exception.args[0],
            "Can't instantiate abstract class UseCase with abstract method execute",
        )
