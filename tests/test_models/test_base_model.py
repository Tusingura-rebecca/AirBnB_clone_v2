#!/usr/bin/python3
"""
test_base_model module
"""
from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel instance"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ Is new instance of type BaseModel """
        inst = self.value()
        self.assertEqual(type(inst), self.value)

    def test_kwargs(self):
        """ Two instances of BaseModel are asymmetric"""
        inst = self.value()
        copy = inst.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is inst)

    def test_kwargs_int(self):
        """ Test addition of uninstantiated attribute """
        inst = self.value()
        copy = inst.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        inst = self.value()
        inst.save()
        key = self.name + "." + inst.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], inst.to_dict())

    def test_str(self):
        """ Test valid str representation """
        inst = self.value()
        self.assertEqual(str(inst), '[{}] ({}) {}'.format(self.name, inst.id,
                         inst.__dict__))

    def test_todict(self):
        """ """
        inst = self.value()
        n = inst.to_dict()
        self.assertEqual(inst.to_dict(), n)

    def test_kwargs_none(self):
        """ Test for zero kwargs """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ Test for only one of two kwargs """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """
        Test that BaseModel instance has valid id attribute
        """
        new = self.value()
        self.assertIs(type(new.id), str)

    def test_created_at(self):
        """
        Test that BaseModel instance has valid creared_at attribute
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test that BaseModel instance has valid updated_at attribute
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == "__main__":
    unittest.main()
