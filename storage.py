import streamlit as st
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define Google API scopes
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Load credentials JSON from Streamlit secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDS"])

# Authenticate with Google API
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, SCOPE)
gc = gspread.authorize(credentials)

# Your Google Sheet ID
SHEET_ID = "1ir2j7_h-zDIXwmINtwgIt1T9nDcInFvPy60Remk82NA"

# Open your sheet
sheet = gc.open_by_key(SHEET_ID).sheet1  # Using the first worksheet

def save_response(data: dict):
    """
    Append a response dictionary as a new row in the sheet.
    """
    # Customize this list based on your sheet's columns
    columns = ["name", "answer"]  # Adjust as needed

    # Prepare data in order of columns
    row = [data.get(col, "") for col in columns]

    sheet.append_row(row)
