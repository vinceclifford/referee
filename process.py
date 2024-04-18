import csv 
from datetime import datetime, timedelta

PATH = "./list.csv" 
CLUB = "TSV Vaterstetten" 
DAYS_IN_ADVANCE = 10 
CURENT_DATE = datetime.today()
CUT_OFF_DATE = CURENT_DATE + timedelta(days=DAYS_IN_ADVANCE)

solution = ""
 
with open(PATH, 'r') as file: 
    csv_dict_reader = csv.DictReader(file)

    for row in csv_dict_reader: 
        game_time = datetime.strptime(row['Datum+Zeit'], "%Y-%m-%dT%H:%M")
        amount_SR = "" 
    
        if row['SR-Verein'] != CLUB or game_time > CUT_OFF_DATE or game_time < CURENT_DATE: 
            continue 
        
        if row['1. Schiedsrichter '] != "" and row['2.Schiedsrichter'] != "": 
            continue 
        
        if row['1. Schiedsrichter '] == '' and row['2.Schiedsrichter'] == '': 
            amount_SR = "1. & 2. SR"
        elif row['1. Schiedsrichter '] == '': 
            amount_SR = "1. SR"
        else: 
            amount_SR = "2. SR"
        
    
        formatted_game_time = game_time.strftime("%d.%m.%Y %H:%M")
        solution =  solution + f'''
        {formatted_game_time}  
        {row['Heimverein']} vs. {row['Gastverein']}     {row['72']}  
        {row['Halle ']} | {amount_SR}  
        '''
        
        solution = '\n'.join(line.strip() for line in solution.splitlines())

        
solution = f"""Hallo zusammen, 
ich suche auch noch Schiedsrichter für das kommende Wochenende. Ich würde mich über jeglich Hilfe freuen. 

{solution}

Vielen Dank! 
"""

print(solution)
        

        