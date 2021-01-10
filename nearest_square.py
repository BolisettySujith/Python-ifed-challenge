def nearest_square(num):
    initial =0
    something = (initial+1)**2
    while something <= num:
        initial += 1
    return something