import csv
import random
import json
import argparse

students = []
total_students = 0

# Parse the provided command-line arguments
parser = argparse.ArgumentParser()

parser.add_argument('--no-sim', action='store_true', help="Actually creates the output files, not just run a simulaton.")
parser.add_argument('--disable-first-tutor-filter', action='store_true', help="Disable first tutor filtering")
parser.add_argument('--exclude-tutors', nargs='+', metavar="TUTORS", help="Tutor Classes to be excluded from Mayhem.")
parser.add_argument('--exclude-students', nargs="+", metavar="STUDENT_IDS", help="Student IDs to be excluded from Mayhem.")
args = parser.parse_args()

if args.no_sim:
    print("The program will run in real-mode and actually create all the output files")
else:
    print("The program will run in simulation mode and not create any new files.")

excluded = 0
exclude = []
if args.exclude_tutors:
    exclude = args.exclude
    print("The program will exclude the following tutor class{}: {}".format("es" if len(exclude) > 1 else "", ' '.join(exclude)))

if args.exclude_students:
    exclude.extend(args.exclude_students)
    print("The program will exclude the following student{}: {}".format("s" if len(args.exclude_students) > 1 else "", ' '.join(args.exclude_students)))

if args.disable_first_tutor_filter:
    print("I've been given the disable first tutor flag. This means that a students first target could be in his very own tutor class, INSTANTLY taking them out of the game. You evil, evil man.")

# Just gives the user an opportunity to read all the messages
input("(Press enter to continue, or Ctrl+C to cancel)")

# Read the students.csv file provided by staff and convert it into a JSON for easier manipulation
with open('students.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        if row['Tutor'] not in exclude and row['IDNumber'] not in exclude:
        # if row['Tutor'] in ('13CH'):
            students.append({
                'id': row['IDNumber'],
                'firstname': row['Firstname'],
                'lastname': row['Lastname'],
                'year': row['Year'],
                'tutor': row['Tutor'],
                'type': row['Type']
            })
            total_students += 1
        else:
            print("Excluding {} {}, {}, {}".format(row['Firstname'], row['Lastname'], row['Tutor'], row['IDNumber']))
            excluded += 1
    print('\n---------------------\n')
    print(f'Total students excluded: {excluded}')
    print(f'Total students: {total_students}')

# Randomize the order of the students in such a way that no one's first target will be in their own tutor class
# Yeah don't ask me how this works, I have no idea anymore.
output_students = [students.pop()]
attempts = 0
while len(output_students) < total_students:
    attempts += 1
    i = random.randint(0, len(students)-1)
    if not args.disable_first_tutor_filter and output_students[-1]['tutor'] == students[i]['tutor']:
        if attempts > 100:
            print("Okay so there is a VERY small chance that this program will never finish, and it looks like you got it! If that's the case, which it is, do Ctrl+C to kill the program and re-run it. :)")
            exit()
        continue
    else:
        attempts = 0
        output_students.append(students.pop(i))

# Give each student a reference to their target's ID
i = 0
while i < len(output_students):
    output_students[i]['target'] = output_students[(i+1)%len(output_students)]['id']
    i += 1

# Write the final list of students to the students.json file
if args.no_sim:
    with open('students.json', 'w+') as file:
        json.dump(output_students, file, indent=4)
        print("File students.json has been created")

print("Done!")
