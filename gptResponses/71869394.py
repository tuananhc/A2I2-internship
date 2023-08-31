# To login to a service account using a dictionary of credentials instead of a file, you can use the `gspread.service_account_from_dict` method. Here's an example of how you can modify your code:

# ```python
import gspread

creds = {
    'type': 'service_account',
    'project_id': 'hidden',
    'private_key_id': 'hidden',
    'private_key': 'hidden',
    'client_email': 'hidden',
    'client_id': 'hidden',
    'auth_uri': 'hidden',
    'token_uri': 'hidden',
    'auth_provider_x509_cert_url': 'hidden',
    'client_x509_cert_url': 'hidden'
}

# Login to service account using the credentials dictionary
account = gspread.service_account_from_dict(creds)
# ```

# This way, you can provide the service account credentials directly in the `creds` dictionary.