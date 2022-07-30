import time
import threading

class Job:
    def __init__(self):
        self.job='null'
    def setData(self,job):
        self.job =job
class counter():
    def __init__(self,limit ,active):
        self.limit  = limit 
        self.active = active

    def setLimit(self,limit):
        self.limit  =  limit
    def setActive(self,active):
        self.active  =  active    


def task():
    print("Started Task ... "+threading.current_thread().name)
    threadCount.setActive(threadCount.active+1)

    time.sleep(10)
    print("completed ....."+threading.current_thread().name)
    threadCount.setActive(threadCount.active-1)


    

def thread(args):
    threadCount.setLimit(args['session'])
    job.setData(args['job'])


    if (threadCount.limit < threadCount.active):
        return {'result': 'is busy'}

    thread = threading.Thread(target=task)
    thread.setName(job.job)
    thread.start()
    return {'result': 
        {
        'job': job.job+' Started',
        }
    }

def jobActive():
    return {'result': 
        {
        'job Active': threadCount.active,
        }
    }

threadCount = counter(0, 0)
job=Job()
