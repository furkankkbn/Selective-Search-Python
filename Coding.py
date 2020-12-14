from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QTableWidget,QTableWidgetItem,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
from Design import Ui_MainWindow

import os
import io as _io

import math
import numpy as np
import matplotlib.pyplot as plt
from xlrd import open_workbook
from openpyxl.reader.excel import load_workbook

from skimage import data, img_as_float,io
from skimage.measure import compare_ssim as SSIM2

from sklearn.metrics import mean_squared_error as MSE
from PIL import Image
import scipy
import pandas as pd
from scipy import ndimage

from skimage import data
from skimage import color
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops
import random
import matplotlib.image as IMG
from skimage import data
from skimage.measure import compare_psnr,compare_mse
from skimage.util import img_as_float
from skimage.filters import gabor_kernel
from skimage.feature import greycomatrix, greycoprops
from skimage import data
from PIL.ImageQt import ImageQt
import matplotlib.patches as mpatches
import selectivesearch
from sklearn.metrics import jaccard_similarity_score

class override_graphicsScene (Qt.QGraphicsScene):
    def __init__(self,parent = None):
        super(override_graphicsScene,self).__init__(parent)

    def mousePressEvent(self, event):
        super(override_graphicsScene, self).mousePressEvent(event)
        print(event.pos())

