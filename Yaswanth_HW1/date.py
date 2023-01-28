# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:23:42 2023

@author: yaswa
"""

import re

date_regex = r"^(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[ ](\d{1,2}),[ ](\d{4})"
date_regex1 =r"\d{1,2}\/\d{1,2}\/\d{2}"
date_regex2=r"\d{1,2}-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec),\s\d{4}"
date_regex3=r"\d{4}-\d{2}-\d{2}$"
def is_valid_date(s):
    match1 = re.search(date_regex,s)
    match2 = re.search(date_regex1,s)
    match3 = re.search(date_regex2,s)
    match4 = re.search(date_regex3,s)
    if match1:
        print("Date Matched : ",match1.group()) 
    if match2:
        print("Date Matched : ",match2.group())
    if match3:
        print("Date Matched : ",match3.group())
    if match4:
        print("Date Matched : ",match4.group())
    # else:
    #     return None
