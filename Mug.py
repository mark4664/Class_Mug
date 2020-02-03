#!/usr/bin/python3

# Script name: mug.py

# Mark Bradley
# 03/02/2020

# Demo of a class object built to show the use of a commom tea mug
# Kept as simple as possible to show the using a class to model a real world object.
#  *** This is the minimal version ***
# There is no test code in this version so it has to be imported before it can be used
# To use this class put the mug.py file in your working directory and following code near the start of your Python script
# from mug.py import mug

class Mug:
    ''' Class to describe the common Mug.
        Size is capacity in ml.
        Decoration,colour picture etc.
        State how many ml are in the mug at the moment.
        Clean, True if the mug has not been used
        Content, whats in the mug'''
    
    def __init__(self,size=350,decoration='Plain white',state=0,clean=True):
        # Initalize an instance of mug
        # This builds the 'mug' using the default parameter unless new ones are supplied.
        self.size=size
        self.decoration=decoration
        self.state=state
        self.clean=clean
        self.content='nothing'      # Mugs have no contentat the start
        
    def fill(self,quantity,content='Tea'):
        # quantity is the amount to put in the mug. It cannot exceed the size!
        self.content=content
        
        if quantity > (self.size - self.state):
            print('Oh dear some of that over flowed!')
            self.state = self.size
        else:
            self.state = quantity
            
        self.clean = False
        
    def empty(self):
        # Pour away the contents - state=0
        self.state=0
        
    def sip(self,sip_size=30):
        # Take a sip of the drink, default is 30ml
        if sip_size > self.state:
            print('Oh dear all your '+self.content+' has gone!')
            self.state = 0
        else:
            self.state = self.state - sip_size
    
    def wash(self):
        self.empty()
        self.clean=True
        
    def whatsleft(self):
        # Print the current state of the mug
        print('The '+ self.decoration +' mug has '+ str(self.state) +' ml of '+ self.content +' in it')
        
