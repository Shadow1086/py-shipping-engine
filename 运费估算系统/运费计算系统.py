from time import localtime
import datetime
from tkinter import *
from tkinter import messagebox
import re
import math

try:
    with open('user.txt', 'r', encoding='utf8') as f:
        pass
except FileNotFoundError:
    with open('user.txt', 'w', encoding='utf8') as f:
        f.write('\n')

try:
    with open('history.txt', 'r', encoding='utf8') as f:
        pass
except FileNotFoundError:
    with open('history.txt', 'w', encoding='utf8') as f:
        f.write('用户名 时间 重量 金额')

#第一界面   登录
class Page1(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.layout1()
#登录页面布局
    def layout1(self):
#用户名提示
        self.label01 = Label(self,text='用户名',width=12,height=1,borderwidth=1,relief='solid').grid(row=0,column=0,padx=5,pady=5)

#取得用户名输入
        #StringVar 变量

        self.entry01=Entry(self,fg='grey',width=30)
        self.entry01.insert(0,'用户名中需要同时拥有字母和数字')
        self.entry01.bind('<FocusIn>',self.on_entry01_click)
        self.entry01.bind('<FocusOut>',self.on_entry01_out)
        self.entry01.grid(row=0,column=1,columnspan=3)

#密码提示
        self.label02 = Label(self,text='密码',relief="solid",borderwidth=1,width=12,height=1).grid(row=1,column=0,pady=5)
#获得密码输入
        self.entry02  = Entry(self,fg='grey',width=30)
        self.entry02.insert(0,'密码中需要同时包含大小写字母和数字')
        self.entry02.bind("<FocusIn>",self.on_entry02_click)
        self.entry02.bind("<FocusOut>",self.on_entry02_out)
        self.entry02.grid(row=1,column=1,columnspan=3,pady=5)

#登录按钮
        self.bin01 = Button(self, text='登录',width=9)
        self.bin01['command'] = self.log_in
        self.bin01.grid(row=2,column=1,columnspan=3,pady=5,padx=5)
#退出按钮
        self.bin02  =Button(self,text = '退出',command=app.destroy,width=9)
        self.bin02.grid(row=2,column=0,columnspan=2,pady=5,padx=5)
#注册按钮
        self.bin03 = Button(self,text='注册',width=10)
        self.bin03.bind('<Button-1>',self.sign_up)
        self.bin03.grid(row=3,column=1,pady=5)
#用户登录 管理员登录
    def log_in(self):
        self.name = self.entry01.get()
        self.key = self.entry02.get()
        if self.name =='manager01' and self.key == 'Manager01':
            return(self.into_mana_page())
        else:
            with open(r'user.txt', 'r', encoding='utf8') as f:
                if (f'用户名：{self.name},密码：{self.key}\n') in f.readlines():
                    self.into_page2()
                else:
                    messagebox.showinfo('Failure','try again')

    def into_mana_page(self):
        self.pack_forget()
        self.mana_page = Mana_page(self.master)
#提示文字
    def on_entry01_click(self,event):
        if self.entry01.get()=='用户名中需要同时拥有字母和数字':
            self.entry01.delete(0,'end')
            self.entry01.config(fg='black')
    def on_entry01_out(self,event):
        if self.entry01.get()=='':
            self.entry01.insert(0,'用户名中需要同时拥有字母和数字')
            self.entry01.config(fg='grey')

    def on_entry02_click(self,event):
        if self.entry02.get()=='密码中需要同时包含大小写字母和数字':
            self.entry02.delete(0,'end')
            self.entry02.config(fg='black',show='*')
    def on_entry02_out(self,event):
        if self.entry02.get()=='':
            self.entry02.insert(0,'密码中需要同时包含大小写字母和数字')
            self.entry02.config(fg='grey',show='')
#注册
    def sign_up(self, event):
        self.top01 = Toplevel(self.master)
        self.top01.geometry('300x250+900+450')
        self.top01.title('注册')
    #用户名提示
        label01 = Label(self.top01,text='用户名',relief="solid",width=12,height=1)
        label01.pack(pady=5)

        self.entry_01=StringVar()
        entry01=Entry(self.top01,textvariable=self.entry_01)
        entry01.pack(pady=5)

        label03 = Label(self.top01,text='用户名中需带有字母和数字',width=30,fg='grey')
        label03.pack()
    #密码提示
        label02 = Label(self.top01, text='密码',width=12,height=1,relief='solid')
        label02.pack(pady=5)

        self.entry_02 = StringVar()
        entry02 = Entry(self.top01, textvariable=self.entry_02,show='*')
        entry02.pack(pady=5)

        label04 = Label(self.top01,text='密码中需要同时包含大小写字母和数字',fg='grey')
        label04.pack()
    #完成提示
        bin01 = Button(self.top01,text='完成')
        bin01['command']=self.keep_in_file
        bin01.pack()

#注册后保存至文件
    def keep_in_file(self):
        name = str(self.entry_01.get())
        key = str(self.entry_02.get())
        username_pattern = r'(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+'
        # 密码必须包含大小写字母和数字
        password_pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]+'
        if re.fullmatch(username_pattern, name) and re.fullmatch(password_pattern, key):
            with open('user.txt', 'r', encoding='utf8') as f :
                for line in f.readlines():
                    if name not in line :
                        pass
                    else :
                        return(messagebox.showinfo('Failure', '用户名已被注册，请重新命名'))
            with open('user.txt', 'a', encoding='utf8') as f:
                f.write(f'用户名：{name},密码：{key}\n')
            messagebox.showinfo('Welcome','注册成功')
            self.top01.destroy()
        else:
            messagebox.showinfo('Failure','注册失败，请检查用户名或密码的格式是否正确')
