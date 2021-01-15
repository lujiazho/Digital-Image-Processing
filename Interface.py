import tkinter
import tkinter.messagebox
from tkinter.constants import *

from PIL import Image, ImageTk
import cv2

from processing.ImgProcessing import *


class ttsx(object):
    def __init__(self,face1,tk,rate=-10):
        self.rate = rate
        self.panel = None
        self.face1 = face1 # 这个是传进来的frame()对象, 依赖于tk()对象
        self.SELF = tk # 这个是tk()对象

    def createICO(self):
        self.img1 = ImageTk.PhotoImage(Image.open('./images/house.jpg'))
        self.img2 = ImageTk.PhotoImage(Image.open('./images/bell.jpg'))
        self.img3 = ImageTk.PhotoImage(Image.open('./images/camera.jpg'))
        self.img4 = ImageTk.PhotoImage(Image.open('./images/cabinet.jpg'))

    # 绑定快捷键
    def AssertERRORToMakeFuckingICOShowing(self):
        # assert False
        # try:
        #     assert False
        #     raise NameError
        # except Exception as e:
        #     print("nvm")
        # assert False
        # raise NameError
        raise NotImplementedError

    # 创建菜单
    def createMenu(self):
        '''只支持两层嵌套'''
        menus = ['文件', '编辑', '工具', '帮助']
        items = [['打开', '保存', '另存为...'],

                 ['撤销', '-',  '剪切', '复制', '粘贴', '删除', '选择所有',['更多...','数据', '图表', '统计']],

                 [['灰度变换', 'n值化', '线性化', ['非线性化', '对数变换', '伽马变换']],
                  '绘制直方图', '图像相加', ['图像滤波', '均值滤波', '中值滤波'], '图像锐化',
                   ['人脸检测', 'HOG模型', 'CNN模型', '虹软SDK', 'face++SDK', 'PyramidBox_Lite']],

                 ['检查更新', '关于作者']]
        callbacks = [[FILE.dialog1, FILE.dialog2, FILE.dialog3],

                     [EDIT.dialog1, None, EDIT.dialog1, EDIT.dialog1, EDIT.dialog1,
                      EDIT.dialog1, EDIT.dialog1, [EDIT.dialog1, EDIT.dialog1, EDIT.dialog1]],

                    [[TOOLS.grey_n, TOOLS.grey_lin, [TOOLS.grey_lg, TOOLS.grey_gamma]], 
                    TOOLS.Hist_RGB, TOOLS.ImgPlus, [TOOLS.AvgFiltering, TOOLS.MedFiltering], TOOLS.Sobel_Sharpening, 
                    [TOOLS.HOGFaceRecognition, TOOLS.CNNFaceRecognition, TOOLS.ArcSoft, TOOLS.FacePPSDK, TOOLS.paddleHub1]],

                     [HELP.Update, HELP.ABOUT]]
        icos = [[self.img1, self.img2, self.img3],

                [self.img1, None, self.img2, self.img3, self.img2, self.img4, self.img2, [self.img3, self.img2, self.img4]],

                [[self.img1, self.img2, [self.img1, self.img3]], self.img3, self.img4, [self.img1, self.img2],
                 self.img2, [self.img3, self.img1, self.img2, self.img4, self.img3]],

                [self.img1, self.img2]]

        menubar = tkinter.Menu(self.SELF)
        # 创建每一个菜单项, 目前4个
        for i,x in enumerate(menus):
            m = tkinter.Menu(menubar, tearoff=0)
            # 创建每个菜单项的下拉项
            for item, callback, ico in zip(items[i], callbacks[i], icos[i]):
                # 如果这个下拉项还有嵌套项
                if isinstance(item, list):
                    sm = tkinter.Menu(menubar, tearoff=0)
                    # 就默认第一个是项名，后面的是嵌套项
                    for subitem, subcallback, subico in zip(item[1:], callback, ico):
                        # 继续判断是不是有嵌套项
                        if isinstance(subitem, list):
                            xm = tkinter.Menu(menubar, tearoff=0)
                            for subsubitem, subsubcallback, subsubico in zip(subitem[1:], subcallback, subico):
                                if subsubitem == '-':
                                    xm.add_separator()
                                else:
                                    xm.add_command(label=subsubitem, command=subsubcallback, image=subsubico, compound='left')
                            sm.add_cascade(label=subitem[0], menu=xm)
                        elif subitem == '-':
                            sm.add_separator()
                        else:
                            sm.add_command(label=subitem, command=subcallback, image=subico, compound='left')
                    m.add_cascade(label=item[0], menu=sm)
                elif item == '-':
                    m.add_separator()
                else:
                    m.add_command(label=item, command=callback, image=ico, compound='left')
            menubar.add_cascade(label=x, menu=m)
        self.SELF.config(menu=menubar)

    #初始化窗体
    def tkMain(self,title,h=400,w=300):
        self.SELF.title(title)
        self.SELF.geometry("565x350") # 桌子, 即tk()对象

        # 读入菜单要用的图片
        self.createICO()
        # 创建菜单
        self.createMenu()
        self.AssertERRORToMakeFuckingICOShowing()
