import gspread
from oauth2client.service_account import ServiceAccountCredentials
from constants import *
from newfuncs import *





if __name__ == "__main__":
    scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("07 Irons HiScore").get_worksheet(2)
    names = sheet.col_values(1)[1:]
    bingo_skills(sheet,0)
    #bingo_skills_player(sheet, names, "IronRok", 0)
#  updates one player in the spreadsheet

# update_skills(sheet) updates the whole spreadsheet

# worksheet.update_cells(cell_list) batch update

# update_player(sheet,"ironrok")


### sheet examples
#list_of_hashes = sheet.get_all_records()
