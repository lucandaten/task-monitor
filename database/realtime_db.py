import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class RealTimeDB():

    def __init__(self, realtime_db_name, account_key_path = ''):
        account_key_filepath = f'{account_key_path}/{realtime_db_name}.json'
        cred = credentials.Certificate(account_key_filepath)
        url = f'https://{realtime_db_name}.firebaseio.com/'
        firebase_admin.initialize_app(cred, {'databaseURL': url})

    def get(self, node):
        ref = db.reference(node)
        return ref.get()