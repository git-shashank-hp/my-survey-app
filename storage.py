import gspread
from datetime import datetime

# Load credentials
gc = gspread.service_account(filename='creds.json')

# Open the sheet
sh = gc.open('SurveyData')  # Name of your Google Sheet
worksheet = sh.worksheet('Responses')  # Tab name

def save_response(name, response):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    worksheet.append_row([name, response, timestamp])
