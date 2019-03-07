# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import tesserocr
import bs4
import re
from PIL import Image
from bs4 import BeautifulSoup
import time
import pickle
session = requests.Session()
t = time.localtime()
if t[1] >= 8 :
    School_Year = t[0] + 1
    School_Term = 1
else:
    School_Year = t[0]
    School_Term = 2

class_type_data_dict = {'1':'全校公共必修课','2':'全校公共选修课','3':'专业平台必修课','4':'专业平台选修课','5':'专业模块必修课',
                    '6':'专业模块选修课','7':'课外必修课','20':'通识核心课程','21':'学科(专业)基础课程','22':'专业核心课程必修',
                    '26':'专业核心课程选修','23':'专业拓展课程必修','25':'专业拓展课程选修','27':'素质拓展必修','28':'素质拓展选修'}
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from Ui_Login import Ui_MainWindow
from Ui_main import Ui_Dialog
from Ui_yucuankebiao import Ui_Dialog1
from Ui_chakankebiao import Ui_Dialog2
from Ui_guanyu import Ui_Dialog3
from Ui_zizhuxuanke import Ui_Dialog4

def denglu(name, password):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host': '210.42.38.26:81'
    }
    url_login = "http://210.42.38.26:84/jwc_glxt/"  # 登录页面链接
    html = session.get(url_login, headers=header)  # 获取登录页面
    # print(html.cookies)
    soup = bs4.BeautifulSoup(html.text, 'lxml')
    # print(soup)
    __VIEWSTATE = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']  # 找到提交两个参数
    __EVENTVALIDATION = soup.find('input', attrs={'name': '__EVENTVALIDATION'})['value']  # 找到提交两个参数
    # print(__VIEWSTATE)
    # print(__EVENTVALIDATION)
    # print(html.headers)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host': '210.42.38.26:81',
    }
    while 1:
        r = session.get("http://210.42.38.26:84/jwc_glxt/ValidateCode.aspx", headers=header)  # 获取验证码
        # print(r.cookies)
        with open('ValidateCode.jpg', 'wb') as f:
            f.write(r.content)  # 保存验证码图片
        image = Image.open('ValidateCode.jpg')
        resultjpg = tesserocr.image_to_text(image)  # 识别验证码图片
        resultjpg = resultjpg.replace(' ', '')
        resultjpg = resultjpg.replace('.', '')
        # print(len(resultjpg))
        # print(resultjpg)
        if len(resultjpg) == 5:
            break
    name = name
    # print(name)
    password = password
    # print(password)
    data = {'__VIEWSTATE': __VIEWSTATE,
            '__VIEWSTATEGENERATOR': 'CC6531A5',
            '__EVENTVALIDATION': __EVENTVALIDATION,
            'txtUserName': name,
            'btnLogin.x': '52',
            'btnLogin.y': '12',
            'txtPassword': password,
            'CheckCode': resultjpg
            }  # 构造提交表单
    # print(data)
    login_url = 'http://210.42.38.26:84/jwc_glxt/Login.aspx?xttc=1'  # 登录地址
    html = session.post(login_url, data=data, headers=header)
    chlick_login = re.findall('<div.*?table_bgcolor.*?<h2>(.*)</h2>', html.text, re.S)
    # print(len(chlick_login))
    # print(chlick_login)
    if len(chlick_login) == 0:
        return 0
    else:
        return 1
