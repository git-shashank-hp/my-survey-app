import json
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Define the scopes required to access Google Sheets and Drive
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Load service account credentials from Streamlit secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDS"])

# Authenticate with Google Sheets
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gc = gspread.authorize(credentials)

# Open the target Google Sheet and worksheet
spreadsheet = gc.open("SurveyData")  # Make sure the name matches your actual Google Sheet
worksheet = spreadsheet.worksheet("Responses")  # Tab name in the sheet

# Function to append a new response
def save_response(name, response):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    worksheet.append_row([name, response, timestamp])
