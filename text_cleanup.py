import re

test_cases = [
    "BodilyInjury",
    "AutomobileLiabilityInsurance",
    "AntilockBrakes",
    "ABCMotorCreditCompany",
    "IL010NBD",

]

def split_camel_case(text):
    pattern = r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])'
    return re.sub(pattern, '_', text).lower()

for case in test_cases:
    print(case, "->", split_camel_case(case))