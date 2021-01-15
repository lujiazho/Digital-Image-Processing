# -*- coding:utf-8 -*-
import pickle  # 存放数据的模块
import tkinter
import tkinter.messagebox
import os
import sys

import Interface
# import win32com.client # 微软这个服务器
from tkinter.constants import *
from tkinter import filedialog
import tkinter.messagebox
import pyglet
import os
# from pydub import AudioSegment # 音频格式转换
from images.memory_pic import * # 导入图片
import base64 # 编码

# 注册功能函数
def usr_sign_up():
    # 用户信息数据 录入函数
    def sign_to_Python():
        # 获取输入信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        # 打开保存用户信息的文件
        try:
            with open("usrs_info.pickle", "rb") as usr_file:
                exist_usr_info = pickle.load(usr_file)
        # 如果没有 新建一个
        except FileNotFoundError:
            with open("usrs_info.pickle", "wb") as usr_file:  # with open with语句可以自动关闭资源
                usrs_info = {"admin": "admin"}  # 以字典的形式保存账户和密码
                pickle.dump(usrs_info, usr_file) # 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
                exist_usr_info = usrs_info
        # 密码两次输入不一致
        if np != npf:
            tkinter.messagebox.showerror("Error", "Password and confirm password must be the same!")
        # 账户已被注册过
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror("Error", "The user has already signed up! ")
        # 成功录入
        else:
            exist_usr_info[nn] = np
            with open("usrs_info.pickle", "wb") as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo("Welcome", "You have successfully signed up!")
            # 销毁新创建的顶级窗口
            window_sign_up.destroy()

    # 没有任何传入，新建顶级窗口 用于注册
    window_sign_up = tkinter.Toplevel()
    window_sign_up.geometry("350x200")
    window_sign_up.title("sign up window")
 
    # 设置用户名的StringVar
    new_name = tkinter.StringVar()
    new_name.set("example@python.com")

    # 在顶级窗口加Label 输入口
    tkinter.Label(window_sign_up, text="User name:").place(x=10, y=10)
    entry_new_name = tkinter.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)
 
    # 设置密码的StringVar
    new_pwd = tkinter.StringVar()
    # 添加密码输入口
    tkinter.Label(window_sign_up, text="Password:").place(x=10, y=50)
    entry_usr_pwd = tkinter.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)
 
    new_pwd_confirm = tkinter.StringVar()
    # 添加confirm输入口
    tkinter.Label(window_sign_up, text="Confirm password:").place(x=10, y=90)
    entry_usr_pwd_confirm = tkinter.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)
 
    # 确认注册按钮
    btn_confirm_sign_up = tkinter.Button(window_sign_up, text="Sign up", command=sign_to_Python)
    btn_confirm_sign_up.place(x=150, y=130)
 

# 在这里面设置了最初创建的tk()对象的size并将其传入initface类
class basedesk():
    def __init__(self,master):
        # 界面布局，master是传入的tk()对象
        self.window = master
        self.window.title("LOGIN WINDOW")
        self.window.geometry("450x300")
        self.window.iconphoto(False, tkinter.PhotoImage(file='./images/meCROP.png'))
        # 再把此tk()对象传入interface()
        initface(self.window)
                