def zidongpingjiao():#自动评教
    y = 1
    m = 0
    while y ==1:
        url = 'http://210.42.38.26:84/jwc_glxt/Stu_Assess/Stu_Assess.aspx'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Referer': 'http://210.42.38.26:84/jwc_glxt/Stu_Notice/Notice_Query.aspx',
            'Host': '210.42.38.26:84'
        }
        html = session.get(url, headers=header)
        #print(html.text)
        results = re.findall('<div.*?GridViewStyle.*?<td.*?open.*?id=(\d{7}).*?</a>', html.text, re.S)
        if len(results) == 0:
            m = 0
            return m
            #print("评教已完成")
            break
        else:
            m = m + 1
            #print(results[0])
            for result in results:
                url_get = 'http://210.42.38.26:84/jwc_glxt/Stu_Assess/Stu_Assess_Proc.aspx?id=' + results[0]
                #print(url_get)
                html_chlick = session.get(url_get)
                soup = bs4.BeautifulSoup(html_chlick.text, 'lxml')
                __VIEWSTATE1 = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
                __EVENTVALIDATION1 = soup.find('input', attrs={'name': '__EVENTVALIDATION'})['value']
                header1 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                    'Host': '210.42.38.26:84'
                }
                html_chlick = session.get(url_get, headers=header1)
                data = {
                    '__VIEWSTATE': __VIEWSTATE1,
                    '__EVENTVALIDATION': __EVENTVALIDATION1,
                    'GridCourse2$ctl02$userscore': '5',
                    'GridCourse2$ctl03$userscore': '5',
                    'GridCourse2$ctl04$userscore': '5',
                    'GridCourse2$ctl05$userscore': '5',
                    'GridCourse2$ctl06$userscore': '5',
                    'GridCourse2$ctl07$userscore': '5',
                    'GridCourse2$ctl08$userscore': '5',
                    'GridCourse2$ctl09$userscore': '5',
                    'SuitTeach': 'RadioButton1',
                    'TeacherGood': '',
                    'TeacherChange': '',
                    'btnSave': '确定'
                }
                #print(data)
                html1 = session.post(url_get, headers=header1, data=data)
                return m
                #print(html1)
def chengjichaxun(year,term):#成绩查询
    #print(1)
    ulist = []
    url = 'http://210.42.38.26:84/jwc_glxt/Student_Score/Score_Query.aspx'  # 成绩查询页面url
    header = {
        'Referer': 'http://210.42.38.26:81/jwc_glxt/Stu_Notice/Notice_Query.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host': '210.42.38.26:81'
    }
    r = session.get(url, headers = header)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup_class = bs4.BeautifulSoup(r.text, 'lxml')  # 得到网页
    __VIEWSTATE = soup_class.find('input', attrs={'name': '__VIEWSTATE'})['value']
    __EVENTVALIDATION = soup_class.find('input', attrs={'name': '__EVENTVALIDATION'})['value']
    #print (r)
    data = {
        '__VIEWSTATE':__VIEWSTATE,
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__EVENTVALIDATION':__EVENTVALIDATION,
        'ctl00$MainContentPlaceHolder$School_Year':year,
        'ctl00$MainContentPlaceHolder$School_Term':term,
        'ctl00$MainContentPlaceHolder$score_q':'RadioButton2',
        'ctl00$MainContentPlaceHolder$BtnSearch.x': '20',
        'ctl00$MainContentPlaceHolder$BtnSearch.y': '4'
    }
    #print(data)
    header = {
        'Referer': 'http://210.42.38.26:84/jwc_glxt/Student_Score/Score_Query.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host': '210.42.38.26:81'
    }
    html = session.post(url,headers = header,data = data)
    html.raise_for_status()
    html.encoding = r.apparent_encoding
    #html.text
    #print(html.text)
    y = 0
    soup = BeautifulSoup(html.text, 'lxml')
    for soup1 in soup.find_all(attrs={'class': 'GridViewStyle'}):
        for tr in soup1.find_all(name='tr'):
            if isinstance(tr, bs4.element.Tag):  # 除去不是bs4库定义的标签类型的tr
                tds = tr('td')  # 将"tr"标签中的"td"的值存入"tds"
                if len(tds) == 0:
                    pass
                else:
                    ulist.append(
                        [tds[0].string, tds[1].string, tds[2].string, tds[3].string, tds[4].string, tds[5].string,
                         tds[6].string, tds[7].string])
                    y = y + 1
        # print(ulist)
    tplt = "{0:^2}\t{1:^3}\t{2:^35}\t{3:^5}\t{4:^5}\t{5:^5}\t{6:^5}\t{7:^5}"
    #print(tplt.format("学年", "学期", "课程名称", "课程学分", "考试类型", "考试成绩", "所获学分", "课程代码", chr(12288)))
    return y,ulist
    #for i in range(y):
        #u = ulist[i]
        #print(tplt.format(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], chr(12288)))

