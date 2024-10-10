def linear_search(arr:list, target:str) -> int: 
    for i in range(len(arr)):
        if arr[i] == target: 
            return i
    return None

def verify_search(input: None | int) -> None:
    if (input == None): 
        return "Nothing was found"
    
    return "Something was found"
        

samp_list = ["hello", "hi", "hola"]
print(linear_search(samp_list, "hi"))
print(linear_search(samp_list, "hola"))
print(linear_search(samp_list, "this not found"))