class initface():
    def __init__(self,master):
    	# tk是最开始创建的tk()对象
        self.tk = master

        # 基准界面initface，对象是框架控件Frame，tk()是Frame的父容器
        # 框架（Frame）控件在屏幕上显示一个矩形区域，多用来作为容器
        self.initface = tkinter.Frame(self.tk, height=400, width=500)
        # pack是 布局管理模块
        self.initface.pack()

        # 第一张桌布，画布（Canvas）组件和 html5 中的画布一样，都是用来绘图的
        # 可以将图形，文本，小部件或框架放置在画布上
        self.canvas = tkinter.Canvas(self.initface, height=300, width=400)
        # 获取封面图片
        self.get_pic(welcome_gif, 'welcome.gif') # 创造图片
        # 创建图像
        self.image_file = tkinter.PhotoImage(file='welcome.gif')
        self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.pack(side='top')
        os.remove('welcome.gif') # 用完就删，生成的中间文件
        
        # 标签控件
        Label1 = tkinter.Label(self.initface, text='User name:')
        Label1.place(x=50, y=150)		# place也是一个位置管理方法
        # Label1.pack()

        # 标签控件
        self.Label2 = tkinter.Label(self.initface, text='Password name:')
        self.Label2.place(x=50, y=190)

        # 设置保存 账号密码的stringVar()对象
        self.var_usr_name = tkinter.StringVar()
        self.var_usr_name.set('example@python.com')		# 设置默认值
         
        self.var_usr_pwd = tkinter.StringVar()
        
        # 输入控件；用于显示简单的文本内容， textvariable是文本框的值，是一个StringVar()对象
        self.entry_usr_name = tkinter.Entry(self.initface, textvariable=self.var_usr_name)
        self.entry_usr_name.place(x=160, y=150)
        self.entry_usr_pwd = tkinter.Entry(self.initface, show='*', textvariable=self.var_usr_pwd)
        self.entry_usr_pwd.place(x=160, y=190)

        # login 按钮
        btn_login = tkinter.Button(self.initface, text="Login", command=self.usr_login)
        btn_login.place(x=170, y=230)

        # sign up 注册按钮
        btn_sign_up = tkinter.Button(self.initface, text="Sign up", command=usr_sign_up)
        btn_sign_up.place(x=270, y=230)
        # btn_sign_up.pack()

        # 退出程序按钮
        btn = tkinter.Button(self.initface, text='EXIT', command=self.change)
        btn.pack()

    # 获取封面图片的函数
    def get_pic(self, pic_code, pic_name):
        image = open(pic_name, 'wb')
        # 解码后写到当前文件下
        image.write(base64.b64decode(pic_code))
        image.close()

    # 点击登录后调用函数
    def usr_login(self):
        # 获取输入的 账户信息
        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()

        # 打开保存用户信息的文件
        try:
            with open("usrs_info.pickle", "rb") as usr_file:
                usrs_info = pickle.load(usr_file)
        # 如果没有 新建一个
        except FileNotFoundError:
            with open("usrs_info.pickle", "wb") as usr_file:  # with open with语句可以自动关闭资源
                usrs_info = {"admin": "admin"}  # 以字典的形式保存账户和密码
                pickle.dump(usrs_info, usr_file) # 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
     
        # 登录成功/失败 处理程序段
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tkinter.messagebox.showinfo(title="Welcome", message="How are you! " + usr_name)
                # 摧毁tk()对象下登录框架Frame(), 这样依赖于frame创建的所有canvas、按钮等等都也被摧毁
                self.initface.destroy()
                # 将tk()对象传入
                Interfaced(self.tk)
            else:
                tkinter.messagebox.showerror(message="Error,your password is wrong,try again")
        else:
            is_sign_up = tkinter.messagebox.askyesno("Welcome", "You have not sign up yet.Sign up today?")
            if is_sign_up:
                usr_sign_up()

    def change(self,):
        sys.exit(1)

 
class Interfaced():
    def __init__(self, master):
    	# 保存传入的tk()对象
        self.master = master
        # self.master.config(bg='blue')
        # sys.exit(1)
        # 依赖于最初的tk()创建一个新的框架对象frame()
        self.face1 = tkinter.Frame(self.master,)
        self.face1.pack()
        # btn_back = tkinter.Button(self.face1,text='face1 back',command=self.back)
        # btn_back.pack()
        # 将此框架和tk()传入Interface.py文件中的ttsx类
        ttx = Interface.ttsx(self.face1, self.master)
        # 调用该类的tkMain函数，进行初始化窗体操作
        ttx.tkMain("My Digital Image Processing")
    
    def back(self):
        self.face1.destroy()
        initface(self.master)
        
    
if __name__ == '__main__':
    root = tkinter.Tk()
    basedesk(root)
    # 窗体主循环
    root.mainloop()