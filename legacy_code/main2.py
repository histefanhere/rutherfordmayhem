import json

def fullname(student):
    return f"{student['firstname']} {student['lastname']}"

with open('students.json', 'r') as file:
    students = json.load(file)

    # students.sort(key=lambda s: len(fullname(s)) )
    # for i in range(4):
    #     longest_student = students[i]
    #     print(fullname(longest_student))
    
    #lengths = {}
    #for i in range(1, 33):
    #    lengths[i] = 0

    #for s in students:
    #    lengths[len(fullname(s))] += 1

    #for i in lengths:
    #    print(f"{i}\t{lengths[i]}")

    tutor_classes = {}
    i = 0
    for s in students:
        i += 1
        try:
            tutor_classes[s['tutor']].append(s)
        except KeyError:
            tutor_classes[s['tutor']] = [s]

    print(len(tutor_classes))

    # thirteen = 0
    # for t in tutor_classes:
    #     if "13" in t:
    #         print(t)
    #         thirteen += 1
        
    # print(thirteen)

    for s in students:
        if s['tutor'] == "10BH":
            print(fullname(s))
    #for s in tutor_classes['10SL']:
    #    print(fullname(s))
    #print(max((tutor_classes[x] for x in tutor_classes)))