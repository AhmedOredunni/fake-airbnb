#!/usr/bin/python3
import unittest
import models
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class Test_FileStorage_init(unittest.TestCase):
    """ Testing the init of FileStorge"""
    def test_FileStorage_instantiation_no_args(self):
        """ test creating  FileStorage instance with no argument"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """ test creating  FileStorage instance with argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

   

    def test_storage_initializes(self):
        """ test if storage is instance of FileStorge"""
        self.assertEqual(type(models.storage), FileStorage)

class Test_FileStorage(unittest.TestCase):
    """ testig FileStorage methods"""
    def setup(self):
        """creat temp file for saving data"""
        self.test_file = "test_file.json"
    def remover(self):
        """ remove temp file"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage(self):
        """ test all() method retur dict"""
        self.assertEqual(dict,type(models.storage.all()))
    def test_new(self):
        """ test new() method  for creat and store new object"""
        obj=BaseModel()
        self.assertIn("BaseModel." + obj.id, models.storage.all())
    def test_new_with_args(self):
        """test creati object with additionl argument"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
    def test_new_with_no_args(self):
        """test creating object with no argument"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_reload(self):
        """testig save obeject to file and reload it """
        obj1=BaseModel()
        obj2=BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()
        new_storge=FileStorage()
        new_storge.reload()
        self.assertTrue(new_storge.all().get("BaseModel." + obj1.id) is not None)        
        self.assertTrue(new_storge.all().get("BaseModel." + obj2.id) is not None)        
    

    def test_save_toFile(self):
        """test saving object to file"""
        obj=BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))
    def test_reload_emptyFile(self):
        """ testing reload a file dont exist"""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

if __name__=="__main__":
    unittest.main()
        
