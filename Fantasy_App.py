import calendar
from datetime import datetime
import pickle
from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import database as db
import streamlit_authenticator as stauth
import requests
from streamlit_lottie import st_lottie
import json


from FIS_WEB_SCRAPE import Men_XC_Season_2022,\
    male_XC_athletes, male_XC_nationality, male_XC_points_2022,   \
    female_XC_points_2022, female_XC_athletes, female_XC_nationality, Women_XC_Season_2022, \
    Male_Jump_Season_2022, Male_Jump_nationality, Male_Jump_athletes, Female_Jump_athletes, Male_NoCo_athletes, \
    Male_Jump_points_2022, Female_Jump_Season_2022, Female_Jump_points_2022, Female_Jump_nationality, \
    Male_NoCo_points_2022, Male_NoCo_nationality, Male_NoCo_Season_2022, Female_NoCo_points_2022, \
    Female_NoCo_Season_2022, price_women_NoCo, price_men_XC, price_women_XC, price_men_Hopp, price_women_Hopp, \
    price_men_NoCo, Female_NoCo_nationality, Female_NoCo_athletes

from Exel_Upload import df_Alex, df_Dad, df_Tate, df_Torje, df_Ronen, df_Fabian, df_Sander, df_Johannes, df_Magnus


# ----------------Settings--------------------
page_title = "Carter Brubaker's Fantasy Ski League"
page_icon = ":ski:"
sports = ["Cross Country", "Nordic Combined", "Ski Jumping"]
seasons = ["2021/22", "2022/23"]
genders = ["Men", "Women"]
weekends_XC = {"Ruka": "25-27 Nov 2022", "Lillehammer": "2-4 Dec 2022", "Beitostolen": "9-11 Dec 2022",
                   "Davos": "17-18 Dec 2022", "Tour De Ski": "31 Dec - 08 Jan 2023", "Milano": "21-22 Jan 2023",
                   "Les Rousses": "27-29 Jan 2023", "Toblach": "3-5 Feb 2023", "World Championships": "21 Feb-Mar 5 2023",
                   "Oslo": "11-12 Mar 2023", "Drammen": "14 Mar 2023", "Falun": "17-19 Mar 2023", "Tallinn": "21 Mar 2023",
                   "Lahti": "24-26 Mar 2023"}
weekends_NoCo_Men = {"Ruka": "24-27 Nov 2022", "Lillehammer": "1-4 Dec 2022", "Ramsau": "15-18 Dec 2022",
                         "Otepaa": "5-8 Jan 2023", "Klingenthal": "13-15 Jan 2023", "Chaux-Neuva": "20-22 Jan 2023",
                         "Seefeld": "26-29 Jan 2023", "Oberstdorf": "3-5 Feb 2023", "Schonach": "10-12 Feb 2023",
                         "World Championships": "24 Feb- 4 Mar 2023", "Oslo": "8-12 Mar 2023", "Lahti": "24-27 Mar 2023"}
weekends_NoCo_Women = {"Lillehammer": "1-4 Dec 2022", "Ramsau": "15-18 Dec 2022", "Otepaa": "5-8 Jan 2023",
                           "Seefeld": "26-29 Jan 2023", "Schonach": "10-12 Feb 2023",
                           "World Championships": "24 Feb- 4 Mar 2023", "Oslo": "8-12 Mar 2023"}
weekends_Jumping_Men = {"Wisla": "4-6 Nov 2022", "Ruka": "25-27 Nov 2022", "Titisee Neustadt": "8-11 Dec 2022",
                            "Engelberg": "16-18 Dec 2022", "Four Hills Tournament": "29 Dec 2022 - 6 Jan 2023",
                            "Zakopane": "13-15 Jan 2023", "Sapporo": "19-22 Jan 2023", "Kulm Mitterndorf": "27-29 Jan 2023",
                            "Willingen": "2-5 Feb 2023", "Lake Placid": "10-12 Feb 2023", "Rasnov": "17-19 Feb 2023",
                            "World Championships": "21 Feb-5 Mar 2023", "Raw Air Tournament": "11-19 Mar 2023",
                            "Lahti": "23-26 Mar 2023", "Planica": "30 Mar-2 April 2023"}
