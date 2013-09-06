
import os
import argparse

def write(html):
    path = '/Volumes/HD/Aaron/Library/Containers/com.evernote.Evernote/Data/Library/Application Support/Evernote/accounts/Evernote/amurdoch/content'
    
    l = os.listdir(path)
    
    def compare(a, b):
        if a.startswith('p') and b.startswith('p'):
            return -1 if int(a[1:]) < int(b[1:]) else 1
        else:
            return 1
    
    l.sort(compare)
    
    filename = os.path.join(path, l[-1])
    filename = os.path.join(filename, 'content.html')
    
    with open(filename, 'r') as f:
        s = f.read()
        
    i = s.find('</body>')
    if i == -1:
        i = s.find('<body/>')
        s = s[:i] + '<body>' + html + '</body>' + s[i+len('<body/>'):]
    else:
        s = s[:i] + html + s[i:]
    
    with open(filename, 'w') as f:
        f.write(s)
        

    


