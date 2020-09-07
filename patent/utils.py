import functools
import time

from django.db import connection, reset_queries
from django.db.models import Q
from .models import Master


def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()
        
        start_queries = len(connection.queries)
        
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        
        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end-start):.2f}s")
        return result
    
    return inner_func


def tagsearch(condition, data):
    if condition == "and":
        print("here")
        if len(data) == 1:
            b = Master.objects.filter(Q(tags__icontains=data[0]))
            
        if len(data) == 2:
            b = Master.objects.filter(Q(tags__icontains=data[0]) & Q(tags__contains=data[1]))
        if len(data) == 3:
            b = Master.objects.filter(Q(tags__icontains=data[0]) & Q(tags__contains=data[1]) & Q(tags__contains=data[2]))
        if len(data) == 4:
            b = Master.objects.filter(Q(tags__icontains=data[0]) & Q(tags__contains=data[1]) & Q(tags__contains=data[2]) & Q(tags__contains=data[3]))
            
        return b
    elif condition == "or":
        print("there")
        if len(data) == 1:
            b = Master.objects.filter(Q(tags__icontains=data[0]))
            
        if len(data) == 2:
            b = Master.objects.filter(Q(tags__icontains=data[0]) | Q(tags__contains=data[1]))
        if len(data) == 3:
            b = Master.objects.filter(Q(tags__icontains=data[0]) | Q(tags__contains=data[1]) | Q(tag__contains=data[2]))
        if len(data) == 4:
            b = Master.objects.filter(Q(tags__icontains=data[0]) & Q(tags__contains=data[1]) | Q(tags__contains=data[2]) | Q(tags__contains=data[3]))
            
        return b
