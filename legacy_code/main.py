import json, pdfkit, random

output = "<html><body><table>"

def fullname(student):
    return f"{student['firstname']} {student['lastname']}"

def get_student(id):
    for s in students:
        if s['id'] == id:
            return s

with open('mixed_students.json', 'r') as file:
    students = json.load(file)
    students.sort(key=lambda s: s['tutor'])
    total_students = len(students)
    i = 0
    output += "<tr>"
    while i < len(students):
        if i % 4 == 0 and i != 0:
            output += "</tr><tr class=\"keep-together\">"
        #if i % 100 == 0:
            #output += "<div class=\"new-page\">foo</div>"
        output += f'''
        <td class=\"keep-together\">
            <img src="C:\\Users\\stefa\\Desktop\\rutherford mayhem\\kotuku.png" width="26" height="21">
            <span id="rutherford">Rutherford Mayhem 2019</span>
            <span id="first_name">{fullname(students[i])},</span><br>
            <span id="find">find</span><br>
            <span id="final_name">{fullname( get_student(students[i]['target']) )}</span>
        </td>'''
        i += 1

output += '''</table></body><style>
#first_name {
}
#find {
}
#final_name {
    font-weight: 800
}
table, td {
    border: 1px solid black;
    border-collapse: collapse;
    text-align: center;
    font-family: 'Verdana'
}
td {
    padding: 7px 3px 17px 3px;
}
@media print {
  .new-page {
    page-break-before: always;
  }
}
@media print {
    .keep-together {
        page-break-inside: avoid;
    }
}
.keep-together {
    position: relative;
}
.keep-together > img {
    position: absolute;
    left: 0;
    bottom: 0;
}
#rutherford {
    position: absolute;
    bottom: 0;
    right: 0;
    font-size: 0.6em;
    color: #bbb;
    font-family: 'Veranda';
}
</style></html>'''
with open('index.html', 'w+') as file:
    file.write(output)
options = {
    'print-media-type': None,
    'quiet': None
}
pdfkit.from_string(output, 'print.pdf', options = options)