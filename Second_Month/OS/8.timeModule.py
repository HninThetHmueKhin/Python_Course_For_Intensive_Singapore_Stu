import time

def myFun(fn,*args,rep=1,**kwargs):
    start = time.perf_counter()
    print("Starting time",start)
    for i in range(rep):
        fn(*args,**kwargs)
    end = time.perf_counter()
    print("Ending time",end)
    avgTime = (end-start)/rep
    fn(avgTime)
if __name__ == '__main__':
    myFun(print,1,2,3,rep=5,sep="-",end="***\n")