weekends_Jumping_Women = {"Wisla": "4-6 Nov 2022", "Lillehammer": "2-4 Dec 2022", "Titisee Neustadt": "8-11 Dec 2022",
                              "Silvester Tournament": "27 Dec 2022- 1 Jan 2023", "Sapporo": "6-8 Jan 2023",
                              "Zao": "12-15 Jan 2023", "Hinterzarten": "27-29 Jan 2023", "Willingen": "2-5 Feb 2023",
                              "Hinzenbach": "10-11 Feb 2023", "Rasnov": "17-19 Feb 2023", "Oslo": "10-12 Mar 2023",
                              "Lillehammer_2": "13-16 Mar 2023", "Vikersund": "17-19 Mar 2023", "Lahti": "23-26 Mar 2023"}
date_time = datetime.now()
st.session_state['time'] = date_time

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Lottie Annimations
lottie_submitted = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_dzlwceyg.json")
lottie_snow = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_0tyvusxj.json")
lottie_ski = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tzmFl7.json")

# ---------------------------------------
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")
st.title(page_title + "  ")

# ------------USER AUTHENTICATION---------------

names = ["Michael Brubaker", "Carter Brubaker", "Tate Frantz", "Johannes Årdal", "Magnus Jetlund", "Sander Bakken",
         "Fabian Østvold", "Alex Yigermal", "Ronen Woods", "Torje Seljeset"]

usernames = ["mbrubaker", "cardiB", "Tatefirstplace", "Johannesburg", "TheJet", "Sandman", "Fab", "Jigs", "Woody",
             "primal"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "Carter's Fantasy Ski League", "abcdef",
                                    cookie_expiry_days=7)
name, authentication_status, username = authenticator.login("Login", "sidebar")


if authentication_status == False:
    st.error("Username/Password incorrect")
    st.text("If you forgot or don't have an account contact Carter")


