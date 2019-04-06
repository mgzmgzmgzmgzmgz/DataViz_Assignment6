
def make_zero_array(num):
    arr = []
    for i in range(0, num):
        arr.append(0)
    return arr

def linear_interp(arr, pos):
    first = arr[0]
    last = arr[len(arr)-1]
    num_elem_between = len(arr) - 2
    return (first * (((len(arr)-1) - pos) / (num_elem_between + 1))) + (last * (pos / (num_elem_between + 1)))


def bilinear_inter(top_arr, bottom_arr, x_pos, y_pos):
    top_horz_val = linear_interp(top_arr, x_pos)
    bottom_horz_val = linear_interp(bottom_arr, x_pos)
    vert_top_down_array = make_zero_array(len(top_arr))
    vert_top_down_array[0] = top_horz_val
    vert_top_down_array[len(vert_top_down_array)-1] = bottom_horz_val
    return linear_interp(vert_top_down_array, y_pos)

