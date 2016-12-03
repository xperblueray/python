#!/usr/bin/python3
# Filename: read_class.py

import pickle


class Bird(object):
    have_feather        = True
    reproduction_method = "egg"




with open("summer.pkl", "rb") as f:
    summer= pickle.load(f)


print(summer.have_feather)
