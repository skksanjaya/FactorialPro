import numpy as np

def tot_rainfall(tot_arr):
    return np.sum(tot_arr) 

def avg_rainfall(avg_arr):
    return np.mean(avg_arr)   

def count_zero(zero_arr):
    return np.size(np.where(zero_arr==0))  

def more_than(than5_arr,val):
    return np.where(than5_arr>val) 

def percentile_value(percentile_arr, percentile_val):
    return np.percentile(percentile_arr,percentile_val)  


if __name__ == "__main__":

    rain_info = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

    rain_array = np.array(rain_info)

    print(rain_array)

    print(tot_rainfall(rain_array))

    print(avg_rainfall(rain_array))

    print(count_zero(rain_array))

    print(more_than(rain_array,5))

    print(percentile_value(rain_array,75))

    print(more_than(rain_array,percentile_value(rain_array,75)))


