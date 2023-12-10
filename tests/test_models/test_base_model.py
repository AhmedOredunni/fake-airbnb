#!/usr/bin/python3


import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_attributes_creation(self):
        """
        Test if the attributes are created when creating an instance
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_save_method(self):
        """ Test if the save method updates the updated_at attribute"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        current_updated_at = model.save()
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns a dictionary with the expected keys"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict,dict)

        self.assertTrue('__class__' in model_dict)
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)

    def test_string_representation(self):
        """Test if the __str__ method returns the expected string"""
        model = BaseModel()
        str_representation = str(model)

        self.assertIn(model.__class__.__name__, str_representation)
        self.assertIn(model.id, str_representation)
        self.assertIn(str(model.__dict__), str_representation)

    def test_attributes_initialization_from_dict(self):
        """Test if the attributes are correctly initialized when creating an instance from a dictionary"""
        original_model = BaseModel()
        model_dict = original_model.to_dict()

        new_model = BaseModel(**model_dict)

        self.assertEqual(original_model.id, new_model.id)
        self.assertEqual(original_model.created_at, new_model.created_at)
        self.assertEqual(original_model.updated_at, new_model.updated_at)

if __name__ == '__main__':
    unittest.main()


