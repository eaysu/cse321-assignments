def find_malfunctioning_fuse(arr, index):
    if index == len(arr):
        # case of non-existing malfunctioning fuse
        return False
     
    if arr[index] == 0:
        # return index of malfunctioning fuse
        return index + 1 
    
    else:
        return find_malfunctioning_fuse(arr, index + 1) 
    
index = 0 # initializing index
fuse_arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0] # example fuses

if find_malfunctioning_fuse(fuse_arr, index):
    print(find_malfunctioning_fuse(fuse_arr, index)) 
else:
    print("all fuses are okey")             

