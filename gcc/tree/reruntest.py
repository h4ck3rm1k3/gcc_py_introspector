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

    if (file.endswith(".txt") ) and '#' not in file:
        location = os.path.join(directory, file)
        size = os.path.getsize(location)
        if size > 0:
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
        print ("running test %s" % n)
        print (" ".join(['python3', 'reader.py', "%s/%s" % (directory,n)]))
        x = subprocess.call(['python3', 'reader.py', "%s/%s" % (directory,n)
                             ,'debug'
        ])
        print ("%s %s" % (n,x))
        #os.unlink('lasterror.txt',"%s/%s.lasterror.txt" % (directory,n))

        if x == 0:
            print ("OK")
        else:
            print ("fail")
            raise Exception("err")

    else:
        print ("skipping test %s" % n)

