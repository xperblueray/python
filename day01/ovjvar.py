#!/usr/bin/bash
# Filename:objvar.py

class Person:
    '''Represents a person.'''
    poppulation = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print '(Initializing %s)' % self.name
        
        
