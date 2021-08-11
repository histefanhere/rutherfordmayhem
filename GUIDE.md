# Rutherford Mayhem Guide

This is a detailed guide on how to properly get mayhem up and running, and covers everything from getting your computer environment ready to advice on how to organize everything irl.

## Table of Contents

- [Prerequisites](#prerequisites)
    - [Python](#python)
    - [pdfkit](#pdfkit)
    - [Students file](#students-file)
- [Setup](#setup)
    - [Download the repository](#download-the-repository)
    - [Move students.csv](#move-students.csv)
- [Usage](#usage)

## Prerequisites

### Python
This one's kinda a no brainer, but you need to install [Python 3](https://www.python.org/) and be able to call it from the command line, with either `python` or `python3` depending on your system. You'll need this because the scripts need to be passed flags and arguments through their commands.

### pdfkit
This python library is what the scripts use to generate a printable pdf from an html file. It also requires you to install `wkhtmltopdf` which is what the library is a wrapper for, for which system-specific installation instructions can be found [here (pdfkit wiki).](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf) NOTE: DON'T FORGET TO ADD IT TO YOUR PATH! If you've installed it correctly, you should be able to call the `wkhtmltopdf` command from the command prompt. Once you have that installed, simply install pdfkit as you would a normal python package:
```bash
# Which command to use depends on your system
python3 -m pip install pdfkit
python -m pip install pdfkit
```

### Students file
For the script to run, it needs to know the names of all the students at the school, a file called `students.csv`. It *needs* to have the following headers:
- IDNumber
- Firstname
- Lastname
- Year
- Tutor
- Type
So the start of the file should look something like:
```csv
IDNumber,Firstname,Lastname,Year,Tutor,Type
1,Stefan,Zdravkovic,13,13CH,Domestic
2,Bob,Roberts,10,10XY,Domestic
...
```
The database system that the school uses should be able to generate this file, so kindly ask the staff of the school for a list of all the students! (When we played it, Mrs Farrar knew how to do it).

## Setup

### Download the repository

Download the files from this repo as a zip and extract them. Easy enough, right?

### Move students.csv

Move the `students.csv` file into the root of the repository, so all the scripts can access it. Boom, you're ready to rock!

## Usage

_Confused at any step in the process? All scripts have a help you can find by running `python3 filename.py --help`_

Firstly we need to parse the `students.csv` input file and generate a `json` file that represents the chain of students in the game.

```bash
# Observe the output is as expected
python3 generate_json.py
# Actually create the file
python3 generate_json.py --no-sim
```

**IMPORTANT: SAVE THIS OUTPUT `students.json` FILE.** It represents the offical order of students in the game and who's targetting who - if you lose this file, and someone can't find their target, you'll have no idea who they should be looking for instead.

Now we need to generate the PDF, and for this there are a handful of template files that you should first configure to suit your needs, and you can find these in `templates`. Now just run

```bash
python3 main_pdf.py
```

and - that's it! If everything worked as it should, you should see an output `print.pdf` file with all the cards for all students in a printable format, all sorted by tutor class.