class MainWindow(QWidget,Ui_MainWindow):
       
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.btn_coordinates_import.clicked.connect(self.button_coordinates_import)
        self.btn_apply.clicked.connect(self.button_apply)
        self.table_result.cellClicked.connect(self.onSelected)
    
        
    def onSelected(self,row,column):
        image_name = self.table_result.item(row,0).text()
        
        _ssim = self.table_result.item(row,3).text()
        _mse = self.table_result.item(row,4).text()
        _psnr = self.table_result.item(row,5).text()
        self.lbl_ssim_score.setText(str(_ssim))
        self.lbl_mse_score.setText(str(_mse))
        self.lbl_psnr_score.setText(str(_psnr))
        
        print("./result/draw/"+image_name)
        
        scene = self.show_image_path("./result/draw/"+image_name,self.img_position.size())
        self.img_position.setScene(scene)
        
        scene = self.show_image_path("./result/boxes/"+image_name,self.img_box.size())
        self.img_box.setScene(scene)
        
        scene = self.show_image_path("./result/best/"+image_name,self.img_best.size())
        self.img_best.setScene(scene)
        
        
    dataset_path="./dataset"
    dataset_ref=[['0_MRI',93,114,20],['1_MRI',130,150,40],['1_MRI',50,119,50],['1_MRI',70,112,65],
                 ['1_MRI',58,175,35],['1_MRI',157,132,75],['1_MRI',95,103,45],
                 ['1_MRI',53,106,50],['1_MRI',130,150,40],['1_MRI',145,124,55]]
    referance_file = ""
    referance_data = []
    
    def button_coordinates_import(self):
        """file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"CSV Files (*.csv *.)")
        self.referance_file = file
        self.referance_data=[]
        
        self.dataset = pd.read_csv(file)
        print(self.dataset)"""
        
        self.table_coordinates.setColumnCount(len(self.dataset_ref[0]))
        self.table_coordinates.setRowCount(len(self.dataset_ref))
        for i,row in enumerate(self.dataset_ref):
            for j, value in enumerate(row):
                self.table_coordinates.setItem(i,j, QTableWidgetItem(str(value)))
        
        self.table_coordinates.horizontalHeader().setStretchLastSection(True)
        self.table_coordinates.resizeColumnsToContents()
        self.table_coordinates.setHorizontalHeaderLabels(['Image','x','y','r'])
        self.lbl_img_count.setText(str(len(self.dataset_ref)))
        
    from skimage.filters import rank    
    results=[]
    def button_apply(self):
        
        self.table_result.clear()
        self.results=[]
        
        count_box=0
        radius = 0
        
        file_list = os.listdir(self.dataset_path)
        for i, file in enumerate(file_list):
            f = self.dataset_path+"/"+file
            
            image = cv2.imread(f,cv2.COLOR_BGR2GRAY)
            img_name,x_real,y_real,r = self.dataset_ref[i]
            
            ssim_best_score,mse_best_score,psnr_best_score = 0,0,0
            img = self.get_crop(image,x_real,y_real,r)
            print("crop:",x_real,y_real,r)
            cv2.imwrite('./result/crop/'+str(i)+".png",img)
            radius = r
            a,b = radius,radius
            img = cv2.resize(img,(a,b))
            cv2.imwrite('./result/referances/'+str(i)+".png",img)
            #show(img)
        
            # scale=1.0, sigma=0.8, min_size=50
            img_lbl, regions = selectivesearch.selective_search(image,scale=0.5, sigma=0.5, min_size=radius)
            candidates = set()    
            for r in regions:
                candidates.add(r['rect'])
            
            index,_index,_img,_x,_y =0,0,0,0,0
            fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
            ax.imshow(image)
            
            for x, y, w, h in candidates:
                index+=1
                #img_source = self.get_crop_two(image,x,y,w,h)
                #cv2.imwrite('./result/temp/'+str(index)+".png",img_source)
                if(w>=1 and h>=1):
                    count_box+=1
                    img_source = self.get_crop_two(image,x,y,w,h)
                    cv2.imwrite('./result/temp/'+str(index)+".png",img_source)
                    img_source = cv2.resize(img_source,(a,b))
                    #show(img)
                    #show(img_source)
                    
                    score_SSIM = self.ssim(img,img_source)
                    if(score_SSIM > ssim_best_score):
                        _x,_y=x,y
                        _index = index
                        _img = img_source
                        ssim_best_score = score_SSIM
                       
                    score_MSE = compare_mse(img,img_source)    
                    if(score_MSE > mse_best_score):
                        mse_best_score = score_MSE
                    
                    score_PSNR = compare_psnr(img,img_source)    
                    if(score_PSNR > psnr_best_score):
                        psnr_best_score = score_PSNR
                        
                    rect = mpatches.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=1)
                    ax.add_patch(rect)
        
            self.get_draw_referance(image,x_real,y_real,15)
            radius = radius//2
            self.get_draw_result(image,_x+radius,_y+radius,15)
            plt.savefig('./result/boxes/'+file)
            cv2.imwrite('./result/best/'+file,_img)
            cv2.imwrite('./result/draw/'+file,image)
            self.results.append([file,_x,_y,ssim_best_score,mse_best_score,psnr_best_score])
            #break
    
        self.table_result.setColumnCount(len(self.results[0]))
        self.table_result.setRowCount(len(self.results))
        for i,row in enumerate(self.results):
            for j, value in enumerate(row):
                self.table_result.setItem(i,j, QTableWidgetItem(str(value)))        
        self.table_result.horizontalHeader().setStretchLastSection(True)
        self.table_result.resizeColumnsToContents()
        self.table_result.setHorizontalHeaderLabels(['Image','x','y','SSIM','MSE','PSNR'])
        
        self.lbl_box_count.setText(str(count_box))
        

    def show_image_path(self,img_path,size):
        self.pixmap = Qt.QPixmap()
        self.pixmap.load(img_path)
        self.pixmap = self.pixmap.scaled(size, Qt.Qt.KeepAspectRatioByExpanding,transformMode=QtCore.Qt.SmoothTransformation)
        self.graphicsPixmapItem = Qt.QGraphicsPixmapItem(self.pixmap)
        self.graphicsScene = override_graphicsScene(self)
        self.graphicsScene.addItem(self.graphicsPixmapItem)
        return self.graphicsScene
    
    def get_crop(self,img,x,y,r):
        r=r//2
        w1,h1=x-r,y-r
        w2,h2 = x+r,y+r
        img = img[h1:h2, w1:w2]
        #img = img[y:y+r, x:x+r]
        return img
    
    def get_crop_two(self,img,x,y,w,h):
        img = img[y:y+h, x:x+w]
        return img
    
    """def show(self,img):
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()"""
           
    def ssim(self,img1,img2):
        img_1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img_2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        try:
            if(not img_1 is None and not img_2 is None):
                if(img_1.size == img_2.size):
                    return round(SSIM2(img_1,img_2),2)
            else:
                return 0.0
        except ValueError:
            print("Invalid Entry - try again")
            return 0.0
        return 0.0
    
    def get_draw_referance(self,img,x,y,r):
        cv2.circle(img,(x, y), r, (0,0,0), 3)
        return img
    
    def get_draw_result(self,img,x,y,r):
        cv2.circle(img,(x, y), r, (0,255,0), 3)
        return img
    
    def jaccard(self,img1,img2):
        img_true=np.array(img1).ravel()
        img_pred=np.array(img2).ravel()
        iou = jaccard_similarity_score(img_true, img_pred)
        return iou    
    
    def mse(self,img1,img2):
        img_1 = img1
        img_2 = img2
        
        e = np.sum((img_1.astype("float") - img_2.astype("float"))**2)
        e /= float(img_1.shape[0] * img_2.shape[1])
        r = round(e,2)
        return r
    
    def psnr(self,img1, img2):
        img1 = np.asarray(img1)#cv2.imread(img1)
        img2 = np.asarray(img2)#cv2.imread(img2)
        mse = np.mean( (img1 - img2) ** 2 )
        if mse == 0:
            return 1
        PIXEL_MAX = 255.0
        psnr = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
        print("PSNR------>",str(psnr/1000))
        return psnr/1000