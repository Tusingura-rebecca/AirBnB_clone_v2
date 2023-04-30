"""test_place module"""
from tests.test_models.test_base_model import test_basemodel
from models import place
from models.base_model import BaseModel
import inspect
import models
import pycodestyle
import unittest
Place = place.Place


class test_place_docs(unittest.TestCase):
    """
    Tests to check the documentation and style of Place class
    """
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_func = inspect.getmembers(Place, inspect.isfunction)

    def test_place_func_docstrings(self):
        """
        Test for the presence of docstrings in place methods
        """
        for func in self.place_func:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_pycodestyle_conformance_place(self):
        """
        Test that models/place.py conforms to pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_conformance_test_place(self):
        """
        Test that tests/test_models/test_place.py conforms to pycodestyle
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        """
        Test for the place.py module docstring
        """
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        """
        Test for the Place class docstring
        """
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")


class test_Place(test_basemodel):
    """Tests the Place class"""

    def __init__(self, *args, **kwargs):
        """
        Initializes Place instance
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Initializes the Place class
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)
        self.assertTrue(hasattr(new, "city_id"))
        if models.storage_target == 'db':
            self.assertEqual(new.city_id, None)
        else:
            self.assertEqual(new.city_id, "")

    def test_user_id(self):
        """
        Test that Place instance has valid attribute value for user_id
        """
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(type(new.user_id), str)
        if models.storage_target == 'db':
            self.assertEqual(new.user_id, None)
        else:
            self.assertEqual(new.user_id, "")

    def test_name(self):
        """
        Test that Place instance has valid attribute value for name
        """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(type(new.name), str)
        if models.storage_target == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(new.name, "")

    def test_description(self):
        """
        Test that Place instance has valid attribute value for description
        """
        new = self.value()
        self.assertTrue(hasattr(new, "description"))
        self.assertEqual(type(new.description), str)
        if models.storage_target == 'db':
            self.assertEqual(new.description, None)
        else:
            self.assertEqual(new.description, "")

    def test_number_rooms(self):
        """
        Test that Place instance has valid attribute value for number_rooms
        """
        new = self.value()
        self.assertTrue(hasattr(new, "number_rooms"))
        if models.storage_target == 'db':
            self.assertEqual(new.number_rooms, 0)
        else:
            self.assertEqual(type(new.number_rooms), int)
            self.assertEqual(new.number_rooms, 0)

    def test_number_bathrooms(self):
        """
        Test that Place instance has valid attribute value for number_bathrooms
        """
        new = self.value()
        self.assertTrue(hasattr(new, "number_bathrooms"))
        if models.storage_target == 'db':
            self.assertEqual(new.number_bathrooms, 0)
        else:
            self.assertEqual(type(new.number_bathrooms), int)
            self.assertEqual(new.number_bathrooms, 0)

    def test_max_guest(self):
        """
        Test that Place instance has valid attribute value for max_guest
        """
        new = self.value()
        self.assertTrue(hasattr(new, "max_guest"))
        if models.storage_target == 'db':
            self.assertEqual(new.max_guest, 0)
        else:
            self.assertEqual(type(new.max_guest), int)
            self.assertEqual(new.max_guest, 0)

    def test_price_by_night(self):
        """
        Test that Place instance has valid attribute value for price_by_night
        """
        new = self.value()
        self.assertTrue(hasattr(new, "price_by_night"))
        if models.storage_target == 'db':
            self.assertEqual(new.price_by_night, 0)
        else:
            self.assertEqual(type(new.price_by_night), int)
            self.assertEqual(new.price_by_night, 0)

    def test_latitude(self):
        """
        Test that Place instance has valid attribute value for latitude
        """
        new = self.value()
        self.assertTrue(hasattr(new, "latitude"))
        if models.storage_target == 'db':
            self.assertEqual(new.latitude, None)
        else:
            self.assertEqual(type(new.latitude), float)
            self.assertEqual(new.latitude, 0.0)

    def test_longitude(self):
        """
        Test that Place instance has valid attribute value for longitude
        """
        new = self.value()
        self.assertTrue(hasattr(new, "longitude"))
        if models.storage_target == 'db':
            self.assertEqual(new.longitude, None)
        else:
            self.assertEqual(type(new.longitude), float)
            self.assertEqual(new.longitude, 0.0)

    @unittest.skipIf(models.storage_target == 'db', "not testing File Storage")
    def test_amenity_ids(self):
        """
        Test that Place instance has valid attribute value for amenity_ids
        """
        new = self.value()
        self.assertTrue(hasattr(new, "amenity_ids"))
        self.assertEqual(type(new.amenity_ids), list)
        self.assertEqual(len(new.amenity_ids), 0)

    def test_is_subclass(self):
        """
        Test that Place is a subclass of BaseModel
        """
        new = self.value()
        self.assertIsInstance(new, BaseModel)
