import re

def split_country(input):
    country = re.sub("\d","", input)
    return country

def split_passport(input):
    passport = re.sub("\D","", input)
    return passport