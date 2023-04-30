#!/usr/bin/python3
"""
test_user module
"""
from tests.test_models.test_base_model import test_basemodel
from models import user
from models.base_model import BaseModel
import inspect
import models
import pycodestyle
import unittest
User = user.User


class test_user_docs(unittest.TestCase):
    """
    Tests to check the documentation and style of User class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_func = inspect.getmembers(User, inspect.isfunction)

    def test_user_func_docstrings(self):
        """
        Test for the presence of docstrings in User methods
        """
        for func in self.user_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_pycodestyle_conformance_user(self):
        """
        Test that models/user.py conforms to pycodestyle
        """
        pycodestyles = pycodestyle.StyleGuide(quiet=True)
        result = pycodestyles.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_conformance_test_user(self):
        """
        Test that tests/test_models/test_user.py conforms to pycodestyle
        """
        pycodestyles = pycodestyle.StyleGuide(quiet=True)
        result = pycodestyles.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """
        Test for the user.py module docstring
        """
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """
        Test for the User class docstring
        """
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")


class test_user(test_basemodel):
    """
    Test the User class
    """

    def __init__(self, *args, **kwargs):
        """Initializes User class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test that User has valid attribute value for first_name
        """
        new = self.value()
        self.assertTrue(hasattr(new, "first_name"))
        self.assertEqual(type(new.first_name), str)
        if models.storage_target == 'db':
            self.assertEqual(new.first_name, None)
        else:
            self.assertEqual(new.first_name, "")

    def test_last_name(self):
        """
        Test that User has valid attribute value for last_name
        """
        new = self.value()
        self.assertTrue(hasattr(new, "last_name"))
        self.assertEqual(type(new.last_name), str)
        if models.storage_target == 'db':
            self.assertEqual(new.last_name, None)
        else:
            self.assertEqual(new.last_name, "")

    def test_email(self):
        """
        Test that User has valid attribute value for email
        """
        new = self.value()
        self.assertTrue(hasattr(new, "email"))
        self.assertEqual(type(new.email), str)
        if models.storage_target == 'db':
            self.assertEqual(new.email, None)
        else:
            self.assertEqual(new.email, "")

    def test_password(self):
        """
        Test that User has valid attribute value for password
        """
        new = self.value()
        self.assertTrue(hasattr(new, "password"))
        self.assertEqual(type(new.password), str)
        if models.storage_target == 'db':
            self.assertEqual(new.password, None)
        else:
            self.assertEqual(new.password, "")

    def test_is_subclass(self):
        """
        Test that User is a subclass of BaseModel
        """
        new = self.value()
        self.assertIsInstance(new, BaseModel)
