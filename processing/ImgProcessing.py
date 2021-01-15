from tkinter import filedialog, simpledialog
# import win32com.client # 微软这个服务器
import tkinter
from tkinter.constants import *
import math
import tkinter.messagebox
import pyglet
import os
from PIL import Image, ImageTk
# from pydub import AudioSegment # 音频格式转换
from images.memory_pic import * # 导入图片
import base64 # 编码
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import cv2

# 导入face_recogntion模块
import face_recognition
import time
# 导入虹软检测模块
from face_detection.hrFace import *
from face_detection.facepp_detection import *
# 导入paddlehub模块
from face_detection.paddleHub import *

# 主图片路径
Img_path = ""
# 专门用于打开图片的toplevel窗口
topWin = 0

# n值化灰度变换专用窗口
GreyNvaluesWin = 0
# 线性化灰度变换专用窗口
GreyLinearWin = 0
# 非线性化对数变换窗口
GreyLogWin = 0
# 非线性化指数变换窗口
GreyExWin = 0

# GRB三通道直方图专用窗口
RgbHistWin = 0

# 图像相加的第二个图片路径
ImgPlus_path = ""
# 图片相加的第二个图片专用窗口
ImgPlueSecWin = 0
# 相加的图片专用窗口
ImgPlusResultWin = 0

# 滤波专用椒盐窗口（暂未使用）
PepperSaltWin = 0
# 均值滤波专用窗口
AvgFilterWin = 0
# 中值滤波专用窗口
MedFilterWin = 0

# Sobel图像锐化
SobelSharpenWin = 0

# 人脸检测
FaceRecogWinn = 0


####################################################################################################################################
####################################################################################################################################
######################################                    FILE CLASS                       #########################################
####################################################################################################################################
####################################################################################################################################

def is_chinese(Str):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in Str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

