#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import time
from translate import Translator

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("老郑中英中日互译小工具")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        self.init_window_name["bg"] = "RoyalBlue"                #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="要翻译的内容")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.yingfanzhongbutton = Button(self.init_window_name, text="英翻中", bg="lightblue", width=10,command=self.yingfanzhong)  # 调用内部方法  加()为直接调用
        self.yingfanzhongbutton.grid(row=1, column=11)

        self.zhongfanyingbutton = Button(self.init_window_name, text="中翻英", bg="lightblue", width=10,
                                              command=self.zhongfanying)  # 调用内部方法  加()为直接调用
        self.zhongfanyingbutton.grid(row=2, column=11)

        self.zhongfanributton = Button(self.init_window_name, text="中翻日", bg="lightblue", width=10,
                                         command=self.zhongfanri)  # 调用内部方法  加()为直接调用
        self.zhongfanributton.grid(row=3, column=11)

        self.rifanzhongbutton = Button(self.init_window_name, text="日翻中", bg="lightblue", width=10,
                                       command=self.rifanzhong)  # 调用内部方法  加()为直接调用
        self.rifanzhongbutton.grid(row=4, column=11)


    #功能函数

    # 下方为翻译使用的正确代码

    # 在任何两种语言之间，中文翻译成英文
    def zhongfanying(self):
        fanyizh = self.init_data_Text.get(1.0, END)
        self.translator = Translator(from_lang="chinese", to_lang="english")
        translation = self.translator.translate(fanyizh)
        # 输出到界面
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, translation)
        self.write_log_to_Text("翻译成功~！")


    # 在任何两种语言之间，中文翻译成英文
    def zhongfanri(self):
        fanyizhw =self.init_data_Text.get(1.0, END)
        self.translator = Translator(from_lang="chinese", to_lang="japanese")
        translation =self.translator.translate(fanyizhw)
        # 输出到界面
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, translation)
        self.write_log_to_Text("翻译成功~！")

    # 在任何两种语言之间，中文翻译成英文
    def rifanzhong(self):
        fanyijp = self.init_data_Text.get(1.0, END)
        self.translator = Translator(from_lang="japanese", to_lang="chinese")
        translation = self.translator.translate(fanyijp)
        # 输出到界面
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, translation)
        self.write_log_to_Text("翻译成功~！")


    def yingfanzhong(self):
        fanyien = self.init_data_Text.get(1.0, END)
        self.translator = Translator(from_lang="english", to_lang="chinese")
        translation = self.translator.translate(fanyien)
        # 输出到界面
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, translation)
        self.write_log_to_Text("翻译成功~！")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

gui_start()