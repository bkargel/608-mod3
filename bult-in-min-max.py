"""Return the maximum of three values."""

def maximum(value1,value2, value3):
    
    max_value = value1
    if value2>max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

maximum(12, 27, 36)

"""Return the minimum of four values."""
def minimum(value1,value2, value3, value4):

    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    if value4 < min_value:
        min_value = value4
    return min_value

minimum(15, 9, 27, 14)

