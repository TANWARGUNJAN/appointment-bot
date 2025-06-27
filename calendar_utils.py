from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# Scope defines what the app can access in your Google account
SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_PATH = 'credentials/token.json'
CREDENTIALS_PATH = 'credentials/credentials.json'

def get_calendar_service():
    creds = None
    # Load token if it exists
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    else:
        # If not authorized yet, open browser to log in
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

# Simulated free time function (we’ll replace this later)
def get_free_slots():
    return "You are free between 2 PM and 4 PM tomorrow."

def book_slot():
    return "Meeting booked successfully at 3 PM tomorrow!"
