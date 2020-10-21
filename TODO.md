# TODO:

- What are exactly the dependencies I need??

- Delete useless code / Put cool stuff into seperate scripts

- explore other additional output formats - csv?

- very verbosly print out exlcusioned tutors or students

- combine stylesheets

- errors

# COMPLETED:

- CLI option for generating or not generating the instruction slips?
- Write very detailed README
    - https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
- (proper) script headers
- CLI option for same-tutor exclusion
- Does tutormain.py need to generate the target_students.csv?
- Run tutormain.py, see error about wkhtmltopdf and install to laptop
- Difference between main.py and tutormain.py?????
- Merge target.py into convert_into_csv.py so only the one code needs to be run to generate the propper .json file
- Tries counter in convert_to_csv.py for generating random sequence with same-tutor exlusion
- Argparse in convert_to_csv.py to pass classes/students that need to be excluded

- Put all the HTML and CSS into an external file
    - Proper f-strings in html file

# TRASHED:

- Put everything into _one_ python script???
- `output` folder so inputs and outputs and code don't get mixed around
- Argparse for tutormain.py
