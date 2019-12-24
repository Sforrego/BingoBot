from getstats import *
from constants import *
import time



def update_skills_player(sheet, names, name):
    if name not in names:
        print("Player not in memberslist.")
    else:
        index = names.index(name)
        cell_list = sheet.range(f'B{index+2}:AW{index+2}')
        stats = getStats(playerURL(name,'iron'))
        if stats != "404":
            player_dict, _ , _ = createDicts(parseStats(stats))
            player_skills = list(player_dict.values())
            print(f"updating {name} total {player_skills[0]}")
            for j,cell in enumerate(cell_list):
                cell.value = int(player_skills[j])
            sheet.update_cells(cell_list)
        else:
            print(f"{name} not found in hiscores.")

def bingo_skills_player(sheet, names, name, initial):
    bingo_skills = ["Slayer_Xp","Runecraft_Xp","Agility_Xp","Fishing_Xp",
    "Woodcutting_Xp","Mining_Xp","Thieving_Xp","Hunter_Xp"]
    if name not in names:
        print("Player not in memberslist.")
    else:
        index = names.index(name)
        cell_list = sheet.range(f'F{index+2}:AC{index+2}')
        cell_list = cell_list[1:len(cell_list):3] if not initial else cell_list[0:len(cell_list):3]
        stats = getStats(playerURL(name,'iron'))
        if stats != "404":
            player_dict, _ , _ = createDicts(parseStats(stats))
            player_skills = [player_dict[x] for x in player_dict.keys() if x in bingo_skills]
            print(f"updating {name} slayer {player_skills[0]}")

            for j in range(len(cell_list)):
                cell_list[j].value = int(player_skills[j])

            for cell in cell_list:
                if cell.value:
                    cell.value = int(cell.value)
            sheet.update_cells(cell_list)
        else:
            print(f"{name} not found in hiscores.")

def bingo_skills(sheet,initial=1):
    row = 1
    names = sheet.col_values(1)[1:]
    for _,name in enumerate(names[row-1:],start=row):
        if "team" in name:
            pass
        else:
            bingo_skills_player(sheet,names,name,initial)


def update_bosses_player(sheet, names, name): #index == row number
    if name not in names:
        print("Player not in memberslist.")
    else:
        index = names.index(name)+2
        cell_list = sheet.range(f'B{index}:AW{index}')
        stats = getStats(playerURL(name,'iron'))
        if stats == "404":
            print(f"{name} not found in hiscores.")
        else:
            player_skills, player_clues , player_bosses = createDicts(parseStats(stats))
            print(f"Updating {name}.")
            player_stats = [player_skills["Overall"]]+list(player_clues.values())+list(player_bosses.values())
            for j,cell in enumerate(cell_list):
                cell.value = int(player_stats[j])
            sheet.update_cells(cell_list)


def update_skills(sheet):
    row = 0
    names = sheet.col_values(1)[1:]
    for _,name in enumerate(names[row-1:],start=row):
        update_skills_player(sheet,names,name)

def update_bosses(sheet):
    names = sheet.col_values(1)[1:]
    starting_cell = 246
    for index,name in enumerate(names[starting_cell-2:], start=starting_cell):
        update_player(sheet, name, index)

def update_bosses(BOSSES, sheet):
    # updates the columns names
    for i, boss in enumerate(BOSSES):
        sheet.update_cell(1, 10+i, boss)


if __name__ == "__main__":
    pass
    #updateAll(["CH Product"],"b")
    #sheet.update_cell(1, 10+i, boss))
