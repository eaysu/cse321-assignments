def find_bright_pixel(x, y, arr):
    if check_brightest(x, y, arr):
        return x, y
    
    if x >= len(arr[0]):
        if y >= len(arr):
            # case of out of borders
            return False
        else:
            # iterating through 
            return find_bright_pixel(0, y + 1, arr)
        
    else:
        return find_bright_pixel(x + 1, y, arr)

def check_brightest(x, y, arr):
    # edges don't have 4 neighbours
    if x + 1 >= len(arr[0]) or x - 1 < 0 or y + 1 >= len(arr) or y - 1 < 0:
        return False

    # finding unique brightest pixel
    return (arr[y][x] > arr[y-1][x] and 
            arr[y][x] > arr[y+1][x] and 
            arr[y][x] > arr[y][x-1] and 
            arr[y][x] > arr[y][x+1])

# starts from top-left corner of matrix
x = 0
y = 0

# 2d grid of pixels
pixels_2d =[ [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0] ]

if find_bright_pixel(0, 0, pixels_2d):
    print(find_bright_pixel(x, y, pixels_2d)) 
else:
    print("uniqe brightest pixel doesn't exist")    