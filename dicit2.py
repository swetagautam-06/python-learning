# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hero": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grades ={}
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "outstanding"
#     elif score > 80:
#         student_grades[student] = "excellent"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "fail"
# print(student_grades)

#Nested distionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#nesting dictionary in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log)