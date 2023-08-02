import re

def validate_credit_card(cc_number):

    cc_number = str(cc_number).strip()
    
    if not cc_number:
        return False

    cc_number = re.sub(r'[\s-]', '', cc_number)
    if not cc_number.isdigit():
        return False

    digits = [int(d) for d in cc_number]
    if len(digits) < 13 or len(digits) > 16:
        return False
        
    checksum = 0
    for i in range(len(cc_number)):
        digit = int(cc_number[i])
        if i % 2 == 0:
            digit *= 2
        checksum += digit // 10 + digit % 10
    return checksum % 10 == 0