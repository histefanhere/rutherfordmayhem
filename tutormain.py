import json
import random

import pdfkit

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
        with open(filename, 'r') as file:
            file_cache[filename] = file.read()
    return file_cache[filename]

# Get the students.json file that the generate_json.py file creates
with open('students.json', 'r') as file:
    students = json.load(file)

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
        output += get_file("files/card_template.html").format(**data)
        i += 1

    output += "</tr></table>"

output += '<h3>Instructions:</h3><table width="100"><tr>'
for i in range(50):
    if i % 3 == 0 and i != 0:
        output += '</tr><tr class="keep-together">'
    output += '''
        <td style="padding: 3px; font-size: 0.7rem">
            Give these slips to your students, if a student isn't present keep their slip with you
            (So if someone comes looking for this student you can give them their next slip).
            Once found, a student must give all their collected slips to their finder.
            <span style="font-weight: 600">Students must keep all slips with them throughout the week!</span>
            Good luck! :)
        </td>
    '''
output += '</tr></table>'

# Import all the styling into the output
output += f"<style>{get_file('staticfiles/style.css')}</style>"
output += f"<style>{get_file('staticfiles/stylesheet.css')}</style>"

# And finally, finish it up!
output += '</body></html>'


with open('index.html', 'w+') as file:
    file.write(output)
options = {
    'print-media-type': None,
    'enable-local-file-access': None,

    # These should all be on by default, but there's no harm in specifying them right?
    'images': None,
    'resolve-relative-links': None

#    'quiet': None
}

# Create the HTML in pdf form
# pdfkit does offer to create a pdf from string, however it wouldn't load images from local directories this way.
# pdfkit.from_string(output, 'print.pdf', options = options)
pdfkit.from_file('index.html', 'print.pdf', options = options)


# Relics from a past life
# from fpdf import FPDF, HTMLMixin
# class HTML2PDF(FPDF, HTMLMixin):
#     pass
# pdf = HTML2PDF()
# for i in range(100):
#     pdf.add_page()
# pdf.write_html(output)
# pdf.output('html2pdf.pdf')

# https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
# https://wkhtmltopdf.org/downloads.html

# https://www.google.com/search?hl=en&q=The%20switch%20%2D%2Dprint%2Dmedia%2Dtype%2C%20is%20not%20support%20using%20unpatched%20qt%2C%20and%20will%20be%20ignored.qt5ct%3A%20using%20qt5ct%20plugin
# https://stackoverflow.com/questions/34479040/how-to-install-wkhtmltopdf-with-patched-qt
# https://gist.github.com/tejastank/45b6eba13fb38e24110218e3ce50129b

