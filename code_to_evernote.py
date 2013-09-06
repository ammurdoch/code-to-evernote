#!/usr/bin/python

import argparse
import code_2_html
import html_to_evernote
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert code to html with syntax highlighting and insert it into the most recent Evernote note')
    parser.add_argument('file', type=str, help='The file to highlight and convert')
    parser.add_argument('-l', '--language', dest='language', help="the language of the code you're highlighting")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        raise(Exception('"%s" does not exist' %(args.file)))
    
    html = code_2_html.convert(args.file, args.language)
    html_to_evernote.write(html)    



