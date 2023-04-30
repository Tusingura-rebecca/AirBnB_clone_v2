"""test_amenity module"""
from tests.test_models.test_base_model import test_basemodel
from models import amenity
from models.base_model import BaseModel
import inspect
import models
import pycodestyle
import unittest
Amenity = amenity.Amenity


class test_amenity_docs(unittest.TestCase):
    """
    Tests to check the documentation and style of Amenity class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_func = inspect.getmembers(Amenity, inspect.isfunction)

    def test_amenity_func_docstrings(self):
        """
        Test for the presence of docstrings in amenity methods
        """
        for func in self.amenity_func:
            self.assertIsNot(func[1]
                             .__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_pycodestyle_conformance_amenity(self):
        """
        Test that models/amenity.py conforms to pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_conformance_test_amenity(self):
        """
        Test that tests/test_models/test_amenity.py conforms to pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """
        Test for the amenity.py module docstring
        """
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """
        Test for the Amenity class docstring
        """
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")


class test_Amenity(test_basemodel):
    """Tests the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes the Amenity class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test that Amenity instance has valid attribute value for name"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(type(new.name), str)
        if models.storage_target == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(new.name, "")

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        new = self.value()
        self.assertIsInstance(new, BaseModel)
