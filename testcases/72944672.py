import unittest
import os
import shutil


def myFunc(exepath):
    directory = os.path.dirname(os.path.abspath(exepath)) + "\\Files\\"
    credit_folder = os.path.dirname(os.path.abspath(exepath)) + "\\Credits\\"
    os.chdir(credit_folder)
    os.chdir(directory)
    Source = credit_folder
    Target = directory
    files = os.listdir(Source)
    folders = os.listdir(Target)
    for file in files:
        SourceCredits = os.path.join(Source, file)
        for folder in folders:
            TargetFolder = os.path.join(Target, folder)
            shutil.copy2(SourceCredits, TargetFolder)
    return "Credits Copy & Paste Successfully"
    
class MyFuncTestCase(unittest.TestCase):
    def setUp(self):
        os.mkdir("301")
        os.mkdir("302")
        os.mkdir("303")
        open("Credits/image1.jpg", 'a').close()
        open("Credits/image2.jpg", 'a').close()
        open("Credits/image3.jpg", 'a').close()
    
    def tearDown(self):
        shutil.rmtree("301")
        shutil.rmtree("302")
        shutil.rmtree("303")
    
    def test_myFunc(self):
        result = myFunc(__file__)
        self.assertEqual(result, "Credits Copy & Paste Successfully")
        
        self.assertTrue(os.path.exists("301/image1.jpg"))
        self.assertTrue(os.path.exists("301/image2.jpg"))
        self.assertTrue(os.path.exists("301/image3.jpg"))
        
        self.assertTrue(os.path.exists("302/image1.jpg"))
        self.assertTrue(os.path.exists("302/image2.jpg"))
        self.assertTrue(os.path.exists("302/image3.jpg"))
        
        self.assertTrue(os.path.exists("303/image1.jpg"))
        self.assertTrue(os.path.exists("303/image2.jpg"))
        self.assertTrue(os.path.exists("303/image3.jpg"))
        
        self.assertFalse(os.path.exists("301/A"))
        self.assertFalse(os.path.exists("301/B"))
        
        self.assertFalse(os.path.exists("302/A"))
        self.assertFalse(os.path.exists("302/B"))
        
        self.assertFalse(os.path.exists("303/A"))
        self.assertFalse(os.path.exists("303/B"))

unittest.main()