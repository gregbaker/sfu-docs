#!/usr/bin/env python3

import argparse, tempfile, sys
import PyPDF2


def main():
    parser = argparse.ArgumentParser(description='Rotate PDF documents 180 degrees.')
    parser.add_argument('pdf', nargs='+', help='PDF document(s) to rotate')
    args = parser.parse_args()
    
    for pdf in args.pdf:
        sys.stderr.write('Processing %s...\n' % (pdf,))
        with tempfile.TemporaryFile() as tmp:
            with open(pdf, 'rb') as indata:
                reader = PyPDF2.PdfFileReader(indata)
                writer = PyPDF2.PdfFileWriter()
            
                for pagenum in range(reader.numPages):
                    page = reader.getPage(pagenum)
                    page.rotateClockwise(180)
                    writer.addPage(page)
            
                writer.write(tmp)
        
            tmp.seek(0)
            with open(pdf, 'wb') as outdata:
                outdata.write(tmp.read())
        

main()
