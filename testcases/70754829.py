import unittest
class MyTestCase(unittest.TestCase):
    def test_upload_with_email(self):
        test_files = {('dicom', open("Pre_1", "rb")),
                      ('dicom', open("Pre_2", "rb")),
                      ('dicom', open("Post_1", "rb")),
                      ('dicom', open("Post_2", "rb"))}
        response = requests.post("MyWebsite.com", files=test_files, data={"email": "RecipientEmail@gmail.com"})
        # Add assertions here to validate the response
        
    def test_upload_without_email(self):
        test_files = {('dicom', open("Pre_1", "rb")),
                      ('dicom', open("Pre_2", "rb")),
                      ('dicom', open("Post_1", "rb")),
                      ('dicom', open("Post_2", "rb"))}
        response = requests.post("MyWebsite.com", files=test_files)
        # Add assertions here to validate the response

if __name__ == '__main__':
    unittest.main()