# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:23:13 2023

@author: yaswa
"""

import re

currency_regex1 = r'(^($|USD)\d(?:,\d{3})*(?:\.\d{2})?(?:[KMB]|))'
currency_regex2 = r'([+-]?(?:\$|USD)\d{1,3}(?:,\d{3})*(?:\.\d{2})?(?:[KMB]|))'
# currency_regex3 = r'\$\d*'
def is_valid_currency(string):
    match1 = re.findall(currency_regex1, string)
    match2 = re.findall(currency_regex2, string)
    # match3 = re.findall(currency_regex3, string)

    if match1:
        print("Currency Matched : ",match1) 
    if match2:
        print("Currency Matched : ",match2)
    # if match3:
    #     print(match3)
    # else:
    #     return None
