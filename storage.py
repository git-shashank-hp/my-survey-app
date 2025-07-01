import streamlit as st
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define Google API scopes
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Load credentials from Streamlit secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDS"])

# Authenticate with Google Sheets
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, SCOPE)
gc = gspread.authorize(credentials)

# Your Google Sheet ID here
SHEET_ID = "1ir2j7_h-zDIXwmINtwgIt1T9nDcInFvPy60Remk82NA"

# Open the Google Sheet (first worksheet)
sheet = gc.open_by_key(SHEET_ID).sheet1

def save_response(data: dict):
    """
    Save the user response to the Google Sheet.
    """
    columns = ["name", "answer"]
    row = [data.get(col, "") for col in columns]
    sheet.append_row(row)
