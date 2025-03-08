# Calculate the mean of a vector

x = list(range(0, 10, 1))

def get_mean(data):
   return sum(data) / len(data)

get_mean(x)

# Calculat the median
def get_median(data):
    """
    Calculates the median of a list of numbers

    Args:
        data (_type_): a list of numbers
        
    Returns:
        The median for a series.    
        
    """
    sorted_data = sorted(data) # Sorts the list of numbers
    n = len(sorted_data) # calculates the length
    mid_index = n // 2 # Floor division to get the middle index
    if n % 2 == 0:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
    else:
        return sorted_data[mid_index]

get_median(x)