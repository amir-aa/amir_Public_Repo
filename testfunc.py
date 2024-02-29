import inspect
import unittest
from faker import Faker
from your_module import *  

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_all_functions(self):
        # Get all functions from the module
        functions = inspect.getmembers(your_module, inspect.isfunction)

        for function_name, function_obj in functions:
            with self.subTest(f"Testing {function_name}"):
                # Generate fake parameters for the function
                fake_params = self.generate_fake_params(function_obj)

                # Call the function with fake parameters
                try:
                    result = function_obj(*fake_params)

                    # Add assertions based on your expectations
                    # For example:
                    # self.assertIsInstance(result, expected_type)
                    # self.assertEqual(result, expected_result)

                except Exception as e:
                    # Handle exceptions, if any
                    self.fail(f"Error in {function_name}: {e}")

    def generate_fake_params(self, function_obj):
        # Generate fake parameters for a function
        params = inspect.signature(function_obj).parameters
        fake_params = []

        for param_name, param_info in params.items():
            # Check if the parameter has a default value
            if param_info.default != inspect.Parameter.empty:
                fake_params.append(param_info.default)
            else:
               
                fake_value = self.generate_fake_value(param_info.annotation)
                fake_params.append(fake_value)

        return fake_params

    def generate_fake_value(self, param_type):
        # Generate a fake value based on the parameter's type
        if param_type == int:
            return self.fake.random_int()
        elif param_type == str:
            return self.fake.word()
        elif param_type == float:
            return self.fake.random_float()
        elif param_type == bool:
            return self.fake.boolean()
        # Add more types as needed

if __name__ == '__main__':
    unittest.main()
