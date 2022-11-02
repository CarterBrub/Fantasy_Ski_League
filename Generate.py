import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Michael Brubaker", "Carter Brubaker", "Tate Frantz", "Johannes Årdal", "Magnus Jetlund", "Sander Bakken",
         "Fabian Østvold", "Alex Yigermal", "Ronen Woods", "Torje Seljeset"]

usernames = ["mbrubaker", "cardiB", "Tatefirstplace", "Johannesburg", "TheJet", "Sandman", "Fab", "Jigs", "Woody",
             "primal"]

passwords = ["XXX", "XXX", "XXX", "XXX", "XXX", "XXX", "XXX",
             "XXX", "XXX", "XXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__). parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

