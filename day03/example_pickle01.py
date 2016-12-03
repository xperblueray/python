#!/usr/bin/python3
# Filename: example_pickle01.py

import pickle


class Bird(object):
    have_feather        = True
    reproduction_method = "egg"


summer = Bird()

with open("summer_pickle.pkl", "w") as f:
    pickle.dump(summer, f)