def save_code(name,password):
    save_code1 = {'usr_name':name,'usr_pwd':password}
    try:
        with open('save_dome.kpl', 'rb') as fl:
            data = pickle.load(fl)
        fl.close()
        data = dict(data)
        #print(data)
    except:
        data = {'psd':'False','atom':'False'}
        pass
    if data['psd'] == 'True':
        with open('save_code.kpl', 'wb') as fl:
            pickle.dump(save_code1, fl)
        fl.close()
def save_dome(dome):
    save_dome1 = {'psd':'False','atom':'False'}
    if dome == 1:
        save_dome1['psd'] = 'True'
    elif dome == 2:
        save_dome1['atom'] = 'True'
    with open('save_dome.kpl', 'wb') as fl:
        pickle.dump(save_dome1, fl)
    fl.close()
def save_class(leibie,mingcheng,num):
    for i in range(3):
        while 1:
            if leibie[i] == '全校公共必修课':
               leibie[i] = 1
               break
            elif leibie[i] == '全校公共选修课':
                leibie[i] = 2
                break
            elif leibie[i] == '专业平台必修课':
                leibie[i] = 3
                break
            elif leibie[i] == '专业平台选修课':
                leibie[i] = 4
                break
            elif leibie[i] == '专业模块必修课':
                leibie[i] = 5
                break
            elif leibie[i] == '专业模块选修课':
                leibie[i] = 6
                break
            elif leibie[i] == '课外必修课':
                leibie[i] = 7
                break
            elif leibie[i] == '通识核心课程':
                leibie[i] = 20
                break
            elif leibie[i] == '学科(专业)基础课程':
                leibie[i] = 21
                break
            elif leibie[i] == '专业核心课程必修':
                leibie[i] = 22
                break
            elif leibie[i] == '专业核心课程选修':
                leibie[i] = 26
                break
            elif leibie[i] == '专业拓展课程必修':
                leibie[i] = 23
                break
            elif leibie[i] == '专业拓展课程选修':
                leibie[i] = 25
                break
            elif leibie[i] == '素质拓展必修':
                leibie[i] = 27
                break
            else:
                leibie[i] = 28
                break
        save_class1 = [leibie,mingcheng,num]
        try:
            with open('save_class.kpl', 'wb') as f:
                pickle.dump(save_class1,f)
            f.close()
        except:
            pass
def tishixinxi(self):
    #print(1)
    try:
        with open('save_class.kpl', 'rb') as f:
            data = pickle.load(f)
        f.close()
    except:
        pass
    if len(data) == 0:
        #print(2)
        dome_num = QMessageBox.warning(self, '警告', '你还没有设置预选课表，是否去设置', QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        # print(dome_num)
        if dome_num == 16384:
            dome = Dialog1()
            dome.exec_()
    else:
        #print(data)
        dome_a = Dialog2()
        dome_a.exec_()
def jingruxitong():
    #print(1)
    url_choice_class = 'http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choice.aspx'
    while 1:  # 进入系统尝试
        header_choice1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': '210.42.38.26:84',
            'Referer': 'http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choice.aspx'
        }
        html_chooice_class = session.get(url_choice_class, headers=header_choice1)  # 相当于点击学生选课
        soup_class = bs4.BeautifulSoup(html_chooice_class.text, 'lxml')  # 得到网页
        __VIEWSTATE2 = soup_class.find('input', attrs={'name': '__VIEWSTATE'})['value']
        __EVENTVALIDATION2 = soup_class.find('input', attrs={'name': '__EVENTVALIDATION'})['value']  # 分析页面参数
        # print(html_chooice_class.text)
        for soup1 in soup_class.find_all(attrs={'class': 'table_bgcolor'}):
            for td1 in soup1.find_all(name='h2'):
                tds1 = td1.string
        if tds1 == '学生选课系统':
            #print("成功进入选课系统！")
            return 1,__VIEWSTATE2,__EVENTVALIDATION2
            break
