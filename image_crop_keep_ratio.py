# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:36:27 2019

@author: LL

"""
import cv2,glob
import random
if __name__ == "__main__":
    src_dir = "./image/"   
    filepath = glob.glob(src_dir + '*.*')   #不要出现中文名
    count = 0
    for i in range(len(filepath)):
        img_src = cv2.imread(filepath[i])
        height = len(img_src)
        width = len(img_src[0])
        kuang_gao_bi = width / height
#        h =  random.uniform(3/4, 3/4)
#        w =  random.uniform(4/3, 4/3)
        h =  3/4  #太宽，裁宽
        w =  4/3  #太高，裁高
        
        if kuang_gao_bi > 3/4:         # 太宽
            zy = int((width-(height*h))/2) 
            print("h=",kuang_gao_bi)
            img_cut = img_src[ : , zy:int(width-zy)]
            
            img_cut = cv2.resize(img_cut,(240,320),interpolation=cv2.INTER_CUBIC)
            
        elif  kuang_gao_bi < 3/4:      # 太高   
            sx = int((height-(width*w))/2)
            print("w=",kuang_gao_bi)
            img_cut = img_src[sx:int(height-sx), : ]
            img_cut = cv2.resize(img_cut,(240,320),interpolation=cv2.INTER_CUBIC)

#        elif 4/3 > kuang_gao_bi >3/4 :         
#            sx = int((height-(width*w))/2)
#            print("w=",kuang_gao_bi)
#            img_cut = img_src[sx:int(height-sx), : ]
#            img_cut = cv2.resize(img_cut,(240,320),interpolation=cv2.INTER_CUBIC)
            
#        elif  3/4 < kuang_gao_bi < 1:         
#            sx = int((height-(width*w))/2)
#            print("w=",kuang_gao_bi)
#            img_cut = img_src[sx:int(height-sx), : ]
#            img_cut = cv2.resize(img_cut,(240,320),interpolation=cv2.INTER_CUBIC)
            
        else:                       # 刚好
             img_cut = cv2.resize(img_src,(240,320),interpolation=cv2.INTER_CUBIC)
        
        save_dir = "./image_result/crop{}.jpg".format(count)
        count += 1
        cv2.imwrite(save_dir, img_cut)
    