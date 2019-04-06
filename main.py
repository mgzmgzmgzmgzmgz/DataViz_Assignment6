import functions_file


image_path = "/Users/micahgiles/Desktop/Inner_Desktop/UAB_Spring_19/Data_Visualization/Assignment_6/brain_128_128.raw"

pre_im = open(image_path, 'rb')

brain_image = pre_im.read()


zoom_image_matrix = []

for i in range(0, 128*4):
    zoom_image_matrix.append([])
    for j in range(0, 128*4):
        zoom_image_matrix[i].append(0)

