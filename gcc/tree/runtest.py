import os
import sys
# The folder containing files.
directory = sys.argv[1]
print(('going to read %s' % (directory)))

# Get all files.
list = os.listdir(directory)

# Loop and add files to list.
pairs = []
for file in list:

    if (file.endswith(".tu") or file.endswith(".t")) and '#' not in file:
        # Use join to get full file path.
        location = os.path.join(directory, file)

        # Get size and add to list of tuples.
        size = os.path.getsize(location)
        pairs.append((size, file))

# Sort list of tuples by the first element, size.
pairs.sort(key=lambda s: s[0])
import subprocess
import os.path


# Display pairs.
import time
from threading import Thread

def proc(n):
    print ("running test %s" % n)
    print (" ".join(['python3', './test.py', "%s/%s" % (directory,n)]))
    x = subprocess.call(['python3', './test.py', "%s/%s" % (directory,n)
                         #,'debug'
    ])
    print ("%s %s" % (n,x))

    if os.path.isfile('lasterror.txt') :
        os.rename('lasterror.txt',"%s/%s.lasterror.txt" % (directory,n))

    if os.path.isfile('Nodes.nodes.pickle') :
        os.rename('Nodes.nodes.pickle',"%s/%s.nodes.pickle" % (directory,n))
    else:
        raise Exception('missing pickle')
    
    if x == 0:
        print ("OK")
    else:
        print ("fail")
            
for pair in pairs:

    n = pair[1]
    t = Thread(target=proc, args=(n,))
    t.start()
     
