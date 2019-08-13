#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import face_recognition
import os

'''
__AUTHOR__ = liyang

'''

''' 计算欧式距离
x=np.random.random(3)
y=np.random.random(3)
d1=np.sqrt(np.sum(np.square(x-y))
'''

class faceHandler(object):
    '''
    初始化,图片目录名称
    '''
    def __init__(self,imgDir):
        self._imgDir = imgDir

    '''
       获取图片目录路径
    '''
    def _getImgPath(self):
        abspath = os.path.abspath('.')
        return os.path.join(abspath,self._imgDir)
   
    '''
       获取目标图片的特征值
       @rteurn numpy array
    '''
    def getImgEncoding(self,imgName):
        numpyImg = face_recognition.load_image_file(self._getImgPath()+"/"+imgName)
        try:
          imgEncoding = face_recognition.face_encodings(numpyImg)[0]
        except Exception as e:
          imgEncoding = []
        return imgEncoding 

    '''
      对比图片是否为本人
      @param  knownImgEncoding   已知图片特征值
      @param  unkownImgEncodeing 未知图片特征值
      @param  threshold          对比欧式距离阀值，经过测试，亚洲人设置0.50更为合适，西方人定的标准是0.6
      @return boolean
    '''
    def compareImg(self,knownImgEncoding,unkownImgEncodeing,threshold=0.50):
        knownImgEncodings = [knownImgEncoding]
        faceDistances = face_recognition.face_distance(knownImgEncodings,unkownImgEncodeing)
        for i, face_distance in enumerate(faceDistances):
	        print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
	        print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
	        print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.52))
        
        if faceDistances <= threshold :
           return True
        else:
           return False

if __name__ == '__main__':
  
   face = faceHandler('images')
   kownImgEncoding = face.getImgEncoding('sun1.jpg')
   unkownImgEncodeing = face.getImgEncoding('sun2.jpg')
   result = face.compareImg(kownImgEncoding,unkownImgEncodeing)
   print(result)