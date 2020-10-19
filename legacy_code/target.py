import json

students = []
with open('students.json', 'r') as file:
    students = json.load(file)

with open('students.json', 'w+') as file:
    i = 0
    while i < len(students):
        students[i]['target'] = students[(i+1)%len(students)]['id']
        i += 1

    json.dump(students, file, indent=4)