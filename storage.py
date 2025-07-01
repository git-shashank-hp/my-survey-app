import streamlit as st
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Google API scopes
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Load credentials from Streamlit secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDS"])

# Authenticate
credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, SCOPE)
gc = gspread.authorize(credentials)

# Your Google Sheet ID
SHEET_ID = "1ir2j7_h-zDIXwmINtwgIt1T9nDcInFvPy60Remk82NA"

sheet = gc.open_by_key(SHEET_ID).sheet1

def save_response(data: dict):
    """
    Save response along with current timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [
        data.get("name", ""),
        data.get("answer", ""),
        timestamp
    ]
    sheet.append_row(row)
