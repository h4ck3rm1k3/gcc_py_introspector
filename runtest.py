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
import os.path


# Display pairs.
for pair in pairs:

    n = pair[1]
    
    
    #if not os.path.isfile("%s/%s.lasterror.txt" % (directory,n)):
    if True:
        print "running test %s" % n
        print " ".join(['python2.7', 'reader.py', "%s/%s" % (directory,n)])
        x = subprocess.call(['python2.7', 'reader.py', "%s/%s" % (directory,n)
                             #,'debug'
        ])
        print "%s %s" % (n,x)
        os.rename('lasterror.txt',"%s/%s.lasterror.txt" % (directory,n))
        if os.path.isfile('nodes.pickle') :
            os.rename('nodes.pickle',"%s/%s.nodes.pickle" % (directory,n))
        if x == 0:
            print "OK"
        else:
            print "fail"

    else:
        print "skipping test %s" % n
              
    #python load_pickle.py

