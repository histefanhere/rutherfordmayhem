# Rutherford Mayhem

In 2015 Rutherford College played a school-wide game called _mayhem_, where every student got a card with another students name. Once they found this person they stole their card, all other cards they've collected, and continue finding the next person. The student with the most cards at the end wins.

Inspired by this, in 2019 we replayed this game and I was in charge of organizing it, so here's the code for generating these cards. It takes a *csv input file* of all the students in the school and some info of them like their name and ID (this file was provided by a teacher of the school), and outputs a printable PDF of all the cards.

## Hey my school plays this game too!

Do they? Awesome! So far I've only heard of one other school that does something like this, so if you know what the game's actually called or have any other information about the game, contact me

## Installation

there's a couple things you need to get this setup - the most important is [Python 3](https://www.python.org/). You'll also need [wkhtmltopdf](https://wkhtmltopdf.org/index.html) which is what the script uses to generate the PDF. Installation of this varies from system to system, so if something isn't working please feel free to contact me.

You'll also need the `pdfkit` python package, which is a wrapper for `wkhtmltopdf`
```bash
# Which command to use depends on your system
python3 -m pip install pdfkit
python -m pip install pdfkit
```

And it goes without saying that you need `students.csv` - a CSV file of all the students in the school and various metadata about them. This file can be obtained by sufficiently nagging the teachers of the school :)

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

Now we need to generate the PDF, and for this there are a handful of template files that you should first configure to suit your needs, and you can find these in `files`. Now just run

```bash
python3 main_pdf.py
```

and - that's it! If everything worked as it should, you should see an output `print.pdf` file with all the cards for all students in a printable format, all sorted by tutor class.

## Uhhh, yeah how do I use this?

This was a rough overview. If you're serious about playing this game, contact me for more information and I'll help you with brining mayhem to your school ;).