def kaishixuanke(self,__VIEWSTATE2,__EVENTVALIDATION2,class_type,class_name,class_number):
        url_choice_class = 'http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choice.aspx'
        jishu = 0
        xuankechenggongjishu = 0
        define_rusult = []
        header_choice1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': '210.42.38.26:84',
            'Referer': 'http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choice.aspx'
        }
        while jishu < 3:
            data_class_choice = {
                '__VIEWSTATE': __VIEWSTATE2,
                '__EVENTVALIDATION': __EVENTVALIDATION2,
                'ctl00$MainContentPlaceHolder$School_Year': School_Year,
                'ctl00$MainContentPlaceHolder$School_Term': School_Term,
                'ctl00$MainContentPlaceHolder$Course_Type': class_type[jishu],
                'ctl00$MainContentPlaceHolder$BtnSearch.x': '23',
                'ctl00$MainContentPlaceHolder$BtnSearch.y': '15'
            }  # 进入课程类别详情页面数据提交
            html_class_choice = session.post(url_choice_class, data=data_class_choice,headers=header_choice1)  # 提交数据——课程类别详情页面
            #print(html_class_choice.text)
            soup_class1 = bs4.BeautifulSoup(html_class_choice.text, 'lxml')  # 分析网页查看该页面所有数据
            __VIEWSTATE3 = soup_class1.find('input', attrs={'name': '__VIEWSTATE'})['value']
            __EVENTVALIDATION3 = soup_class1.find('input', attrs={'name': '__EVENTVALIDATION'})['value']
            # print(__EVENTVALIDATION2)
            ulist_chooices = []
            y = 0
            for soup2 in soup_class1.find_all(attrs={'class': 'GridViewStyle'}):
                for td2 in soup2.find_all(name='td'):
                    tds2 = td2.string
                    # print(tds)
                    l = "".join(tds2)
                    i = 0
                    tds2 = ""
                    while i <= len(l):
                        if i == len(l):
                            break
                        else:
                            tds2 = tds2 + l[i]
                            i = i + 1
                    ulist_chooices.append(tds2)
                    y = y + 1
                # print(ulist_chooices)
            x = 1
            list1 = []
            while x != y + 1:
                list1.append(ulist_chooices[x])
                #print(ulist_chooices[x])
                x = x + 2
            l = 0
            class_choice_name = class_name[jishu]
            #print(class_choice_name)
            for z in list1:
                if z == class_choice_name:
                    break
                else:
                    l = l + 1
            show = 'show$' + str(l)
            data_class = {
                '__EVENTTARGET': 'ctl00$MainContentPlaceHolder$Course_Group',
                '__EVENTARGUMENT': show,
                '__VIEWSTATE': __VIEWSTATE3,
                '__EVENTVALIDATION': __EVENTVALIDATION3,
                'ctl00$MainContentPlaceHolder$School_Year': School_Year,
                'ctl00$MainContentPlaceHolder$School_Term': School_Term,
                'ctl00$MainContentPlaceHolder$Course_Type': class_type
            }
            html_class_choice1 = session.post(url_choice_class, data=data_class, headers=header_choice1)  # 课程详情页面
            # soup12 = bs4.BeautifulSoup(html_class_choice1.text, 'lxml')
            # print(data_class)
            # print(soup12)
            # reluite_class_choice = re.findall('<div.*?table_bgcolor.*?GridViewStyle.*?ctl00_MainContentPlaceHolder_GridCourse.*?<a.*?href=(.*)target.*?</a>',html_class_choice1.text, re.S)
            # reluite_class_choice = reluite_class_choice[0][1:-2]
            # print(reluite_class_choice)
            #print('请输入详细课程名称')
            class_choice_name = class_name[jishu] +  '  ('+ class_number[jishu] + '班)' #'形势与政策(六)  (1班)'
            soup_class2 = BeautifulSoup(html_class_choice1.text, "lxml")
            class_choice_name_url1 = '1'
            for soup3 in soup_class2.find_all(attrs={'id': 'ctl00_MainContentPlaceHolder_GridCourse'}):
                for tr3 in soup3.find_all(name='tr'):
                    td3 = tr3('td')
                    if len(td3) == 0:
                        pass
                    else:
                        tds3 = td3
                        #print('正在为你选取',class_choice_name,'课程')
                        if class_choice_name == tds3[0].string:
                            class_choice_name_url = tds3[5]
                            # print(class_choice_name_url)
                            class_choice_name_url1 = str(class_choice_name_url)[33:-29]
                            break
                            #print(class_choice_name_url1)
                        else:
                            pass
            if class_choice_name_url1 == '1':
                QMessageBox.warning(self,'警告','由于课程名称或者班级错误导致一门课选课失败')
            else:
                reluite_class_choice = "http://210.42.38.26:84/jwc_glxt/Course_Choice/" + class_choice_name_url1
                html_class_choice2 = session.get(reluite_class_choice, headers=header_choice1)
                # print(html_class_choice2)
                soup_class3 = BeautifulSoup(html_class_choice2.text, 'lxml')
                # print("已经选了", jishu + 1, "门课了")
                for soup4 in soup_class3.find_all(name='script'):
                    soup4 = soup4.string[7:-3]
                    if soup4[0] == '恭':
                        #print(soup4)
                        xuankechenggongjishu = xuankechenggongjishu + 1
                    else:
                        define_rusult.append(soup4)
                        #print(soup4)
            jishu = jishu + 1
            url = 'http://210.42.38.26:84/jwc_glxt/Student_Score/Score_Query.aspx'  # 成绩查询页面url
            header = {
                'Referer': 'http://210.42.38.26:84/jwc_glxt/Course_Choice/Course_Choice.aspx',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                'Host': '210.42.38.26:81'
            }
            r = session.get(url, headers=header)
            header_choice1 = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                'Host': '210.42.38.26:84',
                'Referer': 'http://210.42.38.26:84/jwc_glxt/Student_Score/Score_Query.aspx'
            }
            html_chooice_class = session.get(url_choice_class, headers=header_choice1)  # 相当于点击学生选课
            soup_class = bs4.BeautifulSoup(html_chooice_class.text, 'lxml')  # 得到网页
            __VIEWSTATE2 = soup_class.find('input', attrs={'name': '__VIEWSTATE'})['value']
            __EVENTVALIDATION2 = soup_class.find('input', attrs={'name': '__EVENTVALIDATION'})['value']  # 分析页面参数
        #print('成功选取', xuankechenggongjishu, '门课')
        #print('选取失败',jishu-xuankechenggongjishu,'门课')
        return define_rusult,xuankechenggongjishu,jishu-xuankechenggongjishu
