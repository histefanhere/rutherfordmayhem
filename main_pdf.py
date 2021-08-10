##############
# FILENAME:    main_pdf.py
# DESCRIPTION: Create a printable PDF from the processed JSON file.
#              this should be the SECOND program you run.
# AUTHOR:      Stefan Zdravkovic
# DATE:        22/10/2020
##############


import argparse
import json
import random

import pdfkit

# Parse the provided command-line arguments
parser = argparse.ArgumentParser()

parser.add_argument('-i', '--no-instructions', dest="no_instructions", action='store_true', help="dont print out instruction slips for each tutor")
args = parser.parse_args()

# Setting up the final html output
output = "<html><body>"

# Some useful utility functions
def fullname(student):
    return f"{student['firstname']} {student['lastname']}"

def get_student(id):
    for s in students:
        if s['id'] == id:
            return s

file_cache = {}
def get_file(filename):
    if not filename in file_cache:
        try:
            with open(filename, 'r') as file:
                file_cache[filename] = file.read()
        except FileNotFoundError:
            print(f"ERROR: I couldn't seem to find the file {filename}. Do you know where it is?")
            exit()
    return file_cache[filename]

# Get the students.json file that the generate_json.py file creates
try:
    with open('students.json', 'r') as file:
        students = json.load(file)
except FileNotFoundError:
    print("ERROR: where the heck is students.json!? please run generate_json.py first then run this script.")
    exit()

# And sort them by tutor class
tutor_classes = {}
for s in students:
    try:
        tutor_classes[s['tutor']].append(s)
    except KeyError:
        tutor_classes[s['tutor']] = [s]

# Start generating the output...
for tutor, group in tutor_classes.items():
    output += f"<h3>{tutor}</h3><table width='100'>"

    i = 0
    output += "<tr class=\"keep-together\">"
    while i < len(group):
        if i % 3 == 0 and i != 0:
            output += "</tr><tr class=\"keep-together\">"

        student = group[i]
        target = get_student(student['target'])
        data = {
            "FIRSTNAME": student['firstname'],
            "LASTNAME": student['lastname'],
            "FULLNAME": fullname(student),
            "TUTOR": student['tutor'],
            "YEAR": student['year'],

            "FIRSTNAME_TARGET": target['firstname'],
            "LASTNAME_TARGET": target['lastname'],
            "FULLNAME_TARGET": fullname(target),
            "TUTOR_TARGET": target['tutor'],
            "YEAR_TARGET": target['year'],
        }
        output += get_file("templates/card_template.html").format(**data)
        i += 1

    output += "</tr></table>"

# Don't include the instructions if we're told not too
if not args.no_instructions:
    output += '<h3>Instructions:</h3><table width="100"><tr>'
    for i in range(4):
        if i % 3 == 0 and i != 0:
            output += '</tr><tr class="keep-together">'
        output += get_file('templates/instructions_template.html')
    output += '</tr></table>'
else:
    print("There will be NO instruction sheets")

# Import all the styling into the output
output += f"<style>{get_file('staticfiles/stylesheet.css')}</style>"

# And finally, finish it up!
output += '</body></html>'

print("\nThe PDF is about to be generated. Any output from this point onwards is from the PDF generator")
input("(Press enter to continue)\n")

with open('index.html', 'w+') as file:
    file.write(output)
options = {
    'print-media-type': None,
    'enable-local-file-access': None,

    # These should all be on by default, but there's no harm in specifying them right?
    'images': None,
    'resolve-relative-links': None
}

# Create the HTML in pdf form
# pdfkit does offer to create a pdf from string, however it wouldn't load images from local directories this way.
# pdfkit.from_string(output, 'print.pdf', options = options)
pdfkit.from_file('index.html', 'print.pdf', options = options)
