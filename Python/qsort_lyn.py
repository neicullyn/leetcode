from random import randint
def qsort_lyn(objects, left_index, right_index):
    n = right_index - left_index
    if n <= 1:
        pass
    elif n == 2:
        if objects[left_index] > objects[left_index+1]:
            objects[left_index], objects[left_index+1] = objects[left_index+1], objects[left_index]
    else:        
        pivot_index = randint(left_index, right_index-1)
        pivot_value = objects[pivot_index]
        objects[pivot_index], objects[right_index-1] = objects[right_index-1], objects[pivot_index]
        store_index = left_index
        for i in range(left_index, right_index-1):
            if objects[i] < pivot_value:
                objects[i], objects[store_index] = objects[store_index], objects[i]
                store_index = store_index + 1
        objects[store_index], objects[right_index-1] = objects[right_index-1], objects[store_index]
        qsort_lyn(objects, left_index, store_index)
        qsort_lyn(objects, store_index+1, right_index)

l=[3, 7, 4, 5, 9]
qsort_lyn(l, 0, len(l))
print l