# Digital Image Processing
基于Python语言的数字图像处理程序，包含登录界面和工具栏。主要功能包括：灰度变换（n值化、线性化、非线性化）；绘制RGB直方图；两幅任意大小、通道图像相加；均值滤波和中值滤波；Sobel算子锐化；集成人脸识别API如face_recognition库、虹软SDK、face++、paddlehub库

A Windows application based on tkinter of Python for image processing purposes, which is part of my final project of course *Digital Image Processing and Experiment* in CAU(China Agricultural University).

## Details
The main functions include:
- Grayscale transformation (N value, linearization, nonlinearization)
- Plot RGB histogram
- Add two images on pixel-level (images could be arbitrary size and channel)
- Mean filtering and Median filtering
- Sobel operator sharpness
- Face detection based on multiple API:
	- face_recognition packages of Python
	- arcsoft SDK
	- face++ API
	- Paddlehub

## Requirements
```
$ pip install -r requirements.txt
```
## Run
```
$ python login.py
```
## Results Show（incomplete）

|(●'◡'●)|Operation|Result|
|---|---|----
|<p align="center">1</p>|<p align="center">Login Interface(password is 123)</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/Login.png" width = "300" height = "200" alt="" align=center />
|<p align="center">2</p>|<p align="center">Register Interface</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/register.png" width = "300" height = "200" alt="" align=center />
|<p align="center">3</p>|<p align="center">N Value</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/n_value.png" width = "300" height = "200" alt="" align=center />
|<p align="center">4</p>|<p align="center">Images Add</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/img_add.png" width = "300" height = "200" alt="" align=center />
|<p align="center">5</p>|<p align="center">RGB_histogram</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/RGB_histogram.png" width = "300" height = "200" alt="" align=center />
|<p align="center">6</p>|<p align="center">Median Filtering</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/median_filtering.png" width = "300" height = "200" alt="" align=center />
|<p align="center">7</p>|<p align="center">Logarithmic Grayscale Transformation</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/Logarithmic_gray_scale_transformation.png" width = "300" height = "200" alt="" align=center />
|<p align="center">8</p>|<p align="center">Sobel</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/Sobel.png" width = "300" height = "200" alt="" align=center />
|<p align="center">9</p>|<p align="center">Face Detection</p>|<img src="https://github.com/leaving-voider/Digital-Image-Processing/blob/master/imgs_detection/example1.png" width = "300" height = "200" alt="" align=center />

## Notes
The arcsoft face detection API need you to appy and then you can use. [Here](https://blog.csdn.net/weixin_42815846/article/details/106882614) is a tutorial to teach you how to do that.

When you get your `APPID` and `FD_SDKKEY` successfully, you can replace the two lines below with them within the [hrFace.py](https://github.com/leaving-voider/Digital-Image-Processing/blob/master/face_detection/hrFace.py) file.
![img](https://github.com/leaving-voider/Digital-Image-Processing/blob/master/screenshots/modifications.png)
