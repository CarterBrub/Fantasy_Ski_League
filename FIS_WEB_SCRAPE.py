
import requests
from bs4 import BeautifulSoup

# -------------WORLD CUP SEASON 2022 CROSS COUNTRY MEN------------------------
url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=CC&seasoncode=2022&cupcode=WC&disciplinecode=ALL&gendercode=M&nationcode=&pict_info=0")
htmltext = url.text

male_XC_athletes = []
male_XC_points_2022 = []
male_XC_nationality = []


soup = BeautifulSoup(htmltext, "html.parser")
overall_score = soup.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name = soup.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country = soup.find_all("span", {"class": "country__name-short"})


for hit in athlete_name:
    male_XC_athletes.append(hit.text.strip())

for hit in overall_score:
    male_XC_points_2022.append(hit.text.strip())

for hit in athlete_country:
    male_XC_nationality.append(hit.text)

Men_XC_Season_2022 = {male_XC_athletes[i]: male_XC_points_2022[i] for i in range(len(male_XC_athletes))}



# ------------------------- WORLD CUP SEASON 2022 CROSS COUNTRY WOMEN -----------------------------

url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=CC&seasoncode=2022&cupcode=WC&disciplinecode=ALL&gendercode=W&nationcode=&pict_info=0")
htmltext = url.text

female_XC_athletes = []
female_XC_points_2022 = []
female_XC_nationality = []


soup2 = BeautifulSoup(htmltext, "html.parser")
overall_score2 = soup2.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name2 = soup2.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country2 = soup2.find_all("span", {"class": "country__name-short"})


for hit in athlete_name2:
    female_XC_athletes.append(hit.text.strip())

for hit in overall_score2:
    female_XC_points_2022.append(hit.text.strip())

for hit in athlete_country2:
    female_XC_nationality.append(hit.text)

Women_XC_Season_2022 = {female_XC_athletes[i]: female_XC_points_2022[i] for i in range(len(female_XC_athletes))}


# -------------------------- WORLD CUP SEASON 2022 SKI JUMPING MEN -----------------------------------

url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=JP&seasoncode=2022&cupcode=WC&disciplinecode=ALL&gendercode=M&nationcode=&pict_info=0")
htmltext = url.text

Male_Jump_athletes = []
Male_Jump_points_2022 = []
Male_Jump_nationality = []


soup3 = BeautifulSoup(htmltext, "html.parser")
overall_score3 = soup3.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name3 = soup3.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country3 = soup3.find_all("span", {"class": "country__name-short"})


for hit in athlete_name3:
    Male_Jump_athletes.append(hit.text.strip())

for hit in overall_score3:
    Male_Jump_points_2022.append(hit.text.strip())

for hit in athlete_country3:
    Male_Jump_nationality.append(hit.text)

Male_Jump_Season_2022 = {Male_Jump_athletes[i]: Male_Jump_points_2022[i] for i in range(len(Male_Jump_athletes))}



# -------------------------- WORLD CUP SEASON 2022 SKI JUMPING WOMEN -----------------------------------
url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=JP&seasoncode=2022&cupcode=WC&disciplinecode=ALL&gendercode=W&nationcode=&pict_info=0")
htmltext = url.text

Female_Jump_athletes = []
Female_Jump_points_2022 = []
Female_Jump_nationality = []


soup4 = BeautifulSoup(htmltext, "html.parser")
overall_score4 = soup4.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name4 = soup4.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country4 = soup4.find_all("span", {"class": "country__name-short"})


for hit in athlete_name4:
    Female_Jump_athletes.append(hit.text.strip())

for hit in overall_score4:
    Female_Jump_points_2022.append(hit.text.strip())

for hit in athlete_country4:
    Female_Jump_nationality.append(hit.text)

Female_Jump_Season_2022 = {Female_Jump_athletes[i]: Female_Jump_points_2022[i] for i in range(len(Female_Jump_athletes))}



# -------------------------- WORLD CUP SEASON 2022 NORDIC COMBINED MEN -----------------------------------
url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=NK&seasoncode=2022&cupcode=WC&disciplinecode=ALL&gendercode=M&nationcode=&pict_info=0")
htmltext = url.text

Male_NoCo_athletes = []
Male_NoCo_points_2022 = []
Male_NoCo_nationality = []


soup5 = BeautifulSoup(htmltext, "html.parser")
overall_score5 = soup5.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name5 = soup5.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country5 = soup5.find_all("span", {"class": "country__name-short"})


for hit in athlete_name5:
    Male_NoCo_athletes.append(hit.text.strip())

for hit in overall_score5:
    Male_NoCo_points_2022.append(hit.text.strip())

for hit in athlete_country5:
    Male_NoCo_nationality.append(hit.text)

Male_NoCo_Season_2022 = {Male_NoCo_athletes[i]: Male_NoCo_points_2022[i] for i in range(len(Male_NoCo_athletes))}


# -------------------------- WORLD CUP SEASON 2022 NORDIC COMBINED WOMEN -----------------------------------
url = requests.get("https://data.fis-ski.com/fis_events/ajax/cupstandingsfunctions/load_cupstandings.html?sectorcode=NK&seasoncode=2022&cupcode=WC&disciplinecode=ALL&gendercode=W&nationcode=&pict_info=0")
htmltext = url.text

Female_NoCo_athletes = []
Female_NoCo_points_2022 = []
Female_NoCo_nationality = []


soup6 = BeautifulSoup(htmltext, "html.parser")
overall_score6 = soup6.find_all("div", {"class": "pl-xs-1 pl-sm-1 g-xs-10 g-sm-7 g-md-9 g-lg-8 justify-right bold"})
athlete_name6 = soup6.find_all("div", {"class": "g-xs-10 g-sm-9 g-md-4 g-lg-4 justify-left bold align-xs-top"})
athlete_country6 = soup6.find_all("span", {"class": "country__name-short"})


