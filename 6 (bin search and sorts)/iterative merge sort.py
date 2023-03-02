from queue import Queue
def iterative_merge_sort(arr:list)->list:
    a = Queue()
    for i in range(0,len(arr)-1):
        a.put([arr[i]])
    while a.qsize()>1:
        a.put(merge(a.get(),a.get()))
    return a.get()