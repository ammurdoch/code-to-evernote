import json
import re
import argparse
import os

def convert(stylesheet):

    with open(stylesheet, 'r') as f:
        s = f.read()
    r1 = 'pre '
    r2 = '[^pre]{3}\S*[ ,] ?'
    r3 = '[ {]'
    
    r = '[\S][.\w \-]* ?[,{]{1}'
    
    classes = {}
    selectors = re.findall(r, s)
    
    for sel in selectors:
        i = s.find(sel)
        i = s.find('{', i)
        j = s.find('}', i)
        sel = sel.replace('pre ', '').replace(' {', '').replace('.', '').replace(',', '')
        style = s[i+1:j].replace('\n', '')
        classes[sel] = style
    
    with open(stylesheet.replace('.css', '.json'), 'wb') as f:
        f.write(json.dumps(classes))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert css to json dictionary')
    parser.add_argument('stylesheet', type=str, help='The file to convert')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.stylesheet):
        raise(Exception('"%s" does not exist' %(args.stylesheet)))
    
    convert(args.stylesheet)


