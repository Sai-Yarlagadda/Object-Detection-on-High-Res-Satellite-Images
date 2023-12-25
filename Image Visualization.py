import cv2
import numpy as np
#from Anchor_box import extract_box_dims, dimension_extractor
#image_path = "images/"
#annot_path = "labelTxt-v1.5/"

def visualize_oriented_bbox(img, coords_list):
    for coords in coords_list:
        corners = np.array(coords).reshape((4,2))
        cv2.polylines(img, [corners.astype(np.int32)], True, (0,255,0),2)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

doc = "labelTxt/P0008.txt"
file = open(doc,'r')
coords_list = []
annot_num = [15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
annot_count=0
for annot in file:
    if annot_count in annot_num:
        coords = [float(num) for num in annot.rstrip().split()[:8]]
        coords_list.append(coords)
    annot_count +=1

img_path = "images\\P0008.png"
img = cv2.imread(img_path)
(h,w,c) = img.shape[:3]
print(h, w, c)
visualize_oriented_bbox(img, coords_list)
#cv2.imwrite('img.png', img)
