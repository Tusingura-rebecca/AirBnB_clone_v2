"""test_city module"""
from tests.test_models.test_base_model import test_basemodel
from models import city
from models.base_model import BaseModel
import inspect
import models
import pycodestyle
import unittest
City = city.City


class test_city_docs(unittest.TestCase):
    """
    Tests to check the documentation and style of City class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_func = inspect.getmembers(City, inspect.isfunction)

    def test_city_func_docstrings(self):
        """
        Test for the presence of docstrings in city methods
        """
        for func in self.city_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_pycodestyle_conformance_city(self):
        """
        Test that models/city.py conforms to pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_conformance_test_city(self):
        """
        Test that tests/test_models/test_city.py conforms to pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """
        Test for the city.py module docstring
        """
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """
        Test for the City class docstring
        """
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")


class test_City(test_basemodel):
    """
    Tests for City class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the City instance
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test that City instance has valid attribute value for state_id
        """
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))
        self.assertEqual(type(new.state_id), str)
        if models.storage_target == 'db':
            self.assertEqual(new.state_id, None)
        else:
            self.assertEqual(new.state_id, "")

    def test_name(self):
        """
        Test that City instance has valid attribute value for name
        """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(type(new.name), str)
        if models.storage_target == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(new.name, "")

    def test_is_subclass(self):
        """
        Test that City is a subclass of BaseModel
        """
        new = self.value()
        self.assertIsInstance(new, BaseModel)
