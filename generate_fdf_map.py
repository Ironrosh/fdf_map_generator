import sys
from PIL import Image
import numpy as np

if len(sys.argv) != 2:
	sys.exit("Usage: python3 generate_fdf_map.py path_to_file")
picture = Image.open(sys.argv[1])
picture = picture.convert('RGB')
width, height = picture.size
print("Your picture resolution is", width, "x", height)
if width > height:
	d = width / 10
else:
	d = height / 10
pixels = picture.load()
arr = [[0 for w in range(height)] for h in range(width)]
for i in range(picture.size[0]):
	for j in range(picture.size[1]):
		summ = pixels[i,j][0] + pixels[i,j][1] + pixels[i,j][2]
		arr[i][j] = d - (summ % d)
		#if pixels[i,j] != (255, 255, 255):
		#	arr[i][j] = 10
		#else:
		#	arr[i][j] = 0
fdf = open("out.fdf", 'w+')
for i in range(picture.size[0]):
	for j in range(picture.size[1]):
		fdf.write("%d " % arr[i][j])
	fdf.write("\n")
fdf.close()