if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    with st.sidebar:
        st.sidebar.header(f"Welcome {name}")
        st.sidebar.subheader(f"Today is: \n {datetime.now().date()}")




    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Athletes", "Events", "Team Selection", "My Team", "Standings"],
        icons=["house", "person-video2", "calendar-date", "person-plus", ":bar_chart:"],
        orientation="horizontal",
        )
    "---"

    if selected == "Athletes":
        st.header("Athletes")
        st.text("You will have 100,000 dollars for team selection in each sport. 50,000 for each gender.")
        st.text("Make sure to add up the prices of the athletes so your total team")
        st.text("price for each sport does not exceed 10,0000.")
        st.text("Team selection can be found on the Team Selection Tab")
        "---"
        option = st.selectbox("Which Sport would you like to see?", sports)
        "---"
        if option == "Cross Country":
                st.subheader("Cross Country")
                gender_select = st.selectbox("Which gender?", genders)
                if gender_select == "Men":
                    data = {'Athlete': male_XC_athletes, "Nationality": male_XC_nationality,
                            "Points 21/22 Season": male_XC_points_2022, "Price": price_men_XC}
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                if gender_select == "Women":
                    data = {'Athlete': female_XC_athletes, "Nationality": female_XC_nationality,
                            "Points 21/22 Season": female_XC_points_2022, "Price": price_women_XC}
                    df = pd.DataFrame(data)
                    st.dataframe(df)
        if option == "Ski Jumping":
                st.subheader("Ski Jumping")
                gender_select = st.selectbox("Which gender?", genders)
                if gender_select == "Men":
                    data = {'Athlete': Male_Jump_athletes, "Nationality": Male_Jump_nationality,
                            "Points 21/22 Season": Male_Jump_points_2022, "Price": price_men_Hopp}
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                if gender_select == "Women":
                    data = {'Athlete': Female_Jump_athletes, "Nationality": Female_Jump_nationality,
                            "Points 21/22 Season": Female_Jump_points_2022, "Price": price_women_Hopp}
                    df = pd.DataFrame(data)
                    st.dataframe(df)
        if option == "Nordic Combined":
                st.subheader("Nordic Combined")
                gender_select = st.selectbox("Which gender?", genders)
                if gender_select == "Men":
                    data = {'Athlete': Male_NoCo_athletes, "Nationality": Male_NoCo_nationality,
                            "Points 21/22 Season": Male_NoCo_points_2022, "Price": price_men_NoCo}
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                if gender_select == "Women":
                    data = {'Athlete': Female_NoCo_athletes, "Nationality": Female_NoCo_nationality,
                            "Points 21/22 Season": Female_NoCo_points_2022, "Price": price_women_NoCo}
                    df = pd.DataFrame(data)
                    st.dataframe(df)

    if selected == "Team Selection":
            st.text("Choose up to eight athletes of each gender in each sport.")
            st.text("You will have 50,000 dollars per gender for your team. See the athlete prices on the athletes tab.")
            st.text("If you don't want to fill a slot, scroll to the bottom and select None.")
            sport_selection = st.selectbox("Which Sport", sports)
            if sport_selection == "Cross Country":
                gender_selection = st.selectbox("Which gender", genders)
                if gender_selection == "Men":
                    st.header("Team Selection Men XC")
                    with st.form("entry_form", clear_on_submit=True):
                        weekend_selection = st.selectbox("Select weekend", weekends_XC)
                        st.session_state['weekend_selection'] = weekend_selection
                        team_total = []
                        team_names = []
                        "---"
                        selection1 = st.selectbox("Select first member of team", male_XC_athletes)
                        if selection1 != "None":
                            team_names.append(selection1)
                            index1 = male_XC_athletes.index(selection1)
                            team_total.append(int(price_men_XC[index1]))

                        selection2 = st.selectbox("Select second member of your team", male_XC_athletes)
                        if selection2 != "None":
                            team_names.append(selection2)
                            index2 = male_XC_athletes.index(selection2)
                            team_total.append(int(price_men_XC[index2]))

                        selection3 = st.selectbox("Select third member of your team", male_XC_athletes)
                        if selection3 != "None":
                            team_names.append(selection3)
                            index3 = male_XC_athletes.index(selection3)
                            team_total.append(int(price_men_XC[index3]))

                        selection4 = st.selectbox("Select fourth member of your team", male_XC_athletes)
                        if selection4 != "None":
                            team_names.append(selection4)
                            index4 = male_XC_athletes.index(selection4)
                            team_total.append(int(price_men_XC[index4]))

                        selection5 = st.selectbox("Select fifth member of your team", male_XC_athletes)
                        if selection5 != "None":
                            team_names.append(selection5)
                            index5 = male_XC_athletes.index(selection5)
                            team_total.append(int(price_men_XC[index5]))

                        selection6 = st.selectbox("Select sixth member of your team", male_XC_athletes)
                        if selection6 != "None":
                            team_names.append(selection6)
                            index6 = male_XC_athletes.index(selection6)
                            team_total.append(int(price_men_XC[index6]))

                        selection7 = st.selectbox("Select seventh member of your team", male_XC_athletes)
                        if selection7 != "None":
                            team_names.append(selection7)
                            index7 = male_XC_athletes.index(selection7)
                            team_total.append(int(price_men_XC[index7]))

                        selection8 = st.selectbox("Select final member of your team", male_XC_athletes)
                        if selection8 != "None":
                            team_names.append(selection8)
                            index8 = male_XC_athletes.index(selection8)
                            team_total.append(int(price_men_XC[index8]))
                        "---"
                        submitted = st.form_submit_button("Save Team")

                        # ---------- SUBMISSION PERAMETERS ----------------------
                        if submitted and sum(team_total) > 50000:
                            submitted = False
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                st.warning(f"Your team contains duplicate athletes and your sum is greater than 50,000 dollars. Your total is {sum(team_total)} dollars")
                            if len(unique_names) == len(team_names):
                                st.warning(f"Your Team total is above 50,000 dollars. Your total is: {sum(team_total)} dollars")

                        if submitted and sum(team_total) <= 50000:
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                submitted = False
                                print(team_names)
                                print(unique_names)
                                st.warning("Your team contains duplicate athletes")
                            if len(unique_names) == len(team_names):
                                submitted = True
                                st.session_state['Team_names'] = team_names
                                st.session_state.Team_names = team_names
                                json_str = json.dumps({'submitted': date_time}, default = str)
                                st.session_state.weekend_selection = weekend_selection
                                db.insert_period(json_str, name, st.session_state.weekend_selection,
                                                 st.session_state.Team_names)
                                st.success(f"Your Mens XC Team for {weekend_selection} Has ben saved. Your sum was: {sum(team_total)} dollars")
                                st_lottie(lottie_submitted, 1.5, False, False, "low", 50, 50)
                        # -----------------------------------------------------------------------------------

                if gender_selection == "Women":
                    st.header("Team Selection Women XC")
                    with st.form("entry_form", clear_on_submit=True):
                        weekend_selection = st.selectbox("Select weekend", weekends_XC)
                        team_total = []
                        team_names = []
                        "---"
                        selection1 = st.selectbox("Select first member of team", female_XC_athletes)
                        if selection1 != "None":
                            team_names.append(selection1)
                            index1 = female_XC_athletes.index(selection1)
                            team_total.append(int(price_women_XC[index1]))

                        selection2 = st.selectbox("Select second member of your team", female_XC_athletes)
                        if selection2 != "None":
                            team_names.append(selection2)
                            index2 = female_XC_athletes.index(selection2)
                            team_total.append(int(price_women_XC[index2]))

                        selection3 = st.selectbox("Select third member of your team", female_XC_athletes)
                        if selection3 != "None":
                            team_names.append(selection3)
                            index3 = female_XC_athletes.index(selection3)
                            team_total.append(int(price_women_XC[index3]))

                        selection4 = st.selectbox("Select fourth member of your team", female_XC_athletes)
                        if selection4 != "None":
                            team_names.append(selection4)
                            index4 = female_XC_athletes.index(selection4)
                            team_total.append(int(price_women_XC[index4]))

                        selection5 = st.selectbox("Select fifth member of your team", female_XC_athletes)
                        if selection5 != "None":
                            team_names.append(selection5)
                            index5 = female_XC_athletes.index(selection5)
                            team_total.append(int(price_women_XC[index5]))

                        selection6 = st.selectbox("Select sixth member of your team", female_XC_athletes)
                        if selection6 != "None":
                            team_names.append(selection6)
                            index6 = female_XC_athletes.index(selection6)
                            team_total.append(int(price_women_XC[index6]))

                        selection7 = st.selectbox("Select seventh member of your team", female_XC_athletes)
                        if selection3 != "None":
                            team_names.append(selection7)
                            index7 = female_XC_athletes.index(selection7)
                            team_total.append(int(price_women_XC[index7]))

                        selection8 = st.selectbox("Select final member of your team", female_XC_athletes)
                        if selection8 != "None":
                            team_names.append(selection8)
                            index8 = female_XC_athletes.index(selection8)
                            team_total.append(int(price_women_XC[index8]))
                        "---"
                        submitted = st.form_submit_button("Save Team")

                        if submitted and sum(team_total) > 50000:
                            submitted = False
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                st.warning(
                                    f"Your team contains duplicate athletes and your sum is greater than 50,000 dollars. Your sum is: {sum(team_total)} dollars")
                            if len(unique_names) == len(team_names):
                                st.warning(f"Your Team total is above 50,000 dollars. Your Total is: {sum(team_total)} dollars")

                        if submitted and sum(team_total) <= 50000:
                            unique_names = pd.series(unique_names).unique
                            if len(unique_names) != len(team_names):
                                submitted = False
                                print(team_names)
                                print(unique_names)
                                st.warning("Your team contains duplicate athletes")
                            if len(unique_names) == len(team_names):
                                submitted = True
                                st.session_state['Team_names'] = team_names
                                st.session_state.Team_names = team_names
                                json_str = json.dumps({'submitted': date_time}, default=str)
                                st.session_state.weekend_selection = weekend_selection
                                db.insert_period(json_str, name, st.session_state.weekend_selection,
                                                 st.session_state.Team_names)
                                st.success(f"Your Womens XC Team for {weekend_selection} Has ben saved. Your sum was: {sum(team_total)} dollars")
                                st_lottie(lottie_submitted, 1.5, False, False, "low", 50, 50)
            if sport_selection == "Ski Jumping":
                gender_selection = st.selectbox("Which gender", genders)
                if gender_selection == "Men":
                    st.header("Team Selection Men's Jumping")
                    with st.form("entry_form", clear_on_submit=True):
                        weekend_selection = st.selectbox("Select weekend", weekends_Jumping_Men)
                        team_total = []
                        team_names = []
                        "---"
                        selection1 = st.selectbox("Select first member of team", Male_Jump_athletes)
                        if selection1 != "None":
                            team_names.append(selection1)
                            index1 = Male_Jump_athletes.index(selection1)
                            team_total.append(int(price_men_Hopp[index1]))

                        selection2 = st.selectbox("Select second member of your team", Male_Jump_athletes)
                        if selection2 != "None":
                            team_names.append(selection2)
                            index2 = Male_Jump_athletes.index(selection2)
                            team_total.append(int(price_men_Hopp[index2]))

                        selection3 = st.selectbox("Select third member of your team", Male_Jump_athletes)
                        if selection3 != "None":
                            team_names.append(selection3)
                            index3 = Male_Jump_athletes.index(selection3)
                            team_total.append(int(price_men_Hopp[index3]))

                        selection4 = st.selectbox("Select fourth member of your team", Male_Jump_athletes)
                        if selection4 != "None":
                            team_names.append(selection4)
                            index4 = Male_Jump_athletes.index(selection4)
                            team_total.append(int(price_men_Hopp[index4]))

                        selection5 = st.selectbox("Select fifth member of your team", Male_Jump_athletes)
                        if selection5 != "None":
                            team_names.append(selection5)
                            index5 = Male_Jump_athletes.index(selection5)
                            team_total.append(int(price_men_Hopp[index5]))

                        selection6 = st.selectbox("Select sixth member of your team", Male_Jump_athletes)
                        if selection6 != "None":
                            team_names.append(selection6)
                            index6 = Male_Jump_athletes.index(selection6)
                            team_total.append(int(price_men_Hopp[index6]))

                        selection7 = st.selectbox("Select seventh member of your team", Male_Jump_athletes)
                        if selection7 != "None":
                            team_names.append(selection7)
                            index7 = Male_Jump_athletes.index(selection7)
                            team_total.append(int(price_men_Hopp[index7]))

                        selection8 = st.selectbox("Select final member of your team", Male_Jump_athletes)
                        if selection8 != "None":
                            team_names.append(selection8)
                            index8 = Male_Jump_athletes.index(selection8)
                            team_total.append(int(price_men_Hopp[index8]))
                        "---"
                        submitted = st.form_submit_button("Save Team")
                        if submitted and sum(team_total) > 50000:
                            submitted = False
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                st.warning(
                                    f"Your team contains duplicate athletes and your sum is greater than 50,000 dollars. Your total is: {sum(team_total)} dollars")
                            if len(unique_names) == len(team_names):
                                st.warning(f"Your Team total is above 50,000 dollars. Your total is: {sum(team_total)} dollars")

                        if submitted and sum(team_total) <= 50000:
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                submitted = False
                                print(team_names)
                                print(unique_names)
                                st.warning("Your team contains duplicate athletes")
                            if len(unique_names) == len(team_names):
                                submitted = True
                                st.session_state['Team_names'] = team_names
                                st.session_state.Team_names = team_names
                                json_str = json.dumps({'submitted': date_time}, default=str)
                                st.session_state.weekend_selection = weekend_selection
                                db.insert_period(json_str, name, st.session_state.weekend_selection,
                                                 st.session_state.Team_names)
                                st.success(f"Your Mens Ski Jumping Team for {weekend_selection} Has ben saved. Your total was {sum(team_total)} dollars")
                                st_lottie(lottie_submitted, 1.5, False, False, "low", 50, 50)
                if gender_selection == "Women":
                    st.header("Team Selection Women's Jumping")
                    with st.form("entry_form", clear_on_submit=True):
                        weekend_selection = st.selectbox("Select weekend", weekends_Jumping_Women)
                        team_total = []
                        team_names = []
                        "---"
                        selection1 = st.selectbox("Select first member of team", Female_Jump_athletes)
                        if selection1 != "None":
                            team_names.append(selection1)
                            index1 = Female_Jump_athletes.index(selection1)
                            team_total.append(int(price_women_Hopp[index1]))

                        selection2 = st.selectbox("Select second member of your team", Female_Jump_athletes)
                        if selection2 != "None":
                            team_names.append(selection2)
                            index2 = Female_Jump_athletes.index(selection2)
                            team_total.append(int(price_women_Hopp[index2]))

                        selection3 = st.selectbox("Select third member of your team", Female_Jump_athletes)
                        if selection3 != "None":
                            team_names.append(selection3)
                            index3 = Female_Jump_athletes.index(selection3)
                            team_total.append(int(price_women_Hopp[index3]))

                        selection4 = st.selectbox("Select fourth member of your team", Female_Jump_athletes)
                        if selection4 != "None":
                            team_names.append(selection4)
                            index4 = Female_Jump_athletes.index(selection4)
                            team_total.append(int(price_women_Hopp[index4]))

                        selection5 = st.selectbox("Select fifth member of your team", Female_Jump_athletes)
                        if selection5 != "None":
                            team_names.append(selection5)
                            index5 = Female_Jump_athletes.index(selection5)
                            team_total.append(int(price_women_Hopp[index5]))

                        selection6 = st.selectbox("Select sixth member of your team", Female_Jump_athletes)
                        if selection6 != "None":
                            team_names.append(selection6)
                            index6 = Female_Jump_athletes.index(selection6)
                            team_total.append(int(price_women_Hopp[index6]))

                        selection7 = st.selectbox("Select seventh member of your team", Female_Jump_athletes)
                        if selection7 != "None":
                            team_names.append(selection7)
                            index7 = Female_Jump_athletes.index(selection7)
                            team_total.append(int(price_women_Hopp[index7]))

                        selection8 = st.selectbox("Select final member of your team", Female_Jump_athletes)
                        if selection8 != "None":
                            team_names.append(selection8)
                            index8 = Female_Jump_athletes.index(selection8)
                            team_total.append(int(price_women_Hopp[index8]))
                        "---"
                        submitted = st.form_submit_button("Save Team")
                        if submitted and sum(team_total) > 50000:
                            submitted = False
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                st.warning(
                                    f"Your team contains duplicate athletes and your sum is greater than 50,000 dollars. Your total is: {sum(team_total)} dollars")
                            if len(unique_names) == len(team_names):
                                st.warning(f"Your Team total is above 50,000 dollars. Your total is: {sum(team_total)} dollars.")

                        if submitted and sum(team_total) <= 50000:
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                submitted = False
                                print(team_names)
                                print(unique_names)
                                st.warning("Your team contains duplicate athletes")
                            if len(unique_names) == len(team_names):
                                submitted = True
                                st.session_state['Team_names'] = team_names
                                st.session_state.Team_names = team_names
                                json_str = json.dumps({'submitted': date_time}, default=str)
                                st.session_state.weekend_selection = weekend_selection
                                db.insert_period(json_str, name, st.session_state.weekend_selection,
                                                 st.session_state.Team_names)
                                st.success(f"Your Womens Ski Jumping Team for {weekend_selection} Has ben saved. Your total was: {sum(team_total)} dollars")
                                st_lottie(lottie_submitted, 1.5, False, False, "low", 50, 50)
            if sport_selection == "Nordic Combined":
                gender_selection = st.selectbox("Which gender", genders)
                if gender_selection == "Men":
                    st.header("Team Selection Men Nordic Combined")
                    with st.form("entry_form", clear_on_submit=True):
                        weekend_selection = st.selectbox("Select weekend", weekends_NoCo_Men)
                        team_total = []
                        team_names = []
                        "---"
                        selection1 = st.selectbox("Select first member of team", Male_NoCo_athletes)
                        if selection1 != "None":
                            team_names.append(selection1)
                            index1 = Male_NoCo_athletes.index(selection1)
                            team_total.append(int(price_men_NoCo[index1]))

                        selection2 = st.selectbox("Select second member of your team", Male_NoCo_athletes)
                        if selection2 != "None":
                            team_names.append(selection2)
                            index2 = Male_NoCo_athletes.index(selection2)
                            team_total.append(int(price_men_NoCo[index2]))

                        selection3 = st.selectbox("Select third member of your team", Male_NoCo_athletes)
                        if selection3 != "None":
                            team_names.append(selection3)
                            index3 = Male_NoCo_athletes.index(selection3)
                            team_total.append(int(price_men_NoCo[index3]))

                        selection4 = st.selectbox("Select fourth member of your team", Male_NoCo_athletes)
                        if selection4 != "None":
                            team_names.append(selection4)
                            index4 = Male_NoCo_athletes.index(selection4)
                            team_total.append(int(price_men_NoCo[index4]))

                        selection5 = st.selectbox("Select fifth member of your team", Male_NoCo_athletes)
                        if selection5 != "None":
                            team_names.append(selection5)
                            index5 = Male_NoCo_athletes.index(selection5)
                            team_total.append(int(price_men_NoCo[index5]))

                        selection6 = st.selectbox("Select sixth member of your team", Male_NoCo_athletes)
                        if selection6 != "None":
                            team_names.append(selection6)
                            index6 = Male_NoCo_athletes.index(selection6)
                            team_total.append(int(price_men_NoCo[index6]))

                        selection7 = st.selectbox("Select seventh member of your team", Male_NoCo_athletes)
                        if selection7 != "None":
                            team_names.append(selection7)
                            index7 = Male_NoCo_athletes.index(selection7)
                            team_total.append(int(price_men_NoCo[index7]))

                        selection8 = st.selectbox("Select final member of your team", Male_NoCo_athletes)
                        if selection8 != "None":
                            team_names.append(selection8)
                            index8 = Male_NoCo_athletes.index(selection8)
                            team_total.append(int(price_men_NoCo[index8]))
                        "---"
                        submitted = st.form_submit_button("Save Team")
                        if submitted and sum(team_total) > 50000:
                            submitted = False
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                st.warning(
                                    f"Your team contains duplicate athletes and your sum is greater than 50,000 dollars. Your total is: {sum(team_total)} dollars")
                            if len(unique_names) == len(team_names):
                                st.warning(f"Your Team total is above 50,000 dollars. Your total is: {sum(team_total)} dollars")

                        if submitted and sum(team_total) <= 50000:
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                submitted = False
                                print(team_names)
                                print(unique_names)
                                st.warning("Your team contains duplicate athletes")
                            if len(unique_names) == len(team_names):
                                submitted = True
                                st.session_state['Team_names'] = team_names
                                st.session_state.Team_names = team_names
                                json_str = json.dumps({'submitted': date_time}, default=str)
                                st.session_state.weekend_selection = weekend_selection
                                db.insert_period(json_str, name, st.session_state.weekend_selection,
                                                 st.session_state.Team_names)
                                st.success(f"Your Mens Nordic Combined Team for {weekend_selection} Has ben saved. Your total was: {sum(team_total)} dollars")
                                st_lottie(lottie_submitted, 1.5, False, False, "low", 50, 50)
                if gender_selection == "Women":
                    st.header("Team Selection Women NoCo")
                    with st.form("entry_form", clear_on_submit=True):
                        weekend_selection = st.selectbox("Select weekend", weekends_NoCo_Women)
                        team_total = []
                        team_names = []
                        "---"
                        selection1 = st.selectbox("Select first member of team", Female_NoCo_athletes)
                        if selection1 != "None":
                            team_names.append(selection1)
                            index1 = Female_NoCo_athletes.index(selection1)
                            team_total.append(int(price_women_NoCo[index1]))

                        selection2 = st.selectbox("Select second member of your team", Female_NoCo_athletes)
                        if selection2 != "None":
                            team_names.append(selection2)
                            index2 = Female_NoCo_athletes.index(selection2)
                            team_total.append(int(price_women_NoCo[index2]))

                        selection3 = st.selectbox("Select third member of your team", Female_NoCo_athletes)
                        if selection3 != "None":
                            team_names.append(selection3)
                            index3 = Female_NoCo_athletes.index(selection3)
                            team_total.append(int(price_women_NoCo[index3]))

                        selection4 = st.selectbox("Select fourth member of your team", Female_NoCo_athletes)
                        if selection4 != "None":
                            team_names.append(selection4)
                            index4 = Female_NoCo_athletes.index(selection4)
                            team_total.append(int(price_women_NoCo[index4]))

                        selection5 = st.selectbox("Select fifth member of your team", Female_NoCo_athletes)
                        if selection5 != "None":
                            team_names.append(selection5)
                            index5 = Female_NoCo_athletes.index(selection5)
                            team_total.append(int(price_women_NoCo[index5]))

                        selection6 = st.selectbox("Select sixth member of your team", Female_NoCo_athletes)
                        if selection6 != "None":
                            team_names.append(selection6)
                            index6 = Female_NoCo_athletes.index(selection6)
                            team_total.append(int(price_women_NoCo[index6]))

                        selection7 = st.selectbox("Select seventh member of your team", Female_NoCo_athletes)
                        if selection7 != "None":
                            team_names.append(selection7)
                            index7 = Female_NoCo_athletes.index(selection7)
                            team_total.append(int(price_women_NoCo[index7]))

                        selection8 = st.selectbox("Select final member of your team", Female_NoCo_athletes)
                        if selection8 != "None":
                            team_names.append(selection8)
                            index8 = Female_NoCo_athletes.index(selection8)
                            team_total.append(int(price_women_NoCo[index8]))
                        "---"
                        submitted = st.form_submit_button("Save Team")
                        if submitted and sum(team_total) > 50000:
                            submitted = False
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                st.warning(
                                    f"Your team contains duplicate athletes and your sum is greater than 50,000 dollars. Your total is: {sum(team_total)} dollars")
                            if len(unique_names) == len(team_names):
                                st.warning(f"Your Team total is above 50,000 dollars. Your total is: {sum(team_total)} dollars")

                        if submitted and sum(team_total) <= 50000:
                            unique_names = pd.series(team_names).unique
                            if len(unique_names) != len(team_names):
                                submitted = False
                                print(team_names)
                                print(unique_names)
                                st.warning("Your team contains duplicate athletes")
                            if len(unique_names) == len(team_names):
                                submitted = True
                                st.session_state['Team_names'] = team_names
                                st.session_state.Team_names = team_names
                                json_str = json.dumps({'submitted': date_time}, default=str)
                                st.session_state.weekend_selection = weekend_selection
                                db.insert_period(json_str, name, st.session_state.weekend_selection,
                                                 st.session_state.Team_names)
                                st.success(f"Your Womens Nordic Combined Team for {weekend_selection} Has ben saved. Your total was: {sum(team_total)} dollars")
                                st_lottie(lottie_submitted, 1.5, False, False, "low", 50, 50)

    if selected == "Events":
            eventspage_sport_selection = st.selectbox("What sport?", sports)
            if eventspage_sport_selection == "Cross Country":
                events_data = {"Weekends": weekends_XC}
                df = pd.DataFrame(events_data)
                st.dataframe(df)
            if eventspage_sport_selection == "Ski Jumping":
                events_data = {"Weekends Men": weekends_Jumping_Men, "Weekends Women": weekends_Jumping_Women}
                df = pd.DataFrame(events_data)
                st.dataframe(df)
            if eventspage_sport_selection == "Nordic Combined":
                events_data = {"Weekends Men": weekends_NoCo_Men, "Weekends Women": weekends_NoCo_Women}
                df = pd.DataFrame(events_data)
                st.dataframe(df)

    if selected == "My Team":
        st.header("My Teams")
        with st.form("My Teams"):
            TEAMS = pd.DataFrame(db.fetch_all_periods())
        st.dataframe(TEAMS)

    if selected == "Home":
        st.header("Welcome to the Fantasy Ski League!")
        st.subheader("Look at the athletes and their prices with the athletes tab, and then select your team by clicking "
                     "the team selection tab. To look at the FIS event schedule, check out Events. Enjoy!")

    if selected == "Standings":
        st.header("Standings World Cup 2022/23")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.dataframe(df_Alex)
            st.dataframe(df_Magnus)
            st.dataframe(df_Dad)
        with col2:
            st.dataframe(df_Tate)
            st.dataframe(df_Torje)
            st.dataframe(df_Sander)
        with col3:
            st.dataframe(df_Ronen)
            st.dataframe(df_Johannes)
            st.dataframe(df_Fabian)