for hit in athlete_name6:
    Female_NoCo_athletes.append(hit.text.strip())

for hit in overall_score6:
    Female_NoCo_points_2022.append(hit.text.strip())

for hit in athlete_country6:
    Female_NoCo_nationality.append(hit.text)

Female_NoCo_Season_2022 = {Female_NoCo_athletes[i]: Female_NoCo_points_2022[i] for i in range(len(Female_NoCo_athletes))}

# --------------------------PRICING (BASED ONLY ON LAST SEASON)------------------------------------------

max_xc_points_2022 = 1800
max_hopp_points_men_2022 = 2900
max_hopp_points_women_2022 = 1600
max_NoCo_points_men_2022 = 2000
max_NoCo_points_women_2022 = 800

price_men_XC = []
price_women_XC = []
price_men_Hopp = []
price_women_Hopp = []
price_men_NoCo = []
price_women_NoCo = []


male_XC_points_2022 = list(map(lambda x: x.replace("'", ""), male_XC_points_2022))
male_XC_points_2022 = list(map(lambda x: x.replace(" ", ""), male_XC_points_2022))
female_XC_points_2022 = list(map(lambda x: x.replace("'", ""), female_XC_points_2022))
female_XC_points_2022 = list(map(lambda x: x.replace(" ", ""), female_XC_points_2022))
Male_Jump_points_2022 = list(map(lambda x: x.replace("'", ""), Male_Jump_points_2022))
Male_Jump_points_2022 = list(map(lambda x: x.replace(" ", ""), Male_Jump_points_2022))
Female_Jump_points_2022 = list(map(lambda x: x.replace("'", ""), Female_Jump_points_2022))
Female_Jump_points_2022 = list(map(lambda x: x.replace(" ", ""), Female_Jump_points_2022))
Male_NoCo_points_2022 = list(map(lambda x: x.replace("'", ""), Male_NoCo_points_2022))
Male_NoCo_points_2022 = list(map(lambda x: x.replace(" ", ""), Male_NoCo_points_2022))
Female_NoCo_points_2022 = list(map(lambda x: x.replace("'", ""), Female_NoCo_points_2022))
Female_NoCo_points_2022 = list(map(lambda x: x.replace(" ", ""), Female_NoCo_points_2022))


for i in range(len(male_XC_points_2022)):
    price = round(3 * (((int(male_XC_points_2022[i]) / max_xc_points_2022) / 2) * 100000) / 4)
    price_men_XC.append(price)

for i in range(len(female_XC_points_2022)):
    price = round(3 * (((int(female_XC_points_2022[i]) / max_xc_points_2022) / 2) * 100000) / 4)
    price_women_XC.append(price)

for i in range(len(Male_Jump_points_2022) - 21):
    price = round(3 * (((int(Male_Jump_points_2022[i]) / max_hopp_points_men_2022) / 2) * 100000) / 4)
    price_men_Hopp.append(price)
for i in range(0, 21):
    price_men_Hopp.append(25)

for i in range(len(Female_Jump_points_2022) - 12):
    price = round(3 * (((int(Female_Jump_points_2022[i]) / max_hopp_points_women_2022) / 2) * 100000) / 4)
    price_women_Hopp.append(price)
for i in range(0, 12):
    price_women_Hopp.append(25)

for i in range(len(Male_NoCo_points_2022) - 18):
    price = round(3*(((int(Male_NoCo_points_2022[i]) / max_NoCo_points_men_2022) / 2) * 100000) / 4)
    price_men_NoCo.append(price)
for i in range(0, 18):
    price_men_NoCo.append(25)

for i in range(len(Female_NoCo_points_2022)):
    price = round(3 * (((int(Female_NoCo_points_2022[i]) / max_NoCo_points_women_2022) / 2) * 100000) / 4)
    price_women_NoCo.append(price)

price_men_XC.append(0)
price_women_XC.append(0)
price_men_NoCo.append(0)
price_women_NoCo.append(0)
price_men_Hopp.append(0)
price_women_Hopp.append(0)


male_XC_athletes.append("None")
female_XC_athletes.append("None")
Male_NoCo_athletes.append("None")
Female_NoCo_athletes.append("None")
Male_Jump_athletes.append("None")
Female_Jump_athletes.append("None")

male_XC_nationality.append("n/a")
female_XC_nationality.append("n/a")
Male_NoCo_nationality.append("n/a")
Female_NoCo_nationality.append("n/a")
Male_Jump_nationality.append("n/a")
Female_Jump_nationality.append("n/a")

male_XC_points_2022.append("n/a")
female_XC_points_2022.append("n/a")
Male_NoCo_points_2022.append("n/a")
Female_NoCo_points_2022.append("n/a")
Male_Jump_points_2022.append("n/a")
Female_Jump_points_2022.append("n/a")

Female_Jump_athletes.append("LUNDBY Maren")
Female_Jump_nationality.append("NOR")
price_women_Hopp.append(4125)

Female_NoCo_athletes.append("KORHONEN Minja")
Female_NoCo_nationality.append("FIN")
price_women_NoCo.append(4500)

Female_NoCo_Season_2022["None"]= "n/a"
Female_NoCo_Season_2022["KORHONEN Minja"] = "0"
Female_Jump_Season_2022["None"] = "n/a"
Female_Jump_Season_2022["LUNDBY Maren"] = "0"

Female_NoCo_points_2022.append("0")
Female_Jump_points_2022.append("0")

