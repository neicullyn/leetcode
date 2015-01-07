from random import randint
from ctypes.test.test_internals import ObjectsTestCase
def merge_lyn(objects_a, objects_b):
    objects = []
    
    if objects_a is not None:
        A = len(objects_a)
    else:
        A=0
    if objects_b is not None:
        B = len(objects_b)
    else:
        B=0
        
    i = 0
    j = 0
    while i < A and j < B:
        if objects_a[i] < objects_b[j]:
            objects.append(objects_a[i])
            i = i + 1
        else:
            objects.append(objects_b[j])
            j = j + 1
    while i < A:
        objects.append(objects_a[i])
        i = i + 1
    while j < B:
        objects.append(objects_b[j])
        j = j + 1
    return objects

def msort_lyn(objects):
    if len(objects)<=1:
        return objects
    else:
        m = int(len(objects) / 2)
        left = msort_lyn(objects[:m])
        right = msort_lyn(objects[m:])
        return merge_lyn(left, right)
        
        
l=[3, 7, 4, 5, 9]
l=msort_lyn(l)
print l