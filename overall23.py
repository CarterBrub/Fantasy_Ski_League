import requests
from bs4 import BeautifulSoup
import database as db
import pandas as pd

# --------------- MEN XC OVERALL POINTS 2023 -----------------------------------------
url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=CC&seasoncode=2023&cupcode=WC&disciplinecode=ALL&gendercode=M&nationcode=&pict_info=0")
htmltext = url.text

male_XC_athletes_2023 = []
male_XC_points_2023 = []
male_XC_nationality_2023 = []


soup = BeautifulSoup(htmltext, "html.parser")
overall_score = soup.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name = soup.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country = soup.find_all("span", {"class": "country__name-short"})


for hit in athlete_name:
    male_XC_athletes_2023.append(hit.text.strip())

for hit in overall_score:
    male_XC_points_2023.append(hit.text.strip())

for hit in athlete_country:
    male_XC_nationality_2023.append(hit.text)

Men_XC_Season_2023 = {male_XC_athletes_2023[i]: male_XC_points_2023[i] for i in range(len(male_XC_athletes_2023))}



# ------------------------- WORLD CUP SEASON 2023 CROSS COUNTRY WOMEN -----------------------------

url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=CC&seasoncode=2023&cupcode=WC&disciplinecode=ALL&gendercode=W&nationcode=&pict_info=0")
htmltext = url.text

female_XC_athletes_2023 = []
female_XC_points_2023 = []
female_XC_nationality_2023 = []


soup2 = BeautifulSoup(htmltext, "html.parser")
overall_score2 = soup2.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name2 = soup2.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country2 = soup2.find_all("span", {"class": "country__name-short"})


for hit in athlete_name2:
    female_XC_athletes_2023.append(hit.text.strip())

for hit in overall_score2:
    female_XC_points_2023.append(hit.text.strip())

for hit in athlete_country2:
    female_XC_nationality_2023.append(hit.text)

Women_XC_Season_2023 = {female_XC_athletes_2023[i]: female_XC_points_2023[i] for i in range(len(female_XC_athletes_2023))}


# -------------------------- WORLD CUP SEASON 2023 SKI JUMPING MEN -----------------------------------

url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=JP&seasoncode=2023&cupcode=WC&disciplinecode=ALL&gendercode=M&nationcode=&pict_info=0")
htmltext = url.text

Male_Jump_athletes_2023 = []
Male_Jump_points_2023 = []
Male_Jump_nationality_2023 = []


soup3 = BeautifulSoup(htmltext, "html.parser")
overall_score3 = soup3.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name3 = soup3.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country3 = soup3.find_all("span", {"class": "country__name-short"})


for hit in athlete_name3:
    Male_Jump_athletes_2023.append(hit.text.strip())

for hit in overall_score3:
    Male_Jump_points_2023.append(hit.text.strip())

for hit in athlete_country3:
    Male_Jump_nationality_2023.append(hit.text)

Men_Jump_Season_2023 = {Male_Jump_athletes_2023[i]: Male_Jump_points_2023[i] for i in range(len(Male_Jump_athletes_2023))}



# -------------------------- WORLD CUP SEASON 2022 SKI JUMPING WOMEN -----------------------------------
url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=JP&seasoncode=2023&cupcode=WC&disciplinecode=ALL&gendercode=W&nationcode=&pict_info=0")
htmltext = url.text

Female_Jump_athletes_2023 = []
Female_Jump_points_2023 = []
Female_Jump_nationality_2023 = []


soup4 = BeautifulSoup(htmltext, "html.parser")
overall_score4 = soup4.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name4 = soup4.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country4 = soup4.find_all("span", {"class": "country__name-short"})


for hit in athlete_name4:
    Female_Jump_athletes_2023.append(hit.text.strip())

for hit in overall_score4:
    Female_Jump_points_2023.append(hit.text.strip())

for hit in athlete_country4:
    Female_Jump_nationality_2023.append(hit.text)

Women_Jump_Season_2023 = {Female_Jump_athletes_2023[i]: Female_Jump_points_2023[i] for i in range(len(Female_Jump_athletes_2023))}



# -------------------------- WORLD CUP SEASON 2023 NORDIC COMBINED MEN -----------------------------------
url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=NK&seasoncode=2023&cupcode=WC&disciplinecode=ALL&gendercode=M&nationcode=&pict_info=0")
htmltext = url.text

Male_NoCo_athletes_2023 = []
Male_NoCo_points_2023 = []
Male_NoCo_nationality_2023 = []


soup5 = BeautifulSoup(htmltext, "html.parser")
overall_score5 = soup5.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name5 = soup5.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country5 = soup5.find_all("span", {"class": "country__name-short"})


for hit in athlete_name5:
    Male_NoCo_athletes_2023.append(hit.text.strip())

for hit in overall_score5:
    Male_NoCo_points_2023.append(hit.text.strip())

for hit in athlete_country5:
    Male_NoCo_nationality_2023.append(hit.text)

Men_NoCo_Season_2023 = {Male_NoCo_athletes_2023[i]: Male_NoCo_points_2023[i] for i in range(len(Male_NoCo_athletes_2023))}


print(Men_XC_Season_2023)
print(Women_XC_Season_2023)
print(Men_Jump_Season_2023)
print(Men_NoCo_Season_2023)
print(Women_Jump_Season_2023)
# ------------- RUKA---------------------------------
df = pd.DataFrame(db.fetch_all_periods())

Torje = df.loc[df['User']=="Torje Seljeset"]
print(Torje)

for column in Torje:
   print(column)


for row in Torje:
    for cell in row:
        if 'Ruka' in cell:
            print("Nice")
        else:
            print('BYT')
for cell in Torje['Weekend']:
    if cell == 'Ruka':
        print(cell)



Torje = df.loc[df['User'] == "Torje Seljeset"]
t= []
for item in Torje["Team"]:
    t.append(item)
if df['User'] == "Torje Seljeset" and df['Weekend'] == "Ruka":
    print(df['Team'])
else:
    print("Failed")



print(t)
jump_team_ruka_torje = []
for item in t[0]:
    jump_team_ruka_torje.append(item)
print(jump_team_ruka_torje[0])


test = []
for list in t:
    for item in list:
        if item in Men_Jump_Season_2023:
            test.append(int(Men_Jump_Season_2023[item]))
            print(Men_Jump_Season_2023[item])
        elif item in Men_NoCo_Season_2023:
            test.append(int(Men_NoCo_Season_2023[item]))
            print(Men_NoCo_Season_2023[item])
        elif item in Men_XC_Season_2023:
            test.append(int(Men_XC_Season_2023[item]))
            print(Men_XC_Season_2023[item])
        elif item in Women_Jump_Season_2023:
            test.append(int(Women_Jump_Season_2023[item]))
            print(Women_Jump_Season_2023[item])
        elif item in Women_XC_Season_2023:
            test.append(int(Women_XC_Season_2023[item]))
            print(Women_XC_Season_2023[item])
        else:
            print("None")
total_points_ruka = []
for i in jump_team_ruka_torje:
    if i in Men_Jump_Season_2023:
        total_points_ruka.append(int(Men_Jump_Season_2023[i]))
        print(Men_Jump_Season_2023[i])
    else:
        print("none")
print(sum(total_points_ruka))

# make this one big loop. Like users = list of users, for user in users:

