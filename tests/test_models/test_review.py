"""test_review module"""
from tests.test_models.test_base_model import test_basemodel
from models import review
from models.base_model import BaseModel
import inspect
import models
import pycodestyle
import unittest
Review = review.Review


class test_review_docs(unittest.TestCase):
    """Tests to check the documentation and style of Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_func = inspect.getmembers(Review, inspect.isfunction)

    def test_review_func_docstrings(self):
        """Test for the presence of docstrings in review methods"""
        for func in self.review_func:
            self.assertIsNot(func[1].__doc__,
                             None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_pycodestyle_conformance_review(self):
        """Test that models/review.py conforms to pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_conformance_test_review(self):
        """
        Test that tests/test_models/test_review.py conforms to pycodestyle.
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Test for the review.py module docstring"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")


class test_review(test_basemodel):
    """Tests the Review class"""

    def __init__(self, *args, **kwargs):
        """Initializes the Review class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test that Review instance has valid attribute value for place_id"""
        new = self.value()
        self.assertTrue(hasattr(new, "place_id"))
        self.assertEqual(type(new.place_id), str)
        if models.storage_target == 'db':
            self.assertEqual(new.place_id, None)
        else:
            self.assertEqual(new.place_id, "")

    def test_user_id(self):
        """Test that Review instance has valid attribute value for user_id"""
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(type(new.user_id), str)
        if models.storage_target == 'db':
            self.assertEqual(new.user_id, None)
        else:
            self.assertEqual(new.user_id, "")

    def test_text(self):
        """Test that Review instance has valid attribute value for text"""
        new = self.value()
        self.assertTrue(hasattr(new, "text"))
        self.assertEqual(type(new.text), str)
        if models.storage_target == 'db':
            self.assertEqual(new.text, None)
        else:
            self.assertEqual(new.text, "")

    def test_is_subclass(self):
        """Test that Review is a subclass of BaseModel"""
        new = self.value()
        self.assertIsInstance(new, BaseModel)
