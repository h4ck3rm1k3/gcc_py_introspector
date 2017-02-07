import os
import sys
# The folder containing files.
directory = sys.argv[1]
print 'going to read %s' % (directory)

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


# Display pairs.
for pair in pairs:

    n = pair[1]
    print "running test %s" % n
    x = subprocess.call(['python', 'reader.py', "%s/%s" % (directory,n)
                         #,'debug'
    ])
    os.rename('lasterror.txt',"%s/%s.lasterror.txt" % (directory,n))
    os.rename('nodes.pickle',"%s/%s.nodes.pickle" % (directory,n)
    
    print n,x
    if x == 0:
        print "OK"
    else:
        raise Exception("fail")
    #python load_pickle.py

