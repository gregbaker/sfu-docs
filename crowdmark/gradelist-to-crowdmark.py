#!/usr/bin/env python3

import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser(description='Convert CourSys "all grades" grade list to data for Crowdmark.')
    parser.add_argument('grades_csv', help='CourSys "all grades" .csv file')
    parser.add_argument('--email-list', default='emails.txt', help='file to output text list of email addresses, default emails.txt')
    parser.add_argument('--metadata', default='metadata.csv', help='file to output Crowdmark metadata data, default metadata.csv')
    args = parser.parse_args()

    grades = pd.read_csv(args.grades_csv)
    emails = pd.DataFrame()
    emails['email'] = grades['First name'] + ' ' + grades['Last name'] + ' <' + grades['Userid'] + '@sfu.ca>'
    emails.to_csv(args.email_list, header=False, index=False, sep='!')
    
    metadata = pd.DataFrame()
    metadata['Email'] = grades['Userid'] + '@sfu.ca'
    metadata['First Name'] = grades['First name']
    metadata['Last Name'] = grades['Last name']
    metadata['Student ID'] = grades['ID Number']
    metadata.to_csv(args.metadata, header=True, index=False)


main()


