from __future__ import (
    division,
    print_function,
)

from selectivesearch import *
from skimage import data, img_as_float,io
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import structural_similarity as _SSIM
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
       
def get_crop(img,x,y,r):
    w1,h1=x-r,y-r
    w2,h2 = x+r,y+r
    img = img[h1:h2, w1:w2]
    return img

def get_crop_two(img,x,y,w,h):
    img = img[y:y+h, x:x+w]
    return img

def show(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
       
def ssim(img1,img2):
    """img_1 = np.asarray(img1)#cv2.imread(img1)
    img_2 = np.asarray(img2)#cv2.imread(img2)"""

    img_1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img_2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    try:
        if(not img_1 is None and not img_2 is None):
            if(img_1.size == img_2.size):
                return round(_SSIM(img_1,img_2),2)
        else:
            return 0.0
    except ValueError:
        print("Invalid Entry - try again")
        return 0.0
    return 0.0
    

def get_draw_referance(img,x,y,r):
    cv2.circle(img,(x, y), r, (0,0,0), 3)
    return img

def get_draw_result(img,x,y,r):
    #3 ayıt edebilmek için
    cv2.circle(img,(x, y), r, (0,255,0), 3)
    return img



dataset_path="./dataset"
dataset_ref=[[93,114,20],[130,150,40],[50,119,50],[70,112,65],
             [58,175,35],[157,132,75],[95,103,45],
             [53,106,50],[130,150,40],[145,124,55]]
radius = 0
file_list = os.listdir(dataset_path)
print(file_list)
for i, file in enumerate(file_list):
    f = dataset_path+"/"+file
    print("file: ",f)
    
    image = cv2.imread(f,cv2.COLOR_BGR2GRAY)
    x_real,y_real,r = dataset_ref[i]
    print("Coordinate:",x_real,y_real,r)
    radius = r
    anger = 10
    best_score = 0
    img = get_crop(image,x_real,y_real,r)
    a,b = radius,radius
    img = cv2.resize(img,(a,b))
    #show(img)

    img_lbl, regions = selectivesearch.selective_search(image, scale=500, sigma=0.9, min_size=10)
    candidates = set()    
    for r in regions:
        candidates.add(r['rect'])
    
    index,_index,_img,_img_crop,_x,_y =0,0,0,0,0,0
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(image)
    
    for x, y, w, h in candidates:
        index+=1
        #x>=anger and y>=anger and 
        if(w>=radius and h>=radius):
            #print(x, y, w, h,radius)
            img_source = get_crop_two(image,x,y,w,h)
            cv2.imwrite('./result/temp/'+str(index)+".png",img_source)
            img_source = cv2.resize(img_source,(a,b))
            #show(img)
            #show(img_source)
            
            score = ssim(img,img_source)
            print("score=",str(score))
            if(score > best_score):
                _x,_y=x,y
                _index = index
                _img = img_source
                best_score = score
                
            print("best score=",str(best_score))
            rect = mpatches.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=1)
            ax.add_patch(rect)

    print("--->",x_real,y_real)
    get_draw_referance(image,x_real,y_real,15)
    get_draw_result(image,_x+radius,_y+radius,15)
    plt.savefig('./result/boxes/'+file)
    #plt.show()
    cv2.imwrite('./result/best/'+file,_img)
    #show(_img_crop)
    #show(_img)
    #show(image)
    cv2.imwrite('./result/draw/'+file,image)
    #break
