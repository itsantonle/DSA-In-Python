def recursive_binary_search(list, target): 
    if len(list) == 0: 
        return False
    else: 
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target: 
                recursive_binary_search(list[midpoint +1:], target)
            elif list[midpoint] > target: 
                recursive_binary_search(list[:midpoint], target)
                
    # basically making a smaller sublist that if target is not found will have
    # a length of zero