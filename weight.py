#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:10:27 2019

@author: william keilsohn
"""

# Based off of 4chan's weight loss callorie program:

# Import Packages:
#import numpy as np

# Define A Class for the possiblities:
class WCalc:
    
    def __init__(self, weight = 0):
        self.weight = weight
    
    gain_mussle_vals = [16, 18]
    loose_fat_vals = [10, 12]
    maintain_vals = [14, 15]
    
    
    def getUserWeight(self):
        self.weight = int(input('Please enter your current weight (lb): '))
        
    def looseWeight(self):
        loose_cals = list(map(lambda x: self.weight * x, self.loose_fat_vals))
        print(loose_cals)
    
    def maintainWeight(self):
        same_cals = list(map(lambda x: self.weight * x, self.maintain_vals))
        print(same_cals)
        
    def gainMusscle(self):
        gain_cals = list(map(lambda x: self.weight * x, self.gain_mussle_vals))
        print(gain_cals)
        

# Facilitate user experiance:

class User:
    
    def __init__(self, run = True):
        self.run = run
        
    yes_vals = ['Yes', 'yes', 'y', 'Y', 'Yup', 'yis', 'YES']
    sel_vlas = '''Please select one of the following options by entering its number:
                0) Loose Weight
                1) Maintain Weight
                2) Gain Mussle
    '''
        
    def setRun(self):
        user_anser = input("Would you like to continue? ")
        if user_anser in self.yes_vals:
            self.run = True
        else:
            self.run = False
            
    def getRun(self):
        return self.run
    
    def sortCalc(self, obj):
        print(self.sel_vlas)
        user_anser = int(input("Enter your selection here: "))
        print('\n')
        if user_anser == 0:
            obj.looseWeight()
        elif user_anser == 1:
            obj.maintainWeight()
        else:
            obj.gainMusscle()
    
# Make a few objects
c1 = WCalc()
u1 = User()            

# Get user Weight:
c1.getUserWeight()

# Ask followup questions and run analysis
        
while u1.run:
    
    print('\n')
    u1.sortCalc(c1)
    print('\n')
    u1.setRun()

# End process    
print("Thank you for using my tool.")