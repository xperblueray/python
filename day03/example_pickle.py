#!/usr/bin/python3
# Filename: example_pickle.py

import pickle


class Bird(object):
    have_feather = True
    reproduction_method = "egg"


summer = Bird()
pickle_string = pickle.dumps(summer)


with open("summer.pkl", "wb") as f:
    f.write(pickle_string)


