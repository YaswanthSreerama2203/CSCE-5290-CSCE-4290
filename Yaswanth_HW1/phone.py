# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:29:02 2023

@author: yaswa
"""
import re

def match_phone_number(string):
    # phone1 = r"^\d{10}$"
    phone2 = r"^\+\d{1}\s?\d{3}\s?\d{3}\s?-?\d{4}$"
    phone3 = r"^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$"
    phone4 = r"^00\d{1}[-\s]?\d{3}[-\s]?\d{3}[-\s]?\d{4}$"
    # match = re.search(phone1, string)
    match1 = re.findall(phone2, string)
    match2 = re.findall(phone3, string)
    match3 = re.findall(phone4, string)
    # if match:
    #     # print("Phone Number Matched : ",match.group()) 
    if match1 :
        print("Phone Number Matched : ",match1)
    if match2 :
        print("Phone Number Matched : ",match2)
    if match3 :
        print("Phone Number Matched : ",match3)
    else:
        return None
match_phone_number('001-601-266-4949')