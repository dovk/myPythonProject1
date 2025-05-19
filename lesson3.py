
from datetime import datetime
import re
patient_ids = [111, 222, 333, 444, 555, 666, 777, 888, 999, 123]
dates = ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01",
         "2023-06-01", "2023-07-01", "2023-08-01", "2023-09-01", "2023-10-01"]

test_results = [100, 90, 95, 85, 80, 95, 70, 65, 60, 55]

for test_result in test_results:
    if test_result > 70:
        for patient_id in patient_ids:
            print(f"Patient ID: {patient_id}, Test Result: {test_result}")

test_result_distinct = set(test_results)
print(test_result_distinct)

list_patient = []
for patient_id, date, test_result in zip(patient_ids, dates, test_result_distinct):
    list_patient.append({"patient_id": patient_id, "date": date,
                         "test_result": test_result})
print(list_patient)


def get_test_result(patient_id):
    test_res = 0
    "this function returns the test result for a given patient_id"
    for patient in list_patient:
        if patient["patient_id"] == patient_id:
            test_res = patient["test_result"]
            break
    return test_res


print(f"the result of 111 is {get_test_result(111)}")
print(f"the result of 123456 is {get_test_result(123456)}")
# convert string to type date
new_dates = list(map(lambda date: datetime.strptime(date, "%Y-%m-%d"), dates))
print(new_dates)


def getPhoneNumber(strPhoneNumber):
    """
    This function returns the phone number in the format (000) 000-0000.
    """
    # Remove country code if present (e.g., +972)
    pattern_country_code = r"^\+972[-\s]?"
    strPhoneNumber = re.sub(pattern_country_code, "0", strPhoneNumber)

    # Remove country code if present (e.g., 00972)
    pattern_country_code = r"^00972[-\s]?"
    strPhoneNumber = re.sub(pattern_country_code, "0", strPhoneNumber)

    # Match and reformat the phone number
    pattern = r"^(\d{3})[-\s.]?(\d{3})[-\s.]?(\d{4})$"
    res = re.match(pattern, strPhoneNumber)
    if res:
        # Reformat the phone number to (000) 000-0000
        return f"({res.group(1)}) {res.group(2)}-{res.group(3)}"
    return None


phon = "00972541234567"
result = getPhoneNumber(phon)
print(result)  # Output: (054) 123-4567

phon = "050-1234567"
result = getPhoneNumber(phon)
print(result)  # Output: (050) 123-4567

phon = "050-123-4567"
result = getPhoneNumber(phon)
print(result)  # Output: (050) 123-4567

phon = "+972541234567"
result = getPhoneNumber(phon)
print(result)  # Output: (054) 123-4567


phonNum1 = "054-1234567"
phonNum2 = "054 1234567"
phonNum3 = "054-123-4567"
phonNum4 = "08-1234567"
phonNum5 = "+972-541234567"
phonNum6 = "+972541234567"
phonNum7 = "00972541234567"
phonNum8 = "+972-54-1234567"


def retphon(phonNum):
    fixNum = ""

    return fixNum
