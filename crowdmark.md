# Using CrowdMark in CS

SFU (or CS?) had a subscription to [CrowdMark](https://crowdmark.com/) and we can use it for exams in the School.

## Getting Started

Instructors can start by going to [to SFU sign-in page](https://app.crowdmark.com/sign-in/sfu) and linking their SFU account to CrowdMark. You can continue to sign in this way, or do a password reset and set a password so you can use their normal log-in page.

Overall, the [CrowdMark help](https://crowdmark.com/help/) is very good, and I won't replicate it here.

## Creating Your Exam

See the CrowdMark help on [creating an assessment template](https://crowdmark.com/help/creating-an-assessment-template/) for details, but the most critcal detail is to leave a 1.5&Prime; top margin for CrowdMark to do its thing. I do it like this in LaTeX:

```latex
\documentclass[11pt, letterpaper]{article}
\usepackage[top=1.5in,bottom=0.8in,left=0.8in,right=0.8in]{geometry}
```

On your cover page, leave the 3.5&Prime; gap for their name entry boxes: optional but worth it.

Create an &ldquo;administered&rdquo; assessment, turn on &ldquo;automated matching&rdquo; for student names, and drop in your PDF.

## Student Data

CrowdMark needs a list of students and their emails, and if you're doing the name matching, metadata with their names and student numbers.

I have a written a quick program [gradelist-to-crowdmark.py](crowdmark/gradelist-to-crowdmark.py) that takes a CourSys grade CSV (&ldquo;Display All Grades&rdquo; &rarr; &ldquo;Export CSV&rdquo;) and produces `emails.txt` that you can copy-and-paste as the list of students, and `metadata.csv` that can be uploaded as student metadata.

## Duplicating

CrowdMark will produce a big PDF document with booklets for each student (plus a few extra). You can ask the Undergrad Program Assistant to have the exam copied at Document Solutions: as long as they are told to staple in batches of *n* pages, they will.

It's theoretically possible to break the big PDF up, and send each booklet as a separate print job with stapling turned on. This is left as an exercise to the reader.

## Scanning



## To CourSys

Once you export your grades from CrowdMark, my [crowdmark-to-coursys.py](crowdmark/crowdmark-to-coursys.py) will get them into a format that will import into CourSys. It will produce `coursys.csv` if you want to simply upload the grades for the activity.

The `coursys.json` that is produced can be uploaded as a &ldquo;marking detail&rdquo; rubric, as long as you set up the rubric to match the questions in CrowdMark.





