import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Michael Brubaker", "Carter Brubaker", "Tate Frantz", "Johannes Årdal", "Magnus Jetlund", "Sander Bakken",
         "Fabian Østvold", "Alex Yigermal", "Ronen Woods", "Torje Seljeset", "Robert"]

usernames = ["mbrubaker", "cardiB", "Tatefirstplace", "Johannesburg", "TheJet", "Sandman", "Fab", "Jigs", "Woody",
             "primal", "Robert"]

passwords = ["XXX", "XXX", "XXX", "XXX", "XXX", "XXX", "XXX",
             "XXX", "XXX", "XXX", "Rob1234"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__). parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

