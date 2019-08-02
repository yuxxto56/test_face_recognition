# test_face_recognition
人脸识别技术，利用开源人脸识别训练库开发人脸识别，应用场景：真实身份认证、人证合一等场景
### 安装训练库
* 安装face-recognition库
```
  1、安装cmake #若已安装则忽略第一步
  pip install cmake
  2、安装face-recognition
  pip install face-recognition --timeout=1000 #此过程安装比较长,耐心等待
  ##备注
  安装成功,则也一并安装了numpy、face-recognition-models、dlib等依赖库
```
### 人脸对比场景

结合已经封装的face.py文件
* 对比不同人
 ```
   1、输入
   face = faceHandler('images')
   kownImgEncoding = face.getImgEncoding('sun1.jpg')
   unkownImgEncodeing = face.getImgEncoding('sun2.jpg')
   result = face.compareImg(kownImgEncoding,unkownImgEncodeing)
   print(result)
   2、输出
   The test image has a distance of 0.44 from known image #0
   - With a normal cutoff of 0.6, would the test image match the known image? True
   - With a very strict cutoff of 0.5, would the test image match the known image? True
   True #结果通过
 ```
* 对比不同人
 ```
   1、输入
   face = faceHandler('images')
   kownImgEncoding = face.getImgEncoding('sun1.jpg')
   unkownImgEncodeing = face.getImgEncoding('gem1.jpg')
   result = face.compareImg(kownImgEncoding,unkownImgEncodeing)
   print(result)
   2、输出
  The test image has a distance of 0.56 from known image #0
  - With a normal cutoff of 0.6, would the test image match the known image? True
  - With a very strict cutoff of 0.5, would the test image match the known image? False
  False #结果不通过
 ```
