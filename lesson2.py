# x = 20
# if x == 10 or x == 20 or x == 30:
#     print("x is 10 or 20 or 30")
# else:
#     print("x is not present")

# print(list(range(5)))

# %%
# x = 0
# while x < 4:
#     passw = input("enter passw:")
#     if passw == "batbatbat":
#         print("u are in ")
#         break
#     x += 1
# else:
#     print("this is your 4 time so by by")

# %%
# fruits = ["banana", "apple", "orange"]
# colors = ["yellow", "red", "orange", "kiwi"]

# for fruit, color in zip(fruits, colors):
#     print(fruit, color)

# %%
# patient_ids = [111, 222, 333, 444, 555, 666, 777, 888, 999, 123]
# dates = ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01",
#          "2023-06-01", "2023-07-01", "2023-08-01", "2023-09-01", "2023-10-01"]

# test_results = [100, 90, 95, 85, 80, 95, 70, 65, 60, 55]
# # for patient_id in patient_ids:
# #     print(type(patient_id))
# # print(type(dates))
# # print(type(test_results))

# for test_result in test_results:
#     if test_result > 70:
#         for patient_id in patient_ids:
#             print(f"Patient ID: {patient_id}, Test Result: {test_result}")

# test_result_distinct = set(test_results)
# print(test_result_distinct)

# list_patient = []
# for patient_id, date, test_result in zip(patient_ids, dates, test_result_distinct):
#     list_patient.append({"patient_id": patient_id, "date": date,
#                          "test_result": test_result})
# print(list_patient)


# def get_test_result(patient_id):
#     "this function returns the test result for a given patient_id"
#     for patient in list_patient:
#         if patient["patient_id"] == patient_id:
#             return patient["test_result"]
#     return None


# # %%
# def add_number(x, y):
#     '''this function returns the sum of two numbers
#     args: x ==> number , y==> number'''
#     return x + y


# print(add_number(5, 25))
# # %%

x, y = 5, 10


def chg_nums():
    print(x, y)


chg_nums()
print(x, y)

# %%
