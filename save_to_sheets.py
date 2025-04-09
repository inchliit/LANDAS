import gspread
from google.oauth2.service_account import Credentials

def save_to_gsheet(data_row, sheet_name="Responses", worksheet_name="Predictions"):
    # Load credentials
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    )

    # Connect to Google Sheet
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)
    worksheet = sheet.worksheet(worksheet_name)

    # Append row
    worksheet.append_row(data_row, value_input_option="USER_ENTERED")
