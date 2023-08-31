import unittest
import gspread

creds = {'type': 'service_account', 'project_id': 'hidden', 'private_key_id': 'hidden', 'private_key': 'hidden', 'client_email': 'hidden', 'client_id': 'hidden', 'auth_uri': 'hidden', 'token_uri': 'hidden', 'auth_provider_x509_cert_url': 'hidden', 'client_x509_cert_url': 'hidden'}

class MyFuncTestCase(unittest.TestCase):

    def test_login_with_file(self):
        # Arrange
        account = gspread.service_account(filename='service-account.json')
        
        # Act
        result = myFunc()
        
        # Assert
        self.assertEqual(result, # expected result)

    def test_login_with_credentials(self):
        # Arrange
        account = gspread.service_account(credentials=creds)
        
        # Act
        result = myFunc()
        
        # Assert
        self.assertEqual(result, # expected result)

if __name__ == '__main__':
    unittest.main()