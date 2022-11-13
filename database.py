import os
import ssl
from deta import Deta # pip install deta
from dotenv import load_dotenv # pip install python-env

ssl._create_default_https_context = ssl._create_unverified_context


load_dotenv(".env")
DETA_KEY = "a039qfu6_Yus4BjzGWBVkbbou8cBffWR6bzLY6jdG"

deta = Deta(DETA_KEY)

db = Deta.Base(deta, "Fantasy_League")


def insert_period(submission_date, user, weekend, Team):
    return db.put({"key": submission_date, "User": user, "Weekend": weekend, "Team": Team})


def fetch_all_periods(user):
    res = db.get(user)
    return res.items


def get_period(submission_date):
    return db.get(submission_date)
