#!/usr/bin/env python3

import pandas as pd
import argparse, json

CROWDMARK_HEADERS = {
    'Crowdmark ID',
    'Score URL',
    'Email',
    'First Name',
    'Last Name',
    'Student ID',
    'MC-total',
    'Total',
}


def details_for_student(row):
    d = {}
    for col, val in row.iteritems():
        if col == 'userid':
            d['userid'] = val
        else:
            d[col] = {'mark': row[col], 'comment': ''}
    return d


def main():
    parser = argparse.ArgumentParser(description='Convert Crowdmark "export grades" grade list to CourSys import format.')
    parser.add_argument('crowdmark_csv', help='Crowdmark "export grades" .csv file')
    parser.add_argument('activity_name', help='Short name of the CourSys activity, like "Q1"')
    parser.add_argument('--coursys-csv', default='coursys.csv', help='file to output simple CSV for CourSys, default coursys.csv')
    parser.add_argument('--coursys-json', default='coursys.json', help='file to output dubric details for CourSys, default coursys.json')
    args = parser.parse_args()

    # create simple CSV import
    grades = pd.read_csv(args.crowdmark_csv)
    out = pd.DataFrame()
    out['Userid'] = grades['Email'].str.replace('@sfu.ca', '')
    out[args.activity_name] = grades['Total']
    out.to_csv(args.coursys_csv, header=True, index=False)
    
    # create marking details
    details = pd.DataFrame({'userid': grades['Email'].str.replace('@sfu.ca', '')})
    details['multiple-choice'] = grades['MC-total']
    for col in grades:
        if col in CROWDMARK_HEADERS:
            # ignore these columns: they're special
            continue
        elif col.startswith('MC-'):
            # multiple choice component: crowdmard already summed for us
            pass
        else:
            # question grade
            details[col] = grades[col]
            
    detail_marks = details.apply(details_for_student, axis=1)
    with open(args.coursys_json, 'wt', encoding='utf-8') as out_json:
        json.dump({'marks': list(detail_marks)}, out_json)

main()