#登陆成功进入第二界面
    def into_page2(self):
        self.pack_forget()
        self.page2=Page2(self.master,self.name)
#第二界面   计算主程序
class Page2(Frame):
    def __init__(self,window,name):
        super().__init__(window)
        self.window=window
        self.name = name
        self.labels = []
        self.window.title('计算')
        self.window.geometry('300x150+500+350')
        self.pack()
        self.layout2()

#第二界面布局
    def layout2(self):
    #获取重量
        label01 = Label(self, text='重量',relief='solid',width=10).grid(row=0,column=0,padx=5,pady=5)
        self.entry01 = Entry(self, fg='grey')
        self.entry01.insert(0, '单位：公斤(kg)')
        self.entry01.bind('<FocusOut>', self.on_entry_out_01)
        self.entry01.bind('<FocusIn>', self.on_entry_click_01)
        self.entry01.grid(row=0,column=1,padx=5,pady=5)


    #获得地址
        label02 = Label(self, text='收货地址',relief="solid",width=10).grid(row=1,column=0,padx=5,pady=5)

        self.entry02 = Entry(self,fg='grey')
        self.entry02.insert(0,'xx省xx市xxx')
        self.entry02.bind('<FocusIn>',self.on_entry_click_02)
        self.entry02.bind('<FocusOut>',self.on_entry_out_02)
        self.entry02.grid(row=1,column=1,padx=5,pady=5)

    # 确定按钮
        bin01 = Button(self,text='确定',width=10)
        bin01.bind('<Button-1>',self.bin01_command)
        bin01.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
    #个人中心
        self.bin02 = Button(self,text = '个人中心',width=10)
        self.bin02.grid(row=6,column=0,padx=5,pady=5)
        self.bin02['command']=self.into_personal_space
#进入体积计算
        self.bin03 = Button(self,text='切换为体积计算',width=20)
        self.bin03.grid(row=6,column=1,columnspan=3,pady=5)
        self.bin03['command']=self.into_page_volume

    region_01 = ['上海']
    region_02 = ['江苏', '浙江']
    region_03 = ['北京', '天津', '河北', '河南', '安徽', '陕西', '湖南', '湖北', '江西', '福建', '广东', '山西']
    region_04 = ['吉林', '甘肃', '四川', '内蒙', '重庆', '青海', '广西', '云南', '海南', '黑龙', '贵州', '辽宁']
    region_05 = ['新疆', '西藏']
#计算函数
    def work2(self):
        global fee
        try :
            self.weight=float(self.entry01.get())
        except ValueError or AttributeError:
            return messagebox.showinfo('错误','请输入数字')

        self.region = self.entry02.get()[0:2]
        weight = math.ceil(self.weight)
        if self.region in self.region_01:
            if weight <= 1:
                self.fee = 10
            else:
                weight = weight - 1
                self.fee = 10 + weight * 3
                messagebox.showinfo('费用', self.fee)
        elif self.region in self.region_02:
            if self.weight <= 1:
                self.fee = 10
            else:
                weight = weight - 1
                self.fee = 10 + weight * 4
                messagebox.showinfo('费用', self.fee)
        elif self.region in self.region_03:
            if self.weight <= 1:
                self.fee = 15
            else:
                weight = weight - 1
                self.fee = 15 + weight * 5
                messagebox.showinfo('费用', self.fee)
        elif self.region in self.region_04:
            if self.weight <= 1:
                self.fee = 15
            else:
                weight = weight - 1
                self.fee = 15 + weight * 6.5
                messagebox.showinfo('费用', self.fee)
        elif self.region in self.region_05:
            if self.weight <= 1:
                self.fee = 15
            else:
                weight = weight - 1
                self.fee = 15 + weight * 10
            messagebox.showinfo('费用',self.fee)
        else:
            messagebox.showinfo('错误','请输入正确的地址')
