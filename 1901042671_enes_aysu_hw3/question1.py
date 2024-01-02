def find_max_discount(store_list, current_index, current_set, max_discount_set):
    if current_index == len(store_list):

        # Calculate discount for the current set of stores (assume that clac_discount is implemented)
        current_discount = calc_discount(current_set)
        
        # Update max_discount_set if the current set yields a higher discount (assume that clac_discount is implemented)
        if current_discount > calc_discount(max_discount_set):
            max_discount_set = current_set.copy()
        return max_discount_set
    
    # Explore including the current store
    max_discount_set = find_max_discount(store_list, current_index + 1, current_set + [store_list[current_index]], max_discount_set)
    
    # Explore excluding the current store
    max_discount_set = find_max_discount(store_list, current_index + 1, current_set, max_discount_set)
    
    return max_discount_set
