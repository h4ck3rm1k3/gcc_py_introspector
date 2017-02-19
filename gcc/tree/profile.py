from memory_profiler import memory_usage
import resource
import cProfile
import pstats

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    
lastusage=(0,0,0)
pr = cProfile.Profile()
pr.enable()

def memprofile(point):
    #mem_usage = memory_usage(-1, interval=.2, timeout=1)
    global pr
    pr.disable()
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    pr.create_stats()
    
    print (s.getvalue())
    pr = cProfile.Profile()
    pr.enable()


    #point = 'test'
    global lastusage
    point = 'reader'
    usage=resource.getrusage(resource.RUSAGE_SELF)
    print ("%s:usertime=%0.3f systime=%0.3f pages=%d"  % (
        point,
        usage[0]-lastusage[0],
        usage[1]-lastusage[1],
        usage[2] -lastusage[2]
    ))
    #print(mem_usage)
    lastusage = usage
