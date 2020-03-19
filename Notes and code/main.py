from PIL import Image
import numpy as np
img_w, img_h = 200, 200
data = np.zeros((img_h, img_w, 3), dtype=np.uint8)
data[25:75, 25:75] = [255, 255, 255]
data[25:75,125:175] = [255,255,255]
data[125:150,45:150] = [255,255,255]
img = Image.fromarray(data, 'RGB')
img.save('test.png')
img.show()
