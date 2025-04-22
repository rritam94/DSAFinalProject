import json
from datetime import datetime

def sort_by_date(data):
    if isinstance(data, str):
        with open(data, 'r') as file:
            twitter_data = json.load(file)
    else:
        twitter_data = data
    
    def get_date(item):
        date_str = item.get('created_at')
        return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    
    def heapify_by_date(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and get_date(arr[l]) > get_date(arr[largest]):
            largest = l
            
        if r < n and get_date(arr[r]) > get_date(arr[largest]):
            largest = r
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify_by_date(arr, n, largest)
    
    def heap_sort_by_date(arr):
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            heapify_by_date(arr, n, i)
            
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify_by_date(arr, i, 0)
        
        return arr
    
    return heap_sort_by_date(twitter_data)

def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2  

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr) 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)

def sort_by_string(data):
    if isinstance(data, str):
        with open(data, 'r') as file:
            json_data = json.load(file)
    else:
        json_data = data
    
    def get_string(item):
        return item.get('name', '').lower()
    
    def heapify_by_string(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and get_string(arr[l]) > get_string(arr[largest]):
            largest = l
            
        if r < n and get_string(arr[r]) > get_string(arr[largest]):
            largest = r
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify_by_string(arr, n, largest)
    
    def heap_sort_by_string(arr):
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            heapify_by_string(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify_by_string(arr, i, 0)
        
        return arr
    
    return heap_sort_by_string(json_data)

