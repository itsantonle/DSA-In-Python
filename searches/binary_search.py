def binary_search(list:list, target:str) -> int:
    first = 0
    last = len(list) - 1
    
    while(first <= last): 
        midpoint = (first + last) // 2 # alternatively use Math.floor()
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
            
        elif list[midpoint] > target: 
            last = midpoint - 1
            
    return None

#   the sample code must be sorted
            
samp_list = ["hello", "hi", "hola"]
print(binary_search(samp_list, "hi"))
print(binary_search(samp_list, "hola"))
print(binary_search(samp_list, "this not found"))
        