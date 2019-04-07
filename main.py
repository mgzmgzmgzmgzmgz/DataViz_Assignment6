import functions_file as ff


image_path = "/Users/micahgiles/Desktop/Inner_Desktop/UAB_Spring_19/Data_Visualization/Assignment_6/brain_128_128.raw"

image_path_2 = "/Users/micahgiles/Desktop/Inner_Desktop/UAB_Spring_19/Data_Visualization/Assignment_6/NN_brain_128_128.raw"

pre_im_2 = open(image_path_2, 'rb')
im2 = pre_im_2.read()

print(len(im2))

pre_im = open(image_path, 'rb')

brain_image = pre_im.read()
# print(brain_image)

print("length of original array")
print(len(brain_image))
print()


zoom_image_matrix = []



new_arr = ff.make_zero_array(1024*1024)

print("Length the new array should be")
print(len(new_arr))
print()


bla = []

for row in range(0, 128):
    for column in range(0, 128):
        bla.append(ff.access_orig_array_as_matrix(row, column, brain_image))
        # print(val)
        if column != 127:
            for i in range(0, 6):
                bla.append(0)
    if row != 127:
        total_to_add = 6 * 1024
        for z in range(0, total_to_add):
            bla.append(0)

print()
print("Length of bla array")
print(len(bla))
print()

print()
print("First element in bla array")
print(bla[0])
print()

print()
print("Second element in bla array")
print(bla[1])
print()
# print(ff.access_orig_array_as_matrix(0, 0, brain_image))
# print(bla)

# bla.append(ff.access_orig_array_as_matrix(0, 0, brain_image))
#
# print(bla)

# ans = True
#
# for i in range(0, len(bla)):
#     if bla[i] != 0:
#         ans = False
#
# print(ans)