#提示文字
    def on_entry_click_02(self,event):
        if self.entry02.get()=='xx省xx市xxx':
            self.entry02.delete(0,'end')
            self.entry02.config(fg='black')
    def on_entry_out_02(self,entry):
        if  self.entry02.get()=='':
            self.entry02.insert(0,'xx省xx市xxx')
            self.entry02.config(fg='grey')
    def on_entry_out_01(self,event):
        entry=event.widget
        if entry.get()=="":
            entry.insert(0,'单位：公斤(kg)')
            entry.config(fg='grey')
    def on_entry_click_01(self,event):
        entry=event.widget
        if entry.get()=="单位：公斤(kg)":
            entry.delete(0,'end')
            entry.config(fg="black")
#点击刷新界面
    def label_clear(self):
        for label in self.labels:
            label.destroy()
        self.labels.clear()
#计算后保存数据
    def bin01_command(self,event):
        self.work2()
        self.keep_history()
        self.entry01.delete(0,'end')
        self.entry01.insert(0, '单位：公斤(kg)')
        self.entry01.config(fg='grey')
        self.entry01.bind('<FocusOut>', self.on_entry_out_01)
        self.entry01.bind('<FocusIn>', self.on_entry_click_01)
        self.entry02.delete(0,'end')
        self.entry02.insert(0,'xx省xx市xxx')
        self.entry02.config(fg='grey')
        self.entry02.bind('<FocusIn>',self.on_entry_click_02)
        self.entry02.bind('<FocusOut>',self.on_entry_out_02)

    def keep_history(self):
        try:
            t = localtime()
            self.weight = self.entry01.get()
            self.location = self.entry02.get()
            if self.weight == "" or self.location=="":
                messagebox.showinfo('出错','重量和地址不能为空')
            elif self.weight.isdigit()==False:
                pass
            else:
                with open('history.txt', 'a', encoding='utf8') as f:
                    f.write(f',{self.name},{t.tm_year}/{t.tm_mon}/{t.tm_mday} {t.tm_hour}:{t.tm_min},{self.weight},{self.fee}\n')
        except AttributeError:
            pass
#进入个人中心
    def into_personal_space(self):
        self.pack_forget()
        self.personal_space=Personal_space(self.master,self.name)
# #进入体积计算页面
    def into_page_volume(self):
        self.pack_forget()
        self.page_volume = Volume(self.master,self.name)
#个人中心第三界面
class Personal_space(Frame):
    def __init__(self,window,name):
        super().__init__(window)
        self.window=window
        self.name = name
        self.labels=[]
        self.window.title('个人中心')
        self.pack()
        self.personal_space()



#个人中心布局
    def personal_space(self):
        label = Label(self,text='查询历史记录',relief='solid',width=30,height=2)
        label.grid(row=0,column=0,columnspan=4)
        self.variable =StringVar()
        self.variable.set('今天')
        bin00=OptionMenu(self,self.variable,'今天','昨天')
        bin00.grid(row=1,column=0,columnspan=2)
        bin02= Button(self,text='确定',width=10,command=self.check_history)
        bin02.grid(row=1,column=3)
        bin01= Button(self,text = '查询全部个人历史记录',command=self.all_history)
        bin01.grid(row=2,column=0,columnspan=4)
        bin_quit = Button(self,text = '返回',width=18)
        bin_quit['command']=self.go_back_page2
        bin_quit.grid(row=3,column=0,columnspan=4)
#返回至第二界面 计算主界面
    def go_back_page2(self):
        self.pack_forget()
        self.page2=Page2(self.master,self.name)
#点击后刷新界面
    def label_clear(self):
        for label in self.labels:
            label.destroy()
        self.labels.clear()

