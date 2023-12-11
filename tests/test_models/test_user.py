#!/usr/bin/python3
import unittest
import models
import os
from models.base_model import BaseModel
from models.user import User

class Test_FileStorage(unittest.TestCase):
    """ testig FileStorage methods"""
    def setup(self):
        """creat temp file for saving data"""
        self.test_file = "test_file.json"
    def remover(self):
        """ remove temp file"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attribute(self):
        """ test creat user and attr"""
        test_user=User()
        self.assertEqual(test_user.password,"")
        self.assertEqual(test_user.email,"")
        self.assertEqual(test_user.first_name,"")
        self.assertEqual(test_user.last_name,"")
    
    def test_user_inherit_for_basemodel(self):
        """ test if user inherit from basemodel"""
        test_user=User()
        self.assertTrue(issubclass(User,BaseModel))
    def test_user_str_representation(self):
        """ test string repr"""
        test_user=User()
        test_user.email="mouh.bw@hotmail.com"
        test_user.first_name="momo"
        test_user.last_name="djouab"
        test_user.password="password1230"
        user_str=str(test_user)
        self.assertIn("User",user_str)
        self.assertIn("mouh.bw@hotmail.com",user_str)
        self.assertIn("momo",user_str)
        self.assertIn("djouab",user_str)


    def test_user_to_dict(self):
        """ test dict user"""
        test_user=User()
        test_user.email="mouh.bw@hotmail.com"
        test_user.first_name="momo"
        test_user.last_name="djouab"
        test_user.save()
        user_dict=test_user.to_dict()
        self.assertEqual(user_dict['email'],'mouh.bw@hotmail.com')
        self.assertEqual(user_dict['first_name'],'momo')
        self.assertEqual(user_dict['last_name'],'djouab')

    def test_user_instance_creat(self):
        """test creating user instance"""
        #test_user=User(email="mouh.bw@hotmail.com",password="password1230",first_name="momo",last_name="djouab")
        test_user=User()
        test_user.email="mouh.bw@hotmail.com"
        test_user.first_name="momo"
        test_user.last_name="djouab"
        test_user.password="password1230"
        user_dict=test_user.to_dict()
        self.assertEqual(user_dict['email'],"mouh.bw@hotmail.com")
        self.assertEqual(user_dict['password'],"password1230")
        self.assertEqual(user_dict['first_name'],"momo")
        self.assertEqual(user_dict['last_name'],"djouab")

    def test_user_instance_to_dict(self):
        """testing  insatnce to dict"""
        
        #test_user=User(email="mouh.bw@hotmail.com",password="password1230",first_name="momo",last_name="djouab")
        test_user=User()
        test_user.email="mouh.bw@hotmail.com"
        test_user.first_name="momo"
        test_user.last_name="djouab"
        test_user.password="password1230"
        user_dict=test_user.to_dict()
        self.assertEqual(user_dict['email'],'mouh.bw@hotmail.com')
        self.assertEqual(user_dict['first_name'],'momo')
        self.assertEqual(user_dict['last_name'],'djouab')

    def test_user_id_generate(self):
        test_user=User()
        user2=User()
        self.assertNotEqual(test_user.id,user2.id)

if __name__ == "__main__":
    unittest.main()


