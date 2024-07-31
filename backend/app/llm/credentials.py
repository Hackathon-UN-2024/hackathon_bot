from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'configs/credentials.json'

def load_creds():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

    return credentials