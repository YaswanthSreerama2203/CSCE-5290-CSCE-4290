
from currency import is_valid_currency
from date import is_valid_date
from phone import match_phone_number
from tags import match_tag
with open("input.txt", "r") as f:
    for line in f:
        print("Input:", line)
        is_valid_currency(line)
        is_valid_date(line)
        match_phone_number(line)
        match_tag(line)