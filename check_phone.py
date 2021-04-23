import re

def Check_phone(phone):
    result = re.match('^\d[\d\(\)\ -]{4,14}\d$', phone)
    if result:
        return True
    else:
        return False