#查询个人历史记录函数
    def all_history(self):
        top = Toplevel(self)
        top.geometry('400x900+1000+50')
        label01 = Label(top,text = '用户名：\t 时间：\t 重量：\t 金额：\t')
        label01.pack()
        with open('history.txt', 'r', encoding='utf8') as  f:
            for line in f.readlines():
                if self.name in line:
                    new_line = line.replace(',','\t')
                    label_history = Label(top,text=new_line)
                    label_history.pack()
#根据所选查询今天或者昨天的历史记录
    def check_history(self):
        self.v=self.variable.get()
        if self.v=='今天' :
            t1 = localtime()
            print(f',{self.name},{t1.tm_year}/{t1.tm_mon}/{t1.tm_mday}')
            with open('history.txt', 'r', encoding='utf8') as f:
                if f',{self.name},{t1.tm_year}/{t1.tm_mon}/{t1.tm_mday}' not in f.read():
                    return messagebox.showinfo('提示','暂无记录')
                else:
                    f.seek(0)
                    top1 = Toplevel(self)
                    top1.geometry('400x900+1000+50')
                    label01 = Label(top1, text='用户名：\t 时间：\t 重量：\t 金额：\t')
                    label01.pack()
                    for line in f.readlines():
                        if f',{self.name},{t1.tm_year}/{t1.tm_mon}/{t1.tm_mday}' in line:
                            label = Label(top1,text=line.replace(",",'\t'))
                            label.pack()
        if self.v == '昨天':
            t2 = datetime.date.today()
            t2_past = str(t2 - datetime.timedelta(days=1)).replace('-','/')
            print(t2_past)
            with open('history.txt', 'r', encoding='utf8') as f :
                if f',{self.name},{t2_past}' not in f.read():
                    return messagebox.showinfo('提示','暂无记录')
                else :
                    f.seek(0)
                    top1 = Toplevel(self)
                    top1.geometry('400x900+1000+50')
                    label01 = Label(top1, text='用户名：\t 时间：\t 重量：\t 金额：\t')
                    label01.pack()
                    for line in f.readlines():
                        if f',{self.name},{t2_past}' in line:
                            label = Label(top1,text=line.replace(",",'\t'))
                            label.pack()

#管理员页面
class Mana_page(Frame):
    def __init__(self,window):
        super().__init__(window)
        self.window = window
        self.window.title("管理员")
        self.window.geometry('350x150+700+350')
        self.labels=[]
        self.mana_layout()
        self.pack()

#管理员页面布局
    def mana_layout(self):

        self.bin01 = Button(text='查看全部历史记录')
        self.bin01['command']=self.all_history
        self.bin01.pack(pady=5)

        self.entry=Entry(self,fg='grey',width=30)
        self.entry.insert(0,'请输入想查询记录的用户名')
        self.entry.bind('<FocusIn>',self.on_entry_click)
        self.entry.bind('<FocusOut>',self.on_entry_out)
        self.entry.pack(pady=5)

        self.bin_find = Button(text = '搜索',width=15)
        self.bin_find['command']=self.research
        self.bin_find.pack(pady=5)

    def on_entry_click(self,event):
        if self.entry.get() =='请输入想查询记录的用户名':
            self.entry.delete(0,'end')
            self.entry.config(fg='black')
    def on_entry_out(self,event):
        if self.entry.get()=='':
            self.entry.insert(0,'请输入想查询记录的用户名')
            self.entry.config(fg='grey')
    def label_clear(self):
        for label in self.labels:
            label.destroy()
        self.labels.clear()
    def all_history(self):
        top = Toplevel(self)
        top.title('记录')
        top.geometry('350x900+1300+50')
        self.label_clear()
        label01 = Label(top, text='用户名：\t 时间：\t 重量：\t 金额：\t')
        label01.pack()
        self.labels.append(label01)
        with open('history.txt', 'r', encoding='utf8') as f:
            for line in f.readlines():
                new_line = line.replace(',', '\t')
                label_history = Label(top, text=new_line)
                label_history.pack()
                self.labels.append(label_history)

    def research(self):
        self.label_clear()
        self.name_get = self.entry.get()
        with open('history.txt', 'r', encoding='utf8') as f :
            content = f.read()
            if self.name_get not in content :
                messagebox.showinfo('提示','查无记录或无此人')
            else:
                top = Toplevel(self)
                top.geometry('350x900+1300+50')
                top.title('记录')
                label01 = Label(top, text='用户名：\t 时间：\t 重量：\t 金额：\t')
                label01.pack()
                f.seek(0)
                for line in f.readlines():
                    if self.name_get in line :
                        new_line = line.replace(',', '\t')
                        label_history = Label(top, text=new_line)
                        label_history.pack()
                        self.labels.append(label_history)
                self.labels.append(label01)