class Dialog4(QDialog,Ui_Dialog4):#自助选课
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.label_3.hide()
class Dialog3(QDialog,Ui_Dialog3):#关于窗口
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
class Dialog2(QDialog,Ui_Dialog2):#查看课表窗口
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        with open('save_class.kpl', 'rb') as f:
            data = pickle.load(f)
        f.close()
        data1=data[0]
        data2=data[1]
        data3=data[2]
        #print(data[0],data[1],data[2])
        for i in range(3):
            Value = class_type_data_dict[str(data1[i])]
            self.tableWidget.setItem(i+1, 0, QTableWidgetItem(Value))
            Value = data2[i]
            self.tableWidget.setItem(i+1, 1, QTableWidgetItem(Value))
            Value = data3[i]
            self.tableWidget.setItem(i+1, 2, QTableWidgetItem(Value))

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.close()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.close()
        dome = Dialog1()
        dome.exec_()
class Dialog1(QDialog,Ui_Dialog1): #预选课表窗口
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        leibie = []
        mingcheng = []
        num = []
        leibie.append(self.comboBox.currentText())
        mingcheng.append(self.lineEdit.text())
        num.append(self.spinBox.text())
        leibie.append( self.comboBox_2.currentText())
        mingcheng.append( self.lineEdit_2.text())
        num.append(self.spinBox_2.text())
        leibie.append(self.comboBox_3.currentText())
        mingcheng.append(self.lineEdit_3.text())
        num.append(self.spinBox_3.text())
        save_class(leibie,mingcheng,num)
        QMessageBox.information(self,'通知','预选课表已保存！')
        self.close()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        push_check = QMessageBox.warning(self,'提示','是否保存课表!',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        #print(push_check)
        if push_check == 16384:
            self.pushButton.click()
        else:
            self.close()
class  Dialog(QDialog,Ui_Dialog): #主窗口
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet('''QDialog{background: #494A5F;color: #D5D6E2;font-weight: 500;font-size: 1.05em;font-family: "Microsoft YaHei","宋体","Segoe UI", "Lucida Grande", Helvetica, Arial,sans-serif, FreeSans, Arimo;}''')
        self.label.setStyleSheet('''QLabel{color:#d5d6e2;font-weight:500;font-size:35px;font-family:"Microsoft YaHei","宋体","Segoe UI","Lucida Grande",Helvetica,Arial,sans-serif,FreeSans,Arimo}''')
        self.frame.setStyleSheet('''QFrame{background-color:rgba(125, 0, 0, 70%)}''')
        #self.frame_2.setStyleSheet('''QFrame{background-color:rgba(125, 0, 0, 60%)}''')
        self.pushButton.setStyleSheet('''QPushButton{font-family:'微软雅黑',
    font-size: 13px!important,
	height: 30px,
	line-height: 18px!important,
	padding: 3px 18px,
	display: inline-block00,
	vertical-align: middle,
	font-weight: normal,
	border-radius: 2px,
	margin: 0 8px 0 3px,
	border: 1px solid #3383da,
	color: #ffffff,
	background-color: #3383da}''')
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        while 1:
            dome = zidongpingjiao()
            #print(type(dome))
        #print(dome)
            if dome != 0:
                dome_tex = "已成功评教",dome,"门课程"
                self.label_4.setText(dome_tex)
                self.label_4.show()
            else:
                QMessageBox.information(self, '通知', '评教已完成')
                self.label_3.hide()
                break

    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        year = self.comboBox.currentText()
        #print(year)
        if self.comboBox_2.currentIndex() == 0:
            term = 1
        else:
            term = 3
        #print(term)
        dome = chengjichaxun(year,term)
        #print(type(dome))
        #print(dome[0])
        self.tableWidget.setRowCount(dome[0])
        list_dome =dome[1]
        for i in range(dome[0]):
            for j in range(8):
                Value = list_dome[i][j]
                self.tableWidget.setItem(i, j, QTableWidgetItem(Value))
        #print(dome)

    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        sezhikebiao = Dialog1()
        sezhikebiao.exec_()
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        tishixinxi(self)


    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        guanyu = Dialog3()
        guanyu.exec_()

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        self.close()

    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        with open('save_class.kpl', 'rb') as f:
            data = pickle.load(f)
        f.close()
        class_type = data[0]
        class_name = data[1]
        class_number= data[2]
        xuanke = Dialog4()
        xuanke.exec_()
        dome = jingruxitong()
        if dome[0] == 1:
            xuanke.label_2.setText('成功进入选课系统')
            dome = kaishixuanke(self,dome[1],dome[2],class_type,class_name,class_number)
            dome_result = dome[0]
            dome_success = dome[1]
            dome_defint = dome[2]
            dome_success = '你已经成功选取'+dome_success+'门课程！'
            xuanke.label_2.setText(dome_success)
            dome_faide = '有'+dome_defint+'门课程选课失败,由于'+dome_result
            xuanke.label_3.show()
            xuanke.label_3.setText(dome_faide)
        else:
            QMessageBox.information(xuanke,'通知','选课系统未处在规定开放时间内')
            xuanke.label_2.hide()

class MainWindow(QMainWindow, Ui_MainWindow): #登录窗口
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_checkBox_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        save_dome(1)
    
    @pyqtSlot()
    def on_checkBox_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        save_dome(2)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        name = self.lineEdit.text()
        passwoed = self.lineEdit_2.text()
        dome = denglu(name,passwoed)
        #print(dome)
        if dome == 1:
            QMessageBox.information(self,'通知','登录成功！')
            save_code(name,passwoed)
            self.close()
            my_main = Dialog()
            my_main.exec_()
        else:
            QMessageBox.critical(self,'警告','学号或密码输入错误！')

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    ui.show()
    sys.exit(app.exec_())