class FILE:
    

    def template():
        '''各种窗口'''
        #res = messagebox.askokcancel(title='标题', message='提示信息。。。', default=messagebox.CANCEL) # default=messagebox.CANCEL，指定默认焦点位置，另 ABORT/RETRY/IGNORE/OK/CANCEL/YES/NO
        #res = messagebox.showinfo(title='标题', message='提示信息。。。')
        #res = messagebox.showwarning(title='标题', message='提示信息。。。')
        #res = messagebox.showerror(title='标题', message='提示信息。。。')
        #res = messagebox.askquestion(title='标题', message='提示信息。。。') 
        #res = messagebox.askyesno(title='标题', message='提示信息。。。')
        #res = messagebox.askyesnocancel(title='标题', message='提示信息。。。')
        #res = messagebox.askretrycancel(title='标题', message='提示信息。。。')
        
        #res = filedialog.askdirectory()
        #res = filedialog.askopenfile(filetypes=[('xml', '*.xml')])
        #res = filedialog.askopenfiles()
        #res = filedialog.askopenfilename()
        #res = filedialog.askopenfilenames()
        #res = filedialog.asksaveasfile()
        #res = filedialog.asksaveasfilename()
        
        #res = simpledialog.askinteger(title='整数', prompt='输入一个整数', initialvalue=100)
        #res = simpledialog.askfloat(titlee='实数', prompt='输入一个实数', minvalue=0, maxvalue=11)
        res = simpledialog.askstring(title='字符串', prompt='输入一个字符串')
        
        #res = colorchooser.askcolor()
        print(res)
        return
    
    '''
    文件
    ['打开', '保存', '另存为...']
    '''
    # 打开文件
    def dialog1():
        global Img_path, topWin

        filePath = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("BMP",".bmp")]) # 打开文件夹对话框

        if not filePath:
            tkinter.messagebox.showerror(message="Cannot open this file!")
            return
        
        if (is_chinese(filePath)):
            tkinter.messagebox.showerror(message="Cannot open this file because of Chinese Path!")
            return

        try:
            topWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            topWin = tkinter.Toplevel()
            topWin.attributes('-topmost', True)
        # topWin = tkinter.Toplevel()
        topWin.geometry("360x240")
        topWin.resizable(True,True) # 可缩放
        topWin.title("IMAGE")
        # ImageWindow.withdraw()
        LabelPic = tkinter.Label(topWin, text="IMG", width=360, height=240)
        # im = Image.open(filePath)
        im = cv2.imread(filePath)
        im = im[:, :, ::-1]

        image = ImageTk.PhotoImage(Image.fromarray(im))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(im, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        # 记录便于图像处理
        Img_path = filePath
        # Img_path[1].append(ImageWindow)
        # TopWin.append(ImageWindow)
        # print(filePath, ImageWindow)
        # print(Img_path)
        return 

    # 保存文件
    def dialog2():
        return

    # 另存为
    def dialog3():
        return








####################################################################################################################################
####################################################################################################################################
######################################                    EDIT CLASS                       #########################################
####################################################################################################################################
####################################################################################################################################


class EDIT:
    '''
    编辑
    ['撤销', '-',  '剪切', '复制', '粘贴', '删除', '选择所有',['更多...','数据', '图表', '统计']]
    '''
    def dialog1():
        return









####################################################################################################################################
####################################################################################################################################
######################################                    TOOLS CLASS                       ########################################
####################################################################################################################################
####################################################################################################################################

class TOOLS:
    '''
    工具
    [['灰度变换', 'n值化', '线性化', ['非线性化', '对数变换', '伽马变换']], '绘制直方图', '图像相加', '图像滤波', '图像锐化']
    ''' 
    # n值化
    def grey_n():
        global Img_path, GreyNvaluesWin
        print("n值化")
        if(Img_path==""):
            return

        # n值化灰度变换函数
        def N_values_TRANS(n, img):
            dst = img*n
            return dst
        # 得到img的array
        img=np.array(Image.open(Img_path).convert('L'))

        # 读取n
        n = simpledialog.askinteger(title='变换函数 Fx = Fx*n', prompt='输入n', initialvalue=2)

        # 进行n值化灰度变换
        img = N_values_TRANS(n, img)

        # 创建toplevel窗口
        try:
            GreyNvaluesWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            GreyNvaluesWin = tkinter.Toplevel()
            GreyNvaluesWin.attributes('-topmost', True)
        GreyNvaluesWin.geometry("360x240")
        GreyNvaluesWin.resizable(True,True) # 可缩放
        GreyNvaluesWin.title("N值化灰度变换")
        
        LabelPic = tkinter.Label(GreyNvaluesWin, text="IMG", width=360, height=240)

        image = ImageTk.PhotoImage(Image.fromarray(img))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    # 线性化
    def grey_lin():
        global Img_path, GreyLinearWin
        print("线性化")
        if(Img_path==""):
            return

        # 线性化灰度处理函数
        def Contrast_and_Brightness(a, b, img):
            blank = np.ones(img.shape, img.dtype)
            # dst = alpha * img + beta * blank
            dst = img*a + b*blank
            return dst
        # 得到img的array
        img=np.array(Image.open(Img_path).convert('L'))

        # 读取alpha、beta
        a = simpledialog.askfloat(title='变换函数 Fx = Fx*a + b', prompt='输入a', minvalue=0, maxvalue=100)
        b = simpledialog.askfloat(title='变换函数 Fx = Fx*a + b', prompt='输入b', minvalue=0, maxvalue=100)

        # 进行变换
        img = Contrast_and_Brightness(a,b,img)

        # 创建toplevel窗口
        try:
            GreyLinearWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            GreyLinearWin = tkinter.Toplevel()
            GreyLinearWin.attributes('-topmost', True)
        GreyLinearWin.geometry("360x240")
        GreyLinearWin.resizable(True,True) # 可缩放
        GreyLinearWin.title("线性化灰度变换")
        
        LabelPic = tkinter.Label(GreyLinearWin, text="IMG", width=360, height=240)

        image = ImageTk.PhotoImage(Image.fromarray(img))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    # 非线性化——对数变换
    def grey_lg():
        global Img_path, GreyLogWin
        print("对数变换")
        if(Img_path==""):
            return

        # 对数灰度处理函数
        def Log_TRANS(c, img):
            blank = np.ones(img.shape, img.dtype)
            img += blank
            img[img==0] = 255
            img = np.log10(img)
            dst = c*img
            dst = dst.astype(np.uint8)
            return dst
        # 得到img的array
        img=np.array(Image.open(Img_path).convert('L'))

        # 读取c、r
        c = simpledialog.askinteger(title='变换函数 Fx = c*log(1+Fx)', prompt='输入c', minvalue=0, maxvalue=100)

        # 进行变换
        img = Log_TRANS(c,img)

        # 创建toplevel窗口
        try:
            GreyLogWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            GreyLogWin = tkinter.Toplevel()
            GreyLogWin.attributes('-topmost', True)
        GreyLogWin.geometry("360x240")
        GreyLogWin.resizable(True,True) # 可缩放
        GreyLogWin.title("对数灰度变换")
        
        LabelPic = tkinter.Label(GreyLogWin, text="IMG", width=360, height=240)

        image = ImageTk.PhotoImage(Image.fromarray(img))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    # 非线性化——伽马变换
    def grey_gamma():
        global Img_path, GreyExWin
        print("伽马变换")

        if(Img_path==""):
            return

        # 伽马灰度处理函数
        def Gamma_TRANS(c, r, img):
            dst = c*np.power(img, r)
            return dst
        # 得到img的array
        img=np.array(Image.open(Img_path).convert('L'))

        # 读取c、r
        c = simpledialog.askfloat(title='变换函数 Fx = c*Fx**r', prompt='输入c', minvalue=0, maxvalue=100)
        r = simpledialog.askfloat(title='变换函数 Fx = c*Fx**r', prompt='输入r', minvalue=0, maxvalue=100)

        # 进行变换
        img = Gamma_TRANS(c,r,img)

        # 创建toplevel窗口
        try:
            GreyExWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            GreyExWin = tkinter.Toplevel()
            GreyExWin.attributes('-topmost', True)
        GreyExWin.geometry("360x240")
        GreyExWin.resizable(True,True) # 可缩放
        GreyExWin.title("伽马灰度变换")
        
        LabelPic = tkinter.Label(GreyExWin, text="IMG", width=360, height=240)

        image = ImageTk.PhotoImage(Image.fromarray(img))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    ################################################################################################################################

    # RGB三通道直方图
    def Hist_RGB():
        global Img_path, RgbHistWin
        print("三通道直方图")
        if(Img_path==""):
            return

        # 创建toplevel窗口
        try:
            RgbHistWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            RgbHistWin = tkinter.Toplevel()
            RgbHistWin.attributes('-topmost', True)
        RgbHistWin.geometry("550x400")
        RgbHistWin.resizable(True,True) # 可缩放
        RgbHistWin.title("RGB三通道直方图")

        # 创建figure
        fig = Figure(figsize=(8, 6), dpi=100)
        fig_plot = fig.add_subplot(111)

        # 创建figure中的画布，并绑定RgbHistWin
        canvas = FigureCanvasTkAgg(fig, RgbHistWin)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # 清空figure
        fig_plot.clear()
        # 得到图像
        img = cv2.imread(Img_path,1)
        color = ('b','g','r')
        for i,col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
            fig_plot.plot(histr,color = col)
        canvas.draw()
        
        return

    ################################################################################################################################

    # 图片相加
    def ImgPlus():
        global Img_path, ImgPlus_path, ImgPlueSecWin, ImgPlusResultWin
        secondSize = 0
        print("图片相加")
        if(Img_path==""):
            return

        # 读取需要加和的图片
        ImgPlus_path = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("BMP",".bmp")]) # 打开文件夹对话框
        
        if (is_chinese(ImgPlus_path)):
            tkinter.messagebox.showerror(message="Cannot open this file because of Chinese Path!")
            return

        if not ImgPlus_path:
            tkinter.messagebox.showerror(message="Cannot open this file!")
            return
        try:
            ImgPlueSecWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            ImgPlueSecWin = tkinter.Toplevel()
            ImgPlueSecWin.attributes('-topmost', True)
        # topWin = tkinter.Toplevel()
        ImgPlueSecWin.geometry("360x240")
        ImgPlueSecWin.resizable(True,True) # 可缩放
        ImgPlueSecWin.title("被加的图片")
        LabelPic = tkinter.Label(ImgPlueSecWin, text="IMG", width=360, height=240)

        # 读取second图片
        im = cv2.imread(ImgPlus_path)
        secondSize = im.shape
        im = im[:, :, ::-1]

        image = ImageTk.PhotoImage(Image.fromarray(im))
        LabelPic.image = image
        LabelPic['image'] = image
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(im, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        # 图像相加函数
        def IMG_PLUS(img1, img2):
            img1 = cv2.resize(img1, (im.shape[1], im.shape[0]))
            dst = img1*0.5 + img2*0.5
            dst = dst.astype(np.uint8)
            return dst
        # 转换图片的通道
        def ChannelShift(img):
            # 4通道转3通道
            if img.mode == 4:
                r, g, b, a = img.split()
                img = Image.merge("RGB", (r, g, b))
            #  1 通道转3通道
            elif img.mode != 'RGB':
                img = img.convert("RGB")
            return img


        # 得到img的array
        img1 = Image.open(Img_path)
        img2 = Image.open(ImgPlus_path)

        img1 = np.array(ChannelShift(img1))
        img2 = np.array(ChannelShift(img2))

        # 进行变换
        img = IMG_PLUS(img1,img2)

        # 创建合成窗口
        try:
            ImgPlusResultWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            ImgPlusResultWin = tkinter.Toplevel()
            ImgPlusResultWin.attributes('-topmost', True)
        # topWin = tkinter.Toplevel()
        ImgPlusResultWin.geometry("360x240")
        ImgPlusResultWin.resizable(True,True) # 可缩放
        ImgPlusResultWin.title("加和结果图片")
        LabelPic2 = tkinter.Label(ImgPlusResultWin, text="IMG", width=secondSize[1], height=secondSize[0])

        # img 必须(只能)是<class 'numpy.uint8'>
        image2 = ImageTk.PhotoImage(Image.fromarray(img))
        LabelPic2.image = image2
        LabelPic2['image'] = image2
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (event.width, event.height))))
            LabelPic2.image = image1
            LabelPic2['image'] = image1
        LabelPic2.bind('<Configure>', changeSize)
        LabelPic2.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return



    ################################################################################################################################


    # 均值滤波
    def AvgFiltering():
        global Img_path, PepperSaltWin, AvgFilterWin
        print("均值滤波")
        if(Img_path==""):
            return

        # 均值滤波处理函数
        def AvgFilterProc(l, img):
            # 按维度加和
            def Mysum(ThreeDimMatrix):
                ThreeDimMatrix = ThreeDimMatrix.sum(axis = 0)
                ThreeDimMatrix = ThreeDimMatrix.sum(axis = 0)
                return ThreeDimMatrix
            # 计算填充数
            padding = (l-1)//2
            # print('img', img.shape)
            if len(img.shape)==2:
                # 支持一维灰度图
                pad = ((padding, padding), (padding, padding))
                Filter = np.ones((l, l), img.dtype)
            else:
                # 长、高填充，深度不填充
                pad = ((padding, padding), (padding, padding), (0,0))
                # 得到filter
                Filter = np.ones((l, l, img.shape[2]), img.dtype)
            # 图片周围填充0
            padImg= np.pad(img, pad, 'constant', constant_values=(0, 0))
            # 高 1080
            for i in range(padding, padImg.shape[0] - padding):
                # 长 1920
                for j in range(padding, padImg.shape[1] - padding):
                    # 对应位相乘
                    padImg[i][j] = Mysum(Filter * padImg[i-padding:i+padding+1, j-padding:j+padding+1])//(l ** 2)
            dst = padImg[padding:padImg.shape[0] - padding, padding:padImg.shape[1] - padding]  #把操作完多余的0去除，保证尺寸一样大
            return dst
        # 得到img的array
        img=np.array(Image.open(Img_path))

        # 读取l
        l = simpledialog.askinteger(title='滤波核大小(边长 奇数)', prompt='输入边长L', initialvalue=3, minvalue=0, maxvalue=41)
        if l%2==0:
            tkinter.messagebox.showerror(message="The length must be odd number!")
            return

        # 进行变换
        tkinter.messagebox.showinfo(title='Notes', message='Please be patient, the time may take a while because of Matrix Calculation')
        img = AvgFilterProc(l, img)

        # 创建toplevel窗口
        try:
            AvgFilterWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            AvgFilterWin = tkinter.Toplevel()
            AvgFilterWin.attributes('-topmost', True)
        AvgFilterWin.geometry("360x240")
        AvgFilterWin.resizable(True,True) # 可缩放
        AvgFilterWin.title("均值滤波")
        
        LabelPic = tkinter.Label(AvgFilterWin, text="IMG", width=360, height=240)

        image = ImageTk.PhotoImage(Image.fromarray(img))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    # 中值滤波
    def MedFiltering():
        global Img_path, PepperSaltWin, MedFilterWin
        print("中值滤波")
        if(Img_path==""):
            return
        
        # 中值滤波处理函数
        def MedFilterProc(l, img):
            # 按维度加和
            def MyMedian(ThreeDimMatrix):
                # axis0为纵轴，1为深度轴，2为横轴，这很坑
                blank = 0
                if len(img.shape)==2:
                    blank = np.median(ThreeDimMatrix)
                else:
                    blank = np.zeros((img.shape[2]))
                    for i in range(img.shape[2]):
                        blank[i] = np.median(ThreeDimMatrix[:,:,i])
                return blank
            # 计算填充数
            padding = (l-1)//2
            # print('img', img.shape)
            if len(img.shape)==2:
                # 支持一维灰度图
                pad = ((padding, padding), (padding, padding))
            else:
                # 长、高填充，深度不填充
                pad = ((padding, padding), (padding, padding), (0,0))
            # 图片周围填充0
            padImg= np.pad(img, pad, 'constant', constant_values=(0, 0))
            print('padImg', padImg.shape)
            # 高 1080
            for i in range(padding, padImg.shape[0] - padding):
                # 长 1920
                for j in range(padding, padImg.shape[1] - padding):
                    # 对应位相乘
                    padImg[i][j] = MyMedian(padImg[i-padding:i+padding+1, j-padding:j+padding+1])

            dst = padImg[padding:padImg.shape[0] - padding, padding:padImg.shape[1] - padding]  #把操作完多余的0去除，保证尺寸一样大
            return dst
        # 得到img的array
        img=np.array(Image.open(Img_path))

        # 读取l
        l = simpledialog.askinteger(title='滤波核大小(边长 奇数)', prompt='输入边长L', initialvalue=3, minvalue=0, maxvalue=41)
        if l%2==0:
            tkinter.messagebox.showerror(message="The length must be odd number!")
            return

        # 进行变换
        tkinter.messagebox.showinfo(title='Notes', message='Please be patient, the time may take a while because of Matrix Calculation')
        img = MedFilterProc(l, img)

        # 创建toplevel窗口
        try:
            MedFilterWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            MedFilterWin = tkinter.Toplevel()
            MedFilterWin.attributes('-topmost', True)
        MedFilterWin.geometry("360x240")
        MedFilterWin.resizable(True,True) # 可缩放
        MedFilterWin.title("中值滤波")
        
        LabelPic = tkinter.Label(MedFilterWin, text="IMG", width=360, height=240)

        image = ImageTk.PhotoImage(Image.fromarray(img))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    ################################################################################################################################

    # Sobel图像锐化
    def Sobel_Sharpening():
        global Img_path, SobelSharpenWin
        print("Sobel锐化")
        if(Img_path==""):
            return
        
        # 得到img的array
        img=np.array(Image.open(Img_path))
        # img = cv2.imread(Img_path)
        # img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

        def Sobel_Sharpen(img):
            img = img.astype(np.int32)
            fx = np.ones(img.shape, np.int32)
            fy = np.ones(img.shape, np.int32)
            contemplateX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
            contemplateY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
            def HorizontalSobel(Img3DMatrix):
                # axis0为纵轴，1为深度轴，2为横轴，这很坑
                blank = 0
                if len(img.shape)==2:
                    blank = np.sum(Img3DMatrix*contemplateX)
                else:
                    blank = np.zeros((img.shape[2]))
                    for i in range(img.shape[2]):
                        blank[i] = np.sum(Img3DMatrix[:,:,i]*contemplateX)
                return blank

            def VerticalSobel(Img3DMatrix):
                # axis0为纵轴，1为深度轴，2为横轴，这很坑
                blank = 0
                if len(img.shape)==2:
                    blank = np.sum(Img3DMatrix*contemplateY)
                else:
                    blank = np.zeros((img.shape[2]))
                    for i in range(img.shape[2]):
                        blank[i] = np.sum(Img3DMatrix[:,:,i]*contemplateY)
                return blank

            # 计算填充数
            padding = 1
            # print('img', img.shape)
            if len(img.shape)==2:
                # 支持一维灰度图
                pad = ((padding, padding), (padding, padding))
            else:
                # 长、高填充，深度不填充
                pad = ((padding, padding), (padding, padding), (0,0))
            # 图片周围填充0
            padImg= np.pad(img, pad, 'constant', constant_values=(0, 0))
            fx = np.pad(img, pad, 'constant', constant_values=(0, 0))
            fy = np.pad(img, pad, 'constant', constant_values=(0, 0))

            print('padImg', padImg.shape)
            # 高 1080
            for i in range(padding, padImg.shape[0] - padding):
                # 长 1920
                for j in range(padding, padImg.shape[1] - padding):
                    # 求fx
                    fx[i][j] = HorizontalSobel(padImg[i-padding:i+padding+1, j-padding:j+padding+1])
                    # 求fy
                    fy[i][j] = VerticalSobel(padImg[i-padding:i+padding+1, j-padding:j+padding+1])

            fx = fx[padding:padImg.shape[0] - padding, padding:padImg.shape[1] - padding]  #把操作完多余的0去除，保证尺寸一样大
            fy = fy[padding:padImg.shape[0] - padding, padding:padImg.shape[1] - padding]  #把操作完多余的0去除，保证尺寸一样大
            
            # 若是多通道，则每层分别计算
            if len(img.shape)==2:
                cv2.imshow('fx',np.uint8(fx))
                cv2.imshow('fy',np.uint8(fy))
                fx2 = fx*fx
                fy2 = fy*fy
                dst = np.sqrt(fx2 + fy2)
            else:
                dst = np.zeros(img.shape)
                for i in range(img.shape[2]):
                    # cv2.imshow('fx'+str(i),np.uint8(fx[:,:,i]))
                    # cv2.imshow('fy'+str(i),np.uint8(fy[:,:,i]))
                    dst[:,:,i] = np.sqrt(fx[:,:,i]*fx[:,:,i] + fy[:,:,i]*fy[:,:,i])
                

            dst[dst>255] = 255
            # 不加就会在Image.fromarray报错
            dst = dst.astype(np.uint8)
            return dst

        # 进行变换
        img = Sobel_Sharpen(img)

        # 创建toplevel窗口
        try:
            SobelSharpenWin.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            SobelSharpenWin = tkinter.Toplevel()
            SobelSharpenWin.attributes('-topmost', True)
        SobelSharpenWin.geometry("360x240")
        SobelSharpenWin.resizable(True,True) # 可缩放
        SobelSharpenWin.title("Sobel锐化")
        
        LabelPic = tkinter.Label(SobelSharpenWin, text="IMG", width=360, height=240)

        image = ImageTk.PhotoImage(Image.fromarray(img))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(img, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    ################################################################################################################################

    # HOG人脸检测
    def HOGFaceRecognition():
        global FaceRecogWinn
        print("HOG人脸检测")
        filePath = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("BMP",".bmp")]) # 打开文件夹对话框

        if not filePath:
            tkinter.messagebox.showerror(message="Cannot open this file!")
            return
        
        if (is_chinese(filePath)):
            tkinter.messagebox.showerror(message="Cannot open this file because of Chinese Path!")
            return

        try:
            FaceRecogWinn.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            FaceRecogWinn = tkinter.Toplevel()
            FaceRecogWinn.attributes('-topmost', True)

        FaceRecogWinn.geometry("360x240")
        FaceRecogWinn.resizable(True,True) # 可缩放
        FaceRecogWinn.title("人脸检测")
        
        LabelPic = tkinter.Label(FaceRecogWinn, text="IMG", width=360, height=240)


        # 将jpg文件加载到numpy 数组中
        t=time.time()
        # 用于识别
        image = face_recognition.load_image_file(filePath)
        # 用于画框
        frame=cv2.imread(filePath)

        # 使用默认的给予HOG模型查找图像中所有人脸
        # 这个方法已经相当准确了，但还是不如CNN模型那么准确，因为没有使用GPU加速
        face_locations = face_recognition.face_locations(image)
         
        # 打印：我从图片中找到了 多少 张人脸
        print("I found {} face(s) in this photograph.".format(len(face_locations)))
         
        # 循环找到的所有人脸
        for face_location in face_locations:
                # 打印每张脸的位置信息
                top, right, bottom, left = face_location
                print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
                # 指定人脸的位置信息，然后显示人脸图片
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # cv2.imshow('tuxiang',frame)
        # cv2.waitKey(1)  #刷新界面 不然只会呈现灰色
        print('运行时间{}'.format(time.time()-t))

        frame = frame[:, :, ::-1]
        image = ImageTk.PhotoImage(Image.fromarray(frame))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(frame, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    # CNN人脸检测
    def CNNFaceRecognition():
        global FaceRecogWinn
        print("CNN人脸检测")
        filePath = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("BMP",".bmp")]) # 打开文件夹对话框

        if not filePath:
            tkinter.messagebox.showerror(message="Cannot open this file!")
            return
        
        if (is_chinese(filePath)):
            tkinter.messagebox.showerror(message="Cannot open this file because of Chinese Path!")
            return

        try:
            FaceRecogWinn.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            FaceRecogWinn = tkinter.Toplevel()
            FaceRecogWinn.attributes('-topmost', True)

        FaceRecogWinn.geometry("360x240")
        FaceRecogWinn.resizable(True,True) # 可缩放
        FaceRecogWinn.title("人脸检测")
        
        LabelPic = tkinter.Label(FaceRecogWinn, text="IMG", width=360, height=240)


        
        # 将jpg文件加载到numpy 数组中
        t=time.time()
        # 用于识别
        image = face_recognition.load_image_file(filePath)
        # 用于画框
        frame=cv2.imread(filePath)
         
        # 使用CNN模型
        face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
         
        # 打印：我从图片中找到了 多少 张人脸
        print("I found {} face(s) in this photograph.".format(len(face_locations)))
         
        # 循环找到的所有人脸
        for face_location in face_locations:
                # 打印每张脸的位置信息
                top, right, bottom, left = face_location
                print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
                # 指定人脸的位置信息，然后显示人脸图片
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        print('运行时间{}'.format(time.time()-t))

        frame = frame[:, :, ::-1]
        image = ImageTk.PhotoImage(Image.fromarray(frame))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(frame, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    # 虹软SDK人脸识别
    def ArcSoft():
        global FaceRecogWinn
        print("\n虹软SDK人脸检测")
        filePath = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("BMP",".bmp")]) # 打开文件夹对话框

        if not filePath:
            tkinter.messagebox.showerror(message="Cannot open this file!")
            return
        
        if (is_chinese(filePath)):
            tkinter.messagebox.showerror(message="Cannot open this file because of Chinese Path!")
            return

        try:
            FaceRecogWinn.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            FaceRecogWinn = tkinter.Toplevel()
            FaceRecogWinn.attributes('-topmost', True)

        FaceRecogWinn.geometry("360x240")
        FaceRecogWinn.resizable(True,True) # 可缩放
        FaceRecogWinn.title("虹软SDK")

        LabelPic = tkinter.Label(FaceRecogWinn, text="IMG", width=360, height=240)

        frame = detection(filePath)
        frame = frame[:, :, ::-1]
        image = ImageTk.PhotoImage(Image.fromarray(frame))
        LabelPic.image = image
        LabelPic['image'] = image
        # cv2.imshow('image', image)
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(frame, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    # face++人脸识别SDK
    def FacePPSDK():
        global FaceRecogWinn
        print("\nface++SDK人脸检测")
        filePath = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("BMP",".bmp")]) # 打开文件夹对话框

        if not filePath:
            tkinter.messagebox.showerror(message="Cannot open this file!")
            return
        
        if (is_chinese(filePath)):
            tkinter.messagebox.showerror(message="Cannot open this file because of Chinese Path!")
            return

        try:
            FaceRecogWinn.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            FaceRecogWinn = tkinter.Toplevel()
            FaceRecogWinn.attributes('-topmost', True)

        FaceRecogWinn.geometry("360x240")
        FaceRecogWinn.resizable(True,True) # 可缩放
        FaceRecogWinn.title("Face++SDK")

        LabelPic = tkinter.Label(FaceRecogWinn, text="IMG", width=360, height=240)

        frame = Facepp(filePath)
        frame = frame[:, :, ::-1]
        image = ImageTk.PhotoImage(Image.fromarray(frame))
        LabelPic.image = image
        LabelPic['image'] = image
        
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(frame, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return

    # paddlehub的PyramidBox_Lite模型
    def paddleHub1():
        global FaceRecogWinn
        print("\nPyramidBox_Lite人脸检测")
        filePath = filedialog.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("BMP",".bmp")]) # 打开文件夹对话框

        if not filePath:
            tkinter.messagebox.showerror(message="Cannot open this file!")
            return
        
        if (is_chinese(filePath)):
            tkinter.messagebox.showerror(message="Cannot open this file because of Chinese Path!")
            return

        try:
            FaceRecogWinn.destroy()    
        except Exception as e:
            print("NVM")
        finally:
            FaceRecogWinn = tkinter.Toplevel()
            FaceRecogWinn.attributes('-topmost', True)

        FaceRecogWinn.geometry("360x240")
        FaceRecogWinn.resizable(True,True) # 可缩放
        FaceRecogWinn.title("PyramidBox_Lite")

        LabelPic = tkinter.Label(FaceRecogWinn, text="IMG", width=360, height=240)

        frame = paddlePyramidBox_Lite(filePath)
        frame = frame[:, :, ::-1]
        image = ImageTk.PhotoImage(Image.fromarray(frame))
        LabelPic.image = image
        LabelPic['image'] = image
        
        def changeSize(event):
            image1 = ImageTk.PhotoImage(Image.fromarray(cv2.resize(frame, (event.width, event.height))))
            LabelPic.image = image1
            LabelPic['image'] = image1
        LabelPic.bind('<Configure>', changeSize)
        LabelPic.pack(fill=tkinter.BOTH, expand=tkinter.YES)

        return





####################################################################################################################################
####################################################################################################################################
######################################                    HELP CLASS                       #########################################
####################################################################################################################################
####################################################################################################################################


class HELP:
    '''
    帮助
    ['检查更新', '关于作者']
    '''
    def Update():
        res = tkinter.messagebox.showinfo(title='版本信息', message='\n更新日期: 2020/06/22\n软件版本: V1.0\n版权所有: 钟路迦')
        print(res)
        return

    def ABOUT():
        res = tkinter.messagebox.showinfo(title='作者信息', 
            message='\n开发人员: 钟路迦\n所在单位: CAU CIEE CS 172\n联系电话: *******2219\n邮箱: zljdanceholic@cau.edu.cn\nQQ: 93737****\n')
        print(res)
        return