#!/usr/bin/python3
"""
test_state module
"""
from tests.test_models.test_base_model import test_basemodel
from models import state
from models.base_model import BaseModel
import inspect
import models
import pycodestyle
import unittest
State = state.State


class test_state_docs(unittest.TestCase):
    """
    Tests to check the documentation and style of State class
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up for the doc tests
        """
        cls.state_func = inspect.getmembers(State, inspect.isfunction)

    def test_state_func_docstrings(self):
        """
        Test for the presence of docstrings in state methods
        """
        for func in self.state_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_pycodestyle_conformance_state(self):
        """
        Test that models/state.py conforms to pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_conformance_test_state(self):
        """
        Test that tests/test_models/test_state.py conforms to pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """
        Test for the state.py module docstring
        """
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_state_class_docstring(self):
        """
        Test for the State class docstring
        """
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")


class test_state(test_basemodel):
    """
    Tests the State class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the State class
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Test that User instance has valid attribute value for name
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
        Test that State is a subclass of BaseModel
        """
        new = self.value()
        self.assertIsInstance(new, BaseModel)
