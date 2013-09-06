#!/usr/bin/python

import subprocess
import os
import argparse
import json
import re


def convert(code_filename, language=None):
    
    if language:
        print language
        s = subprocess.check_output(('node', 'codeToHtml.js', code_filename, language))
    else:
        s = subprocess.check_output(('node', 'codeToHtml.js', code_filename))
    
    json_stylesheet = '../highlight.js/src/styles/tomorrow-night-eighties.json'
    with open(json_stylesheet, 'rb') as f:
        classes = json.loads(f.read())
        
        i = s.find('class="')
        j = s.find('"', i)
        k = s.find('"', j+1)
        
        while i >= 0:
            cls = s[j+1:k]
            print s[i:k+1]
            try:
                style_str = classes[cls]
            except KeyError:
                style_str = ''
            
            s = s.replace(s[i:k+1], 'style="%s"'%(style_str))
            
            i = s.find('class="')
            j = s.find('"', i)
            k = s.find('"', j+1)           
            
    html_fname = re.sub('[.]\w*$', '.html', code_filename)
    html = '<code style="%s"><pre>\n' %(classes['code'])
    html += s
    html += '</pre></code>'
    
    with open(html_fname, 'wb') as f:
        f.write('<html><body>\n' + html + '\n</body></html>')
        
    return html

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert code to html with syntax highlighting')
    parser.add_argument('file', type=str, help='The file to highlight and convert')
    parser.add_argument('-l', '--language', dest='language', help="the language of the code you're highlighting")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        raise(Exception('"%s" does not exist' %(args.file)))
    
    convert(args.file, args.language)