#体积计算页面
class Volume(Frame):
    def __init__(self,window,name):
        super().__init__(window)
        self.window = window
        self.name = name
        self.labels=[]
        self.window.title('计算运费')
        self.window.geometry('300x250+750+350')
        self.pack()
        self.pack_widget()
    def pack_widget(self):

        label01 = Label(self, text='重量', relief='solid', width=10).grid(row=0, column=0, padx=5, pady=5)
        self.entry01 = Entry(self, fg='grey')
        self.entry01.insert(0, '单位：公斤(kg)')
        self.entry01.bind('<FocusOut>', self.on_entry_out_01)
        self.entry01.bind('<FocusIn>', self.on_entry_click_01)
        self.entry01.grid(row=0, column=1, padx=5, pady=5)

        # 获得地址
        label02 = Label(self, text='收货地址', relief="solid", width=10).grid(row=1, column=0, padx=5, pady=5)
        self.entry02 = Entry(self,fg='grey')
        self.entry02.insert(0,'xx省xx市xxx')
        self.entry02.bind('<FocusIn>',self.on_entry_click_02)
        self.entry02.bind('<FocusOut>',self.on_entry_out_02)
        self.entry02.grid(row=1,column=1,padx=5,pady=5)
  #获得长宽高

        label03=Label(self,text='长度',relief='solid',width=10).grid(row=2,column=0,padx=5,pady=5)
        self.entry03 = Entry(self, fg='grey')
        self.entry03.insert(0, '单位：cm')
        self.entry03.bind('<FocusOut>', self.on_entry_out)
        self.entry03.bind('<FocusIn>', self.on_entry_click)
        self.entry03.grid(row=2,column=1,padx=5,pady=5)


        label04 = Label(self, text='宽度', relief='solid',width=10).grid(row=3, column=0,padx=5,pady=5)
        self.entry04 = Entry(self,fg='grey')
        self.entry04.insert(0,'单位：cm')
        self.entry04.bind('<FocusOut>',self.on_entry_out)
        self.entry04.bind('<FocusIn>',self.on_entry_click)
        self.entry04.grid(row=3, column=1,padx=5,pady=5)

        label05=Label(self,text='高度',relief='solid',width=10).grid(row=4,column=0,padx=5,pady=5)
        self.entry05 = Entry(self,fg='grey')
        self.entry05.insert(0,'单位：cm')
        self.entry05.bind('<FocusIn>',self.on_entry_click)
        self.entry05.bind('<FocusOut>',self.on_entry_out)
        self.entry05.grid(row=4,column=1,padx=5,pady=5)

        # 确定按钮
        bin01 = Button(self, text='确定', width=10)
        bin01.bind('<Button-1>', self.bin01_command)
        bin01.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        bin02 = Button(self, text='返回', width=10)
        bin02['command']=self.go_back_page2
        bin02.grid(row=6,column=0, columnspan=2,padx=5,pady=5)


    def go_back_page2(self):
        self.pack_forget()
        self.page2=Page2(self.master,self.name)

    def bin01_command(self,event):
        self.work2()
        self.keep_history()
        self.entry01.delete(0,'end')
        self.entry01.insert(0, '单位：公斤(kg)')
        self.entry01.config(fg='grey')
        self.entry01.bind('<FocusOut>', self.on_entry_out_01)
        self.entry01.bind('<FocusIn>', self.on_entry_click_01)
        self.entry02.delete(0,'end')
        self.entry02.insert(0,'xx省xx市xxx')
        self.entry02.config(fg='grey')
        self.entry02.bind('<FocusIn>',self.on_entry_click_02)
        self.entry02.bind('<FocusOut>',self.on_entry_out_02)
        self.entry03.delete(0,'end')
        self.entry03.insert(0,'单位：cm')
        self.entry03.config(fg='grey')
        self.entry03.bind('<FocusOut>',self.on_entry_out)
        self.entry03.bind('<FocusIn>',self.on_entry_click)
        self.entry04.delete(0,'end')
        self.entry04.insert(0,'单位：cm')
        self.entry04.config(fg='grey')
        self.entry04.bind('<FocusOut>',self.on_entry_out)
        self.entry04.bind('<FocusIn>',self.on_entry_click)
        self.entry05.delete(0,'end')
        self.entry05.insert(0,'单位：cm')
        self.entry05.config(fg='grey')
        self.entry05.bind('<FocusOut>',self.on_entry_out)
        self.entry05.bind('<FocusIn>',self.on_entry_click)

    region_01 = ['上海']
    region_02 = ['江苏', '浙江']
    region_03 = ['北京', '天津', '河北', '河南', '安徽', '陕西', '湖南', '湖北', '江西', '福建', '广东', '山西']
    region_04 = ['吉林', '甘肃', '四川', '内蒙', '重庆', '青海', '广西', '云南', '海南', '黑龙', '贵州', '辽宁']
    region_05 = ['新疆', '西藏']

    def work2(self):
        global fee
    #防止重量输入格式不正确
        try:
            weight = float(self.entry01.get())
        except ValueError:
            messagebox.showinfo('错误', '请输入数字')

    #防止不输入长宽高
        try:
            self.region = self.entry02.get()[0:2]
            self.weight = float(self.entry01.get())
            self.width = float(self.entry04.get())
            self.height = float(self.entry05.get())
            self.length = float(self.entry03.get())
            volume_ = self.width * self.height * self.length / 8000
            if volume_ > self.weight :
                weight = volume_
            else:
                weight = self.weight
            weight = math.ceil(weight)
            print(weight)
            if self.region in self.region_01:
                if weight <= 1:
                    self.fee = 10
                else:
                    weight = weight - 1
                    self.fee = 10 + weight * 3
                    messagebox.showinfo('费用', self.fee)
            elif self.region in self.region_02:
                if weight <= 1:
                    self.fee = 10
                else:
                    weight = weight - 1
                    self.fee = 10 + weight * 4
                    messagebox.showinfo('费用', self.fee)
            elif self.region in self.region_03:
                if weight <= 1:
                    self.fee = 15
                else:
                    weight = weight - 1
                    self.fee = 15 + weight * 5
                    messagebox.showinfo('费用', self.fee)
            elif self.region in self.region_04:
                if weight <= 1:
                    self.fee = 15
                else:
                    weight = weight - 1
                    self.fee = 15 + weight * 6.5
                    messagebox.showinfo('费用', self.fee)
            elif self.region in self.region_05:
                if weight <= 1:
                    self.fee = 15
                else:
                    weight = weight - 1
                    self.fee = 15 + weight * 10
                messagebox.showinfo('费用', self.fee)
            else:
                messagebox.showinfo('错误','请输入正确地址')
        except ValueError or UnboundLocalError:
            messagebox.showinfo('错误','请输入有效值')
    def keep_history(self):
        try:
            t = localtime()
            self.weight = self.entry01.get()
            self.location = self.entry02.get()
            if self.weight == "" or self.location=="":
                messagebox.showinfo('出错','重量和地址不能为空')
            else:
                with open('history.txt', 'a', encoding='utf8') as f:
                    f.write(f',{self.name},{t.tm_year}/{t.tm_mon}/{t.tm_mday} {t.tm_hour}:{t.tm_min},{self.weight},{self.fee}\n')
        except AttributeError:
            pass
    def on_entry_out(self,event):
        entry=event.widget
        if entry.get()=="":
            entry.insert(0,'单位：cm')
            entry.config(fg='grey')
    def on_entry_click(self,event):
        entry = event.widget
        if entry.get()=="单位：cm":
            entry.delete(0,'end')
            entry.config(fg='black')
    def on_entry_out_01(self,event):
        entry=event.widget
        if entry.get()=="":
            entry.insert(0,'单位：公斤(kg)')
            entry.config(fg='grey')
    def on_entry_click_01(self,event):
        entry=event.widget
        if entry.get()=="单位：公斤(kg)":
            entry.delete(0,'end')
            entry.config(fg="black")
    def on_entry_click_02(self,event):
        if self.entry02.get()=='xx省xx市xxx':
            self.entry02.delete(0,'end')
            self.entry02.config(fg='black')
    def on_entry_out_02(self,entry):
        if  self.entry02.get()=='':
            self.entry02.insert(0,'xx省xx市xxx')
            self.entry02.config(fg='grey')

if __name__ == '__main__':
    app = Tk()
    app.geometry('300x150+700+350')
    app.title('登录')
    page1 = Page1(master=app)
    app.mainloop()





