
from http.client import PRECONDITION_FAILED
import tkinter as tk
import tkinter.font as tf
import math
from tkinter import filedialog, dialog
import os
import tkinter.messagebox
def ys_DHB(t):
        D1=-37.916+(16.467*math.log(t,math.e))
        return D1
def ys_H(t):
        H1=2.511*pow(t,0.422)
        return H1
def ys_G(H1):
        G1=45.144/(1+3.967*math.exp(-0.185*H1))
        return G1
def ys_V(H1,G1):
        V1=(H1+3)*G1*0.42
        return V1
def ys_N(G1,D1):
        N1=40000*(G1/(3.14*pow(D1,2)))
        return N1
def hs_DHB(t):
        D2=1.138*pow(t,0.777)
        return D2
def hs_H(t):
        H2=-6.148+(4.891*math.log(t,math.e))
        return H2
def hs_G(H2):
        G2=45.144/(1+3.967*math.exp(-0.185*H2))
        return G2
def hs_V(H2,G2):
        V2=(H2+3)*G2*0.43
        return V2
def hs_N(G2,D2):
        N2=40000*(G2/(3.14*pow(D2,2)))
        return N2   
def ly_DHB(t):
        D3=30.386*math.exp(-17.691/t)
        return D3
def ly_H(t):
        H3=34.309*math.exp(-25.282/t)
        return H3
def ly_G(H3):
        G3=60.598/(1+7.76*math.exp(-0.216*H3))
        return G3
def ly_V(H3,G3):
        V3=(H3+3)*G3* 0.41
        return V3
def ly_N(G3,D3):
        N3=40000*(G3/(3.14*pow(D3,2)))
        return N3   
def rc_DHB(t):
        D4=0.56*pow(t,0.952)
        return D4
def rc_H(t):
        H4=2.711*pow(t,0.379)
        return H4
def rc_G(H4):
        G4=38.203/(1+3.674*math.exp(-0.197*H4))
        return G4
def rc_V(H4,G4):
        V4=(H4+3)*G4*0.4
        return V4
def rc_N(G4,D4):
        N4=40000*(G4/(3.14*pow(D4,2)))
        return N4   
def ys_gan(D,H):
    gan=math.exp(1.041*math.log(H*D**2)-4.631)
    return gan
def ys_pi(D,H):
    pi=math.exp(0.774*math.log(H*D**2)-4.693)
    return pi
def ys_zhi(D):
    zhi=math.exp(2.577*math.log(D)-4.080)
    return zhi
def ys_ye(D):
    ye=math.exp(2.575*math.log(D)-5.117)
    return ye
def ys_gen(D):
    gen=math.exp(2.287*math.log(D)-4.142)
    return gen
def hs_gan(D,H):
    gan=math.exp(1.024*math.log(H*D**2)-4.499)
    return gan
def hs_pi(D,H):
    pi=math.exp(0.884*math.log(H*D**2)-5.385)
    return pi
def hs_zhi(D):
    zhi=math.exp(2.576*math.log(D)-4.085)
    return zhi
def hs_ye(D):
    ye=math.exp(2.757*math.log(D)-5.759)
    return ye
def hs_gen(D,H):
    gen=math.exp(0.971*math.log(H*D**2)-5.263)
    return gen
def ly_gan(D,H):
    gan=math.exp(0.998*math.log(H*D**2)-4.293)
    return gan
def ly_pi(D,H):
    pi=math.exp(0.804*math.log(H*D**2)-4.535)
    return pi
def ly_zhi(D):
    zhi=math.exp(2.046*math.log(D)-2.551)
    return zhi
def ly_ye(D):
    ye=math.exp(1.905*math.log(D)-3.447)
    return ye
def ly_gen(D):
    gen=math.exp(2.186*math.log(D)-3.462)
    return gen
def rc_gan(D,H):
    gan=math.exp(0.993*math.log(H*D**2)-3.788)
    return gan
def rc_pi(D,H):
    pi=math.exp(0.756*math.log(H*D**2)-3.924)
    return pi
def rc_zhi(D):
    zhi=math.exp(3.499*math.log(D)-6.507)
    return zhi
def rc_ye(D):
    ye=math.exp(2.293*math.log(D)-4.886)
    return ye
def rc_gen(D):
    gen=math.exp(2.764*math.log(D)-4.208)
    return gen
def ii(GD,G,d,h30):
    i=math.exp(-1.3257+(-0.0905)*GD+(-0.2751)*math.log(G)+0.7822*math.sqrt(d)+(-0.0030)*d**2+0.1360*h30)
    return i
def Hh(h30,d):
    h=(48.3936+2.864*h30)/(1+(80.9377/d)+(159.811/d**2))
    return h
def pp(d,GD):
    p=1/(1+math.exp(-(-4.6433+2.0424*math.sqrt(d)+(-0.0333)*GD)))
    return p
def si(N,D):
    SDI=N*((D/20)**1.662)
    return SDI
def ts_DHB(t):
    D5=110.656*math.exp(-116.3/(t+10.609))
    return D5
def ts_H(t):
    H5=10843.793*(1-math.exp(-((t-0.017)/82540.738)**0.952))
    return H5
def ts_V(t):
    v5=3.805/(1+math.exp(5.518-0.045*t))
    return v5
def ts_N(G5,D5):
        N5=40000*(G5/(3.14*pow(D5,2)))
        return N5 
def ts_G(D5):
    G5=3.14*((D5/2)**2)
    return G5
root_lan=tk.Tk()
root_lan.title("QUASSI")
root_lan.geometry("300x250+200+200")
button_list = []
def language_selection1():
    root=tk.Tk()
    root.title("林分模拟器")
    root.geometry("1200x500+200+200")
    text=tk.Text(root,height=800,width=300,state="normal")
    text.pack()
    ft=tf.Font(family="微软雅黑",size=10)
    text.tag_add("tag",tk.END)
    text.tag_config("tag",font=ft)
    menubar=tk.Menu(root)
    def open_file():
        global file_path
        global file_text
        file_path = filedialog.askopenfilename(title='选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path is not None:
            with open(file=file_path, mode='r+', encoding='utf-8') as file:
                file_text = file.read()
            text.insert('insert', file_text)
    def save_file():
        global file_path
        global file_text
        file_path = filedialog.asksaveasfilename(title='保存文件',initialfile='tree.text')
        file_text = text.get('1.0', tk.END)
        if file_path is not None:
            with open(file=file_path, mode='a+', encoding='utf-8') as file:
                file.write(file_text)
            text.delete('1.0', tk.END)
            dialog.Dialog(None, {'title': 'File Modified', 'text': '保存完成', 'bitmap': 'warning', 'default': 0,
                                'strings': ('OK', 'Cancle')})
            print('保存完成')
    def exit_file():
        root.destroy()
    menubar1=tk.Menu(menubar,tearoff=False)
    menubar1.add_command(label="保存",command=save_file)
    menubar1.add_command(label="打开",command=open_file)
    menubar1.add_command(label="退出",command=exit_file)
    menubar.add_cascade(label="文件",menu=menubar1)
    menubar2=tk.Menu(menubar,tearoff=False)
    def ts_command():
        root2=tk.Tk()
        root2.title("树种")
        root2.geometry("300x300+500+200")
        var = tk.StringVar()
        selecttree_label=tk.Label(root2,textvar=var,width=30,height=1,text="你必须挑选一个树种")
        selecttree_label.place(x=0,y=180)
        def print_selection1():
            global tree
            tree=1
        def print_selection2():
            global tree
            tree=2
        def print_selection4():
            global tree
            tree=4
        def print_selection5():
            global tree
            tree=5
        treespeices1=tk.Radiobutton(root2,text="油松",var=var,value="油松",command=print_selection1,indicatoron=False)
        treespeices1.place(x=40,y=20)
        treespeices2=tk.Radiobutton(root2,text="华山松",var=var,value="华山松",command=print_selection2,indicatoron=False)
        treespeices2.place(x=40,y=65)
        treespeices4=tk.Radiobutton(root2,text="锐齿栎",var=var,value="锐翅栎",command=print_selection4,indicatoron=False)
        treespeices4.place(x=40,y=110)
        treespeices5=tk.Radiobutton(root2,text="铁杉",var=var,value="铁杉",command=print_selection5,indicatoron=False)
        treespeices5.place(x=40,y=155)
        def ok_command():
            root2.destroy()
        def Cancel_command():
            var.set(0)
            root2.destroy()
        ok=tk.Button(root2,text="OK",height=2,width=10,command=ok_command)
        ok.place(x=40,y=200)
        concel=tk.Button(root2,text="取消",height=2,width=10,command=Cancel_command)
        concel.place(x=150,y=200)
    menubar2.add_command(label="树种",command=ts_command)
    def stand_condition():
        stand=tk.Tk()
        stand.title("立地条件")
        stand.geometry("450x300+500+200")
        l1=tk.Label(stand,text="林班")
        l1.place(x=50,y=20)
        l2=tk.Label(stand,text="林分年龄")
        l2.place(x=50,y=50)
        l3=tk.Label(stand,text="平均胸径")
        l3.place(x=50,y=80)
        l4=tk.Label(stand,text="平均高度")
        l4.place(x=50,y=110)
        l5=tk.Label(stand,text="林分密度")
        l5.place(x=50,y=140)
        l6=tk.Label(stand,text="林分蓄积量")
        l6.place(x=50,y=170)
        l7=tk.Label(stand,text="模拟年龄")
        l7.place(x=50,y=200)
        entry1=tk.Entry(stand)
        entry1.insert(0, '1')
        entry1.place(x=160,y=20)
        entry2=tk.Entry(stand)
        entry2.insert(0, '20')
        entry2.place(x=160,y=50)
        entry3=tk.Entry(stand)
        entry3.insert(0, '12')
        entry3.place(x=160,y=80)
        entry4=tk.Entry(stand)
        entry4.insert(0, '12')
        entry4.place(x=160,y=110)
        entry5=tk.Entry(stand)
        entry5.insert(0, '2000')
        entry5.place(x=160,y=140)
        entry6=tk.Entry(stand)
        entry6.insert(0, '150')
        entry6.place(x=160,y=170)
        entry7=tk.Entry(stand)
        entry7.insert(0, '50')
        entry7.place(x=160,y=200)
        def ok2_command():
            global t_xs
            global d_xs
            global h_xs
            global n_xs
            global v_xs
            global t_gjxs
            global k3
            global k4
            global k5
            global k6
            t_xs=int(entry2.get())
            d_xs=float(entry3.get())
            h_xs=float(entry4.get())
            n_xs=float(entry5.get())
            v_xs=float(entry6.get())
            t_gjxs=int(entry7.get())
            if tree==1:
                d_lx=ys_DHB(t_xs)
                h_lx=ys_H(t_xs)
                g_lx=ys_G(h_lx)
                n_lx=ys_N(g_lx,d_lx)
                v_lx=ys_V(h_lx,g_lx)
                k3=d_xs/d_lx
                k4=h_xs/h_lx
                k5=n_xs/n_lx
                k6=v_xs/v_lx
            if tree==2:
                d_lx=hs_DHB(t_xs)
                h_lx=hs_H(t_xs)
                g_lx=hs_G(t_xs)
                n_lx=hs_N(g_lx,d_lx)
                v_lx=hs_V(h_lx,g_lx)
                k3=d_xs/d_lx
                k4=h_xs/h_lx
                k5=n_xs/n_lx
                k6=v_xs/v_lx           
            if tree==4:
                d_lx=rc_DHB(t_xs)
                h_lx=rc_H(t_xs)
                g_lx=rc_G(t_xs)
                n_lx=rc_N(g_lx,d_lx)
                v_lx=rc_V(h_lx,g_lx)
                k3=d_xs/d_lx
                k4=h_xs/h_lx
                k5=n_xs/n_lx
                k6=v_xs/v_lx    
            if tree==5:
                d_lx=ts_DHB(t_xs)
                h_lx=ts_H(t_xs)
                g_lx=ts_G(d_lx)
                n_lx=ts_N(g_lx,d_lx)
                v_lx=ts_V(h_lx,g_lx)
                k3=d_xs/d_lx
                k4=h_xs/h_lx
                k5=n_xs/n_lx
                k6=v_xs/v_lx                      
            stand.destroy()
            
        def concel2_command():
            stand.destroy()
        ok2=tk.Button(stand,text="确定",height=2,width=10,command=ok2_command)
        ok2.place(x=50,y=220)
        concel2=tk.Button(stand,text="取消",height=2,width=10,command=concel2_command)
        concel2.place(x=200,y=220)
    menubar2.add_command(label="立地条件",command=stand_condition)
    def jingjie_condition():
        jingjie=tk.Tk()
        jingjie.title("径阶设置")
        jingjie.geometry("450x300+500+200")
        jj1=tk.Label(jingjie,text="胸径范围10-19.9（cm）")
        jj1.place(x=50,y=20)
        jj2=tk.Label(jingjie,text="胸径范围20-34.9（cm）")
        jj2.place(x=50,y=50)
        jj3=tk.Label(jingjie,text="胸径范围35+（cm）")
        jj3.place(x=50,y=80)
        entry11=tk.Entry(jingjie)
        entry11.insert(0, '840')
        entry11.place(x=300,y=20)
        entry22=tk.Entry(jingjie)
        entry22.insert(0, '234')
        entry22.place(x=300,y=50)
        entry33=tk.Entry(jingjie)
        entry33.insert(0, '14')
        entry33.place(x=300,y=80)
        jf1=tk.Label(jingjie,text="抚育方法(上层伐=1，中层伐=2，下层伐=3)")
        jf1.place(x=50,y=110)
        jj2=tk.Label(jingjie,text="间伐强度(%)")
        jj2.place(x=50,y=140)
        jj3=tk.Label(jingjie,text="间伐时间(年)")
        jj3.place(x=50,y=170)
        jf11=tk.Entry(jingjie)
        jf11.insert(0, '0')
        jf11.place(x=300,y=110)
        jf22=tk.Entry(jingjie)
        jf22.insert(0, '0')
        jf22.place(x=300,y=140)
        jf33=tk.Entry(jingjie)
        jf33.insert(0, '0')
        jf33.place(x=300,y=170)
        def ok3_command():
            global t_xs
            global d_xs
            global h_xs
            global n_xs
            global v_xs
            global t_gjxs
            global k3
            global k4
            global k5
            global k6
            t=0
            y01=int(entry11.get())
            y02=int(entry22.get())
            y03=int(entry33.get())
            ff=int(jf11.get())
            qd=int(jf22.get())
            qd=qd*0.01
            nf=int(jf33.get())
            yz=y01+y02+y03
            shannon=-((y01/yz)*math.log(y01/yz)+(y02/yz)*math.log(y02/yz)+(y03/yz)*math.log(y03/yz))
            E=shannon/3
            shannon=float("%.5f" % shannon )
            E=float("%.5f" % E)
            cj=y01*0.2+y02*0.5+y03*1
            jg=y01*3+y02*80+y03*200
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n         每公顷株数","tag")
            text.insert(tk.END,"\n       秦岭栎类油松混交林 ","tag") 
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n      间伐方法 {} (上层伐=1，中层伐=2，下层伐=3) ".format(ff),"tag") 
            text.insert(tk.END,"\n      间伐强度{}%  ".format(qd*100),"tag") 
            text.insert(tk.END,"\n      间伐年份{}年  ".format(nf),"tag")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n年 龄      第一径级          第二径级       第三径级               Shannon指数          Evenness均匀度          林分材积            木材价格")
            while t<85:
                if t/10 <1:
                    t=str(t)
                    t="0"+ t
                text.insert(tk.END,'\n'" {}       {}        {}         {}           {}         {}          {}         {}".format(t,y01,y02,y03,shannon,E,cj,jg),"tag")
                t=int(t)
                t=t+5 
                if ff==0:
                    y1=int(0.92*y01-0.29*y02-0.96*y03+109)
                    y2=int(0.04*y01+0.9*y02)
                    y3=int(0.02*y02+0.9*y03)
                    y01=y1
                    y02=y2
                    y03=y3
                    yz=y01+y02+y03
                    shannon=-((y01/yz)*math.log(y01/yz)+(y02/yz)*math.log(y02/yz)+(y03/yz)*math.log(y03/yz))
                    E=shannon/3
                    shannon=float("%.5f" % shannon )
                    E=float("%.5f" % E)
                    cj=y01*0.2+y02*0.5+y03*1
                    jg=y01*3+y02*80+y03*200
                    t=int(t)
                if ff==1:
                    y1=int(0.92*y01-0.29*y02-0.96*y03+109)
                    y2=int(0.04*y01+0.9*y02)
                    y3=int(0.02*y02+0.9*y03)
                    t=int(t)
                    if t % nf == 0:
                        y3=(1-qd)*y3
                    y01=int(y1)
                    y02=int(y2)
                    y03=int(y3)
                    shannon=-((y01/yz)*math.log(y01/yz)+(y02/yz)*math.log(y02/yz)+(y03/yz)*math.log(y03/yz))
                    E=shannon/3
                    shannon=float("%.5f" % shannon )
                    E=float("%.5f" % E)
                    cj=y01*0.2+y02*0.5+y03*1
                    jg=y01*3+y02*80+y03*200
                    t=int(t)
                if ff==2:
                    y1=int(0.92*y01-0.29*y02-0.96*y03+109)
                    y2=int(0.04*y01+0.9*y02)
                    y3=int(0.02*y02+0.9*y03)
                    t=int(t)
                    if t % nf == 0:
                        y2=(1-qd)*y2
                    y01=int(y1)
                    y02=int(y2)
                    y03=int(y3)
                    shannon=-((y01/yz)*math.log(y01/yz)+(y02/yz)*math.log(y02/yz)+(y03/yz)*math.log(y03/yz))
                    E=shannon/3
                    shannon=float("%.5f" % shannon )
                    E=float("%.5f" % E)    
                    cj=y01*0.2+y02*0.5+y03*1
                    jg=y01*3+y02*80+y03*200
                    t=int(t)     
                if ff==3:
                    y1=int(0.92*y01-0.29*y02-0.96*y03+109)
                    y2=int(0.04*y01+0.9*y02)
                    y3=int(0.02*y02+0.9*y03)
                    t=int(t)
                    if t % nf == 0:
                        y1=(1-qd)*y1
                    y01=int(y1)
                    y02=int(y2)
                    y03=int(y3)
                    shannon=-((y01/yz)*math.log(y01/yz)+(y02/yz)*math.log(y02/yz)+(y03/yz)*math.log(y03/yz))
                    E=shannon/3
                    shannon=float("%.5f" % shannon )
                    E=float("%.5f" % E)
                    cj=y01*0.2+y02*0.5+y03*1
                    jg=y01*3+y02*80+y03*200
                    t=int(t)                          
            jingjie.destroy()
        def concel3_command():
            jingjie.destroy()
        ok3=tk.Button(jingjie,text="确定",height=2,width=10,command=ok3_command)
        ok3.place(x=50,y=220)
        concel3=tk.Button(jingjie,text="取消",height=2,width=10,command=concel3_command)
        concel3.place(x=200,y=220)
    menubar2.add_command(label="径阶设置",command=jingjie_condition)
    menubar.add_cascade(label="设置",menu=menubar2)
    menubar3=tk.Menu(menubar,tearoff=False)
    def nomal_table():
        t=20
        if tree==1:
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                标准林分收获表")
            text.insert(tk.END,"\n                                      油松 ")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\n年 龄    胸 径     树 高    断面积    密 度    蓄 积    平均单株材积    连年生长量    平均生长量")
            while t<85:
                D=ys_DHB(t)
                d1=float("%.1f" % D)
                H=ys_H(t)
                h1=float("%.1f" % H)
                G=ys_G(H)
                g1="%.2f" % G
                V=ys_V(H,G)
                v1=float("%.1f" % V)
                N=ys_N(G,D)
                n1=int(N)
                yH=ys_H(t-1)
                yG=ys_G(yH)
                A1=ys_V(H,G)-ys_V(yH,yG)
                a1=float("%.1f" % A1)
                Av1=V/t
                av1=float("%.1f" % Av1)
                Avo=V/N
                avo1=float("%.4f" % Avo )
                if h1/10 <1:
                    h1=str(h1)
                    h1="0"+ h1
                if d1/10 <1:
                    d1=str(d1)
                    d1="0"+ d1
                if n1/1000 <1:
                    n1=str(n1)
                    n1="0"+ n1
                text.insert(tk.END,'\n'" {}   {}   {}   {}  {}  {}   {}    {}       {}".format(t,d1,h1,g1,n1,v1,avo1,a1,av1),"tag")
                t=t+5 
        if tree==2:
            text.insert(tk.END,"\n--------------------------------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                标准林分收获表")
            text.insert(tk.END,"\n                                      华山松 ")   
            text.insert(tk.END,"\n-------------------------------------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\n年 龄        胸 径      树 高       断面积       密 度       蓄 积       平均单株材积        连年生长量        平均生长量     林分密度指数")
            while t<85:
                D=hs_DHB(t)
                d2=float("%.1f" % D)
                H=hs_H(t)
                h2=float("%.1f" % H)
                G=hs_G(H)
                g2="%.2f" % G
                V=hs_V(H,G)
                v2="%.1f" % V
                N=hs_N(G,D)
                n2=int(N)
                yH=hs_H(t-1)
                yG=hs_G(yH)
                A2=hs_V(H,G)-hs_V(yH,yG)
                a2=float("%.1f" % A2)
                Av2=V/t
                av2=float("%.1f" % Av2)
                Avo=V/N
                avo2=float("%.4f" % Avo )
                avo2=format(avo2, '.4f')
                sdi=si(n2,d2)
                sdi=float("%.1f" % sdi)
                if h2/10 <1:
                    h2=str(h2)
                    h2="0"+ h2
                if d2/10 <1:
                    d2=str(d2)
                    d2="0"+ d2
                if n2/1000 <1:
                    n2=str(n2)
                    n2="0"+ n2
                if a2/10 <1:
                    a2=str(a2)
                    a2="0"+ a2
                if av2/10 <1:
                    av2=str(av2)
                    av2="0"+ av2
                text.insert(tk.END,'\n'" {}      {}    {}    {}    {}    {}     {}         {}        {}      {}".format(t,d2,h2,g2,n2,v2,avo2,a2,av2,sdi),"tag")
                t=t+5  
        if tree==4:
            text.insert(tk.END,"\n----------------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                标准林分收获表")
            text.insert(tk.END,"\n                                      锐齿栎 ")   
            text.insert(tk.END,"\n----------------------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\n年 龄        胸 径       树 高       断面积      密 度       蓄 积       平均单株材积       连年生长量       平均生长量")
            while t<85:
                D=rc_DHB(t)
                d4=float("%.1f" % D)
                H=rc_H(t)
                h4=float("%.1f" % H)
                G=rc_G(H)
                g4="%.2f" % G
                V=rc_V(H,G)
                v4=float("%.1f" % V)
                N=rc_N(G,D)
                n4=int(N)
                yH=rc_H(t-1)
                yG=rc_G(yH)
                A4=rc_V(H,G)-rc_V(yH,yG)
                a4=float("%.1f" % A4)
                Av4=v4/t
                av4=float("%.1f" % Av4)
                Avo=v4/N
                avo4=float("%.4f" % Avo)
                avo4=format(avo4, '.4f')
                if h4/10 <1:
                    h4=str(h4)
                    h4="0"+ h4
                if d4/10 <1:
                    d4=str(d4)
                    d4="0"+ d4
                if n4/1000 <1:
                    n4=str(n4)
                    n4="0"+ n4
                text.insert(tk.END,'\n'" {}      {}    {}    {}    {}    {}     {}         {}        {}".format(t,d4,h4,g4,n4,v4,avo4,a4,av4),"tag")
                t=t+5 
        if tree==5:
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                标准林分收获表")
            text.insert(tk.END,"\n                                      铁杉 ")   
            text.insert(tk.END,"\n----------------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\n年 龄          胸 径              树 高            单株材积   ")
            while t<85:
                D=ts_DHB(t)
                d5=float("%.1f" % D)
                H=ts_H(t)
                h5=float("%.1f" % H)
                V=ts_V(t)
                v5=float("%.5f" % V)
                if h5/10 <1:
                    h5=str(h5)
                    h5="0"+ h5
                if d5/10 <1:
                    d5=str(d5)
                    d5="0"+ d5
                text.insert(tk.END,'\n'" {}        {}         {}        {}   ".format(t,d5,h5,v5),"tag")
                t=t+5 
    menubar3.add_command(label="标准林分生长过程表",command=nomal_table)
    def index_table():
        def ys_index(H_dom,t0,t):
            s1=float(H_dom*((1-math.exp(-(t0/25.679)**1.465))/(1-math.exp(-(t/25.679)**1.465))))
            return s1
        def hs_index(H_dom,t0,t):
            s2=float(H_dom*((1+math.pow(t0/157.453,-0.789))/(1+math.pow(t/157.453,-0.789))))
            return s2
        def ly_index(H_dom,t0,t):
            s3=float(H_dom*math.exp(math.exp((16.821-t)/12.496)-math.exp((16.821-t0)/12.496)))
            return s3
        def rc_index(H_dom,t0,t):
            s4=float(H_dom*math.exp(15.4*(1/(t+2.95)-1/(t0+2.95))))
            return s4
        if tree==1:
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                立地指数表")
            text.insert(tk.END,"\n                                 油松    ")   
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n  年龄    8       9       10      11      12      13      14      15")
            text.insert(tk.END,"\n")
            s1=0
            t=20
            H_dom=8
            while t<60:
                text.insert(tk.END,"  {}".format(t))
                H_dom=8
                while H_dom<16:
                    s1=ys_index(H_dom,30,t)
                    s1=float("%.1f" % s1)
                    if s1/10 <1:
                        s1=str(s1)
                        s1="0"+ s1
                    text.insert(tk.END,"    {}".format(s1))
                    H_dom=H_dom+1
                text.insert(tk.END,"\n")
                t=t+2
            text.insert(tk.END,"                                                                基准年龄：30年")
        if tree==2:
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                立地指数表")
            text.insert(tk.END,"\n                                 华山松    ")   
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n  年龄    8       9       10      11      12      13      14      15")
            text.insert(tk.END,"\n")
            s2=0
            t=20
            H_dom=8
            while t<60:
                text.insert(tk.END,"  {}".format(t))
                H_dom=8
                while H_dom<16:
                    s2=hs_index(H_dom,30,t)
                    s2=float("%.1f" % s2)
                    if s2/10 <1:
                        s2=str(s2)
                        s2="0"+ s2
                    text.insert(tk.END,"    {}".format(s2))
                    H_dom=H_dom+1
                text.insert(tk.END,"\n")
                t=t+2
            text.insert(tk.END,"                                                                基准年龄：30年")

        if tree==4:
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                立地指数表")
            text.insert(tk.END,"\n                                  锐齿栎    ")   
            text.insert(tk.END,"\n--------------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n  年龄    8       9       10      11      12      13      14      15")
            text.insert(tk.END,"\n")
            s4=0
            t=20
            H_dom=8
            while t<60:
                text.insert(tk.END,"  {}".format(t))
                H_dom=8
                while H_dom<16:
                    s4=rc_index(H_dom,15,t)
                    s4=float("%.1f" % s4)
                    if s4/10 <1:
                        s4=str(s4)
                        s4="0"+ s4
                    text.insert(tk.END,"    {}".format(s4))
                    H_dom=H_dom+1
                text.insert(tk.END,"\n")
                t=t+2
            text.insert(tk.END,"                                                                基准年龄：15年")
    menubar3.add_command(label="立地指数表",command=index_table)
    def volumn_table():
        def ys_volume(D,H):
            v1=(0.719*3.14*D**(2-0.092)*H**(1-0.031))/40000
            return v1
        def hs_volume(D,H):
            v2=(0.686*3.14*D**(2-0.186)*H**1.105)/40000
            return v2
        def ly_volume(D,H):
            v3=0.001*D**1.719*H**1.204
            return v3
        def rc_volume(D,H):
            v4=(0.728*3.14*D**(2-0.166)*H**1.015)/40000
            return v4
        if tree==1:
            text.insert(tk.END,"\n     树高   6.0          8.0          10.0        12.0         14.0         16.0         18.0          20.0 ")
            text.insert(tk.END,"\n胸径 ----------------------------------------------------------------------------------------------------")
            D=6
            while D<30:
                if D/10<1:
                    D=str(D)
                    D="0"+ D
                text.insert(tk.END,"\n  {}".format(D))
                D=int(D)
                H=6
                while H<21:
                    v1=ys_volume(D,H)
                    v1="%.4f" % v1
                    text.insert(tk.END,"       {}".format(v1))
                    H=H+2
                text.insert(tk.END,"\n")
                D=D+2
        if tree==2:
            text.insert(tk.END,"\n     树高  6.0          8.0          10.0        12.0         14.0         16.0         18.0          20.0 ")
            text.insert(tk.END,"\n胸径 --------------------------------------------------------------------------------------------------")
            D=6
            while D<30:
                if D/10<1:
                    D=str(D)
                    D="0"+ D
                text.insert(tk.END,"\n  {}".format(D))
                D=int(D)
                H=6
                while H<21:
                    v2=hs_volume(D,H)
                    v2="%.4f" % v2
                    text.insert(tk.END,"       {}".format(v2))
                    H=H+2
                text.insert(tk.END,"\n")
                D=D+2

        if tree==4:
            text.insert(tk.END,"\n     树高  6.0          8.0          10.0        12.0         14.0         16.0         18.0          20.0 ")
            text.insert(tk.END,"\n胸径 --------------------------------------------------------------------------------------------------")
            D=6
            while D<30:
                if D/10<1:
                    D=str(D)
                    D="0"+ D
                text.insert(tk.END,"\n  {}".format(D))
                D=int(D)
                H=6
                while H<21:
                    v4=rc_volume(D,H)
                    v4="%.4f" % v4
                    text.insert(tk.END,"       {}".format(v4))
                    H=H+2
                text.insert(tk.END,"\n")
                D=D+2
    menubar3.add_command(label="二元材积表",command=volumn_table)
    def biomass_table():
        t=20
        if tree==1:
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                     生物量表")
            text.insert(tk.END,"\n                                      油松 ")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\n年 龄    胸 径     树 高       干       皮        枝         叶         根           总")
            while t<85:
                D=ys_DHB(t)
                d1=float("%.1f" % D)
                H=ys_H(t)
                h1=float("%.1f" % H)
                gan=ys_gan(D,H)
                gan1=float("%.1f" % gan)
                pi=ys_pi(D,H)
                pi1=float("%.1f" % pi)
                zhi=ys_zhi(D)
                zhi1=float("%.1f" % zhi)
                ye=ys_ye(D)
                ye1=float("%.1f" % ye)
                gen=ys_gen(D)
                gen1=float("%.1f" % gen)
                zong=gan1+pi1+zhi1+ye1+gen1
                zong1=float("%.1f" % zong)
                if h1/10 <1:
                    h1=str(h1)
                    h1="0"+ h1
                if d1/10 <1:
                    d1=str(d1)
                    d1="0"+ d1
                if gan1/100 <1:
                    gan1=str(gan1)
                    gan1="0"+ gan1
                if pi1/10<1:
                    pi1=str(pi1)
                    pi1="0"+ pi1
                if zhi1/10<1:
                    zhi1=str(zhi1)
                    zhi1="00"+ zhi1
                elif zhi1/100<1:
                    zhi1=str(zhi1)
                    zhi1="0"+zhi1   
                if ye1/10 <1:
                    ye1=str(ye1)
                    ye1="0"+ ye1 
                if gen1/10 <1:
                    gen1=str(gen1)
                    gen1="0"+ gen1
                if zong1/100<1:
                    zong1=str(zong1)
                    zong1="0"+zong1                                            
                text.insert(tk.END,'\n'" {}   {}   {}   {}  {}  {}   {}    {}    {}".format(t,d1,h1,gan1,pi1,zhi1,ye1,gen1,zong1),"tag")
                t=t+5 
        if tree==2:
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                     生物量表")
            text.insert(tk.END,"\n                                      华山松 ")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\n年 龄    胸 径     树 高       干       皮        枝         叶         根           总")
            while t<85:
                D=hs_DHB(t)
                d2=float("%.1f" % D)
                H=hs_H(t)
                h2=float("%.1f" % H)
                gan=hs_gan(D,H)
                gan2=float("%.1f" % gan)
                pi=hs_pi(D,H)
                pi2=float("%.1f" % pi)
                zhi=hs_zhi(D)
                zhi2=float("%.1f" % zhi)
                ye=hs_ye(D)
                ye2=float("%.1f" % ye)
                gen=hs_gen(D,H)
                gen2=float("%.1f" % gen)
                zong=gan2+pi2+zhi2+ye2+gen2
                zong2=float("%.1f" % zong)
                if h2/10 <1:
                    h2=str(h2)
                    h2="0"+ h2
                if d2/10 <1:
                    d2=str(d2)
                    d2="0"+ d2
                if gan2/100 <1:
                    gan2=str(gan2)
                    gan2="0"+ gan2
                if pi2/10<1:
                    pi2=str(pi2)
                    pi2="0"+ pi2
                if zhi2/10<1:
                    zhi2=str(zhi2)
                    zhi2="00"+ zhi2
                elif zhi2/100<1:
                    zhi2=str(zhi2)
                    zhi2="0"+zhi2   
                if ye2/10 <1:
                    ye2=str(ye2)
                    ye2="0"+ ye2 
                if gen2/10 <1:
                    gen2=str(gen2)
                    gen2="0"+ gen2
                if zong2/100<1:
                    zong2=str(zong2)
                    zong2="0"+zong2                                            
                text.insert(tk.END,'\n'" {}   {}   {}   {}  {}  {}   {}    {}    {}".format(t,d2,h2,gan2,pi2,zhi2,ye2,gen2,zong2),"tag")
                t=t+5 
  
        if tree==4:
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                    生物量表")
            text.insert(tk.END,"\n                                      锐齿栎 ")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\n年 龄    胸 径     树 高       干       皮        枝         叶         根           总")
            while t<85:
                D=rc_DHB(t)
                d3=float("%.1f" % D)
                H=rc_H(t)
                h3=float("%.1f" % H)
                gan=rc_gan(D,H)
                gan3=float("%.1f" % gan)
                pi=rc_pi(D,H)
                pi3=float("%.1f" % pi)
                zhi=rc_zhi(D)
                zhi3=float("%.1f" % zhi)
                ye=rc_ye(D)
                ye3=float("%.1f" % ye)
                gen=rc_gen(D)
                gen3=float("%.1f" % gen)
                zong=gan3+pi3+zhi3+ye3+gen3
                zong3=float("%.1f" % zong)
                if h3/10 <1:
                    h3=str(h3)
                    h3="0"+ h3
                if d3/10 <1:
                    d3=str(d3)
                    d3="0"+ d3
                if gan3/100 <1:
                    gan3=str(gan3)
                    gan3="0"+ gan3
                if pi3/10<1:
                    pi3=str(pi3)
                    pi3="0"+ pi3
                if zhi3/10<1:
                    zhi3=str(zhi3)
                    zhi3="00"+ zhi3
                elif zhi3/100<1:
                    zhi3=str(zhi3)
                    zhi3="0"+zhi3   
                if ye3/10 <1:
                    ye3=str(ye3)
                    ye3="0"+ ye3 
                if gen3/10<1:
                    gen3=str(gen3)
                    gen3="00"+ gen3
                elif gen3/100<1:
                    gen3=str(gen3)
                    gen3="0"+gen3 
                if zong3/100<1:
                    zong3=str(zong3)
                    zong3="0"+zong3                                            
                text.insert(tk.END,'\n'" {}   {}   {}   {}  {}  {}   {}    {}    {}".format(t,d3,h3,gan3,pi3,zhi3,ye3,gen3,zong3),"tag")
                t=t+5     
    menubar3.add_command(label="生物量表",command=biomass_table)
    menubar.add_cascade(label="林业数表",menu=menubar3)
    menubar4=tk.Menu(menubar,tearoff=False)
    def gay_command():
        global d_gjxs
        global v_gjxs
        if tree==1:
            d_gjlx=ys_DHB(t_gjxs)
            h_gjlx=ys_H(t_gjxs)
            g_gjlx=ys_G(t_gjxs)
            n_gjlx=ys_N(g_gjlx,d_gjlx)
            v_gjlx=ys_V(h_gjlx,g_gjlx)
            d_gjxs=d_gjlx*k3
            d_gjxs_bl="%.1f" % d_gjxs
            h_gjxs=h_gjlx*k4
            h_gjxs_bl="%.1f" % h_gjxs
            n_gjxs_bl=int(n_gjlx*k5)
            v_gjxs=v_gjlx*k6
            v_gjxs_bl="%.1f" % v_gjxs
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n油松\n")
        if tree==2:
            d_gjlx=hs_DHB(t_gjxs)
            h_gjlx=hs_H(t_gjxs)
            g_gjlx=hs_G(t_gjxs)
            n_gjlx=hs_N(g_gjlx,d_gjlx)
            v_gjlx=hs_V(h_gjlx,g_gjlx)
            d_gjxs=d_gjlx*k3
            d_gjxs_bl="%.1f" % d_gjxs
            h_gjxs=h_gjlx*k4
            h_gjxs_bl="%.1f" % h_gjxs
            n_gjxs_bl=int(n_gjlx*k5)
            v_gjxs=v_gjlx*k6
            v_gjxs_bl="%.1f" % v_gjxs
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n华山松\n","tag")
        if tree==4:
            d_gjlx=rc_DHB(t_gjxs)
            h_gjlx=rc_H(t_gjxs)
            g_gjlx=rc_G(t_gjxs)
            n_gjlx=rc_N(g_gjlx,d_gjlx)
            v_gjlx=rc_V(h_gjlx,g_gjlx)
            d_gjxs=d_gjlx*k3
            d_gjxs_bl="%.1f" % d_gjxs
            h_gjxs=h_gjlx*k4
            h_gjxs_bl="%.1f" % h_gjxs
            n_gjxs_bl=int(n_gjlx*k5)
            v_gjxs=v_gjlx*k6
            v_gjxs_bl="%.1f" % v_gjxs
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n锐齿栎\n","tag")
        text.insert(tk.END,"\n ----------------------------------\n")
        text.insert(tk.END,"\n在 {}   年".format(t_gjxs),"tag")
        text.insert(tk.END,"\n立地平均胸径 = {} cm".format(d_gjxs_bl),"tag")
        text.insert(tk.END,"\n立地平均树高 = {} m".format(h_gjxs_bl),"tag")
        text.insert(tk.END,"\n立地密度= {} tree/ha".format(n_gjxs_bl),"tag")
        text.insert(tk.END,"\n立地材积 = {} m3/ha".format(v_gjxs_bl),"tag")
        text.insert(tk.END,"\n ----------------------------------\n")
        def biomass_table():
            if tree==1:
                D=float(d_gjxs)
                H=float(h_gjxs)
                print (D,H)
                gan=ys_gan(D,H)
                gan="%.1f" % gan
                pi=ys_pi(D,H)
                pi="%.1f" % pi
                zhi=ys_zhi(D)
                zhi="%.1f" % zhi
                ye=ys_ye(D)
                ye="%.1f" % ye
                gen=ys_gen(D)
                gen="%.1f" % gen
                text.insert(tk.END,"\n ----------------------------------\n")
                text.insert(tk.END,"\n油松\n","tag")
                gan=float(gan)
                gan_tan="%.1f" % (gan*0.4995)
                pi=float(pi)
                pi_tan="%.1f" % (pi*0.4925)
                zhi=float(zhi)
                zhi_tan="%.1f" % (zhi*0.508)
                ye=float(ye)
                ye_tan="%.1f" % (ye*0.5145)
                gen=float(gen)
                gen_tan="%.1f" % (gen*0.4425)
            if tree==2:
                D=float(d_gjxs)
                H=float(h_gjxs)
                gan=hs_gan(D,H)
                gan="%.1f" % gan
                pi=hs_pi(D,H)
                pi="%.1f" % pi
                zhi=hs_zhi(D)
                zhi="%.1f" % zhi
                ye=hs_ye(D)
                ye="%.1f" % ye
                gen=hs_gen(D,H)
                gen="%.1f" % gen
                text.insert(tk.END,"\n ----------------------------------\n")
                text.insert(tk.END,"\n华山松\n","tag")
                gan=float(gan)
                gan_tan="%.1f" % (gan*0.4832)
                pi=float(pi)
                pi_tan="%.1f" % (pi*0.4337)
                zhi=float(zhi)
                zhi_tan="%.1f" % (zhi*0.5037)
                ye=float(ye)
                ye_tan="%.1f" % (ye*0.5135)
                gen=float(gen)
                gen_tan="%.1f" % (gen*0.4759)

            if tree==4:    
                D=float(d_gjxs)
                H=float(h_gjxs)
                gan=rc_gan(D,H)
                gan="%.1f" % gan
                pi=rc_pi(D,H)
                pi="%.1f" % pi
                zhi=rc_zhi(D)
                zhi="%.1f" % zhi
                ye=rc_ye(D)
                ye="%.1f" % ye
                gen=rc_gen(D)
                gen="%.1f" % gen
                text.insert(tk.END,"\n ----------------------------------\n")
                text.insert(tk.END,"\n锐齿栎\n","tag")
                gan=float(gan)
                gan_tan="%.1f" % (gan*0.4679)
                pi=float(pi)
                pi_tan="%.1f" % (pi*0.4791)
                zhi=float(zhi)
                zhi_tan="%.1f" % (zhi*0.4661)
                ye=float(ye)
                ye_tan="%.1f" % (ye*0.4328)
                gen=float(gen)
                gen_tan="%.1f" % (gen*0.4857)
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n 生物量估计")
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n 茎的生物量 {} t/ha".format(gan))
            text.insert(tk.END,"\n 皮的生物量 {} t/ha".format(pi))
            text.insert(tk.END,"\n 枝的生物量 {} t/ha".format(zhi))
            text.insert(tk.END,"\n 叶的生物量 {} t/ha".format(ye))
            text.insert(tk.END,"\n 根的生物量 {} t/ha".format(gen))
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n 碳储量估计")
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n 茎的碳储量 {} t/ha".format(gan_tan))
            text.insert(tk.END,"\n 皮的碳储量 {} t/ha".format(pi_tan))
            text.insert(tk.END,"\n 枝的碳储量 {} t/ha".format(zhi_tan))
            text.insert(tk.END,"\n 叶的碳储量 {} t/ha".format(ye_tan))
            text.insert(tk.END,"\n 根的碳储量 {} t/ha".format(gen_tan))      
            text.insert(tk.END,"\n ----------------------------------\n") 
        command_biomass=tk.Button(root,text="生物量和碳储量",height=2,width=20,command=biomass_table)
        command_biomass.place(x=600,y=20)
    menubar4.add_command(label="生长及产量",command=gay_command)
    def it_command():
        it=tk.Tk()
        it.title("单木")
        it.geometry("450x300+500+200")
        l11=tk.Label(it,text="较大树种断面积")
        l11.place(x=50,y=20)
        l22=tk.Label(it,text=" 立地条件总断面积")
        l22.place(x=50,y=50)
        l33=tk.Label(it,text="胸高处的单木直径")
        l33.place(x=50,y=80)
        l44=tk.Label(it,text="立地肥力等级")
        l44.place(x=50,y=110)
        entry11=tk.Entry(it)
        entry11.insert(0, '40')
        entry11.place(x=250,y=20)
        entry22=tk.Entry(it)
        entry22.insert(0, '2000')
        entry22.place(x=250,y=50)
        entry33=tk.Entry(it)
        entry33.insert(0, '20')
        entry33.place(x=250,y=80)
        entry44=tk.Entry(it)
        entry44.insert(0, '4')
        entry44.place(x=250,y=110)
        def ok3_command():
            global GD
            global G
            global d
            global h30
            GD=int(entry11.get())
            G=float(entry22.get())
            d=float(entry33.get())
            h30=float(entry44.get())
            i=ii(GD,G,d,h30)
            i=float("%.2f" % i)
            p=pp(d,GD)
            p=float("%.4f" % p)
            H=Hh(h30,d)
            H=float("%.2f" % H)
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n5年直径增长量:{}".format(i),"tag")
            text.insert(tk.END,"\n5年内存活的可能性:{}".format(p),"tag")
            text.insert(tk.END,"\n单木树高: {}".format(H),"tag")
            text.insert(tk.END,"\n ----------------------------------\n")
            it.destroy()
        def concel3_command():
            it.destroy()
        ok3=tk.Button(it,text="OK",height=2,width=10,command=ok3_command)
        ok3.place(x=50,y=220)
        concel3=tk.Button(it,text="Concel",height=2,width=10,command=concel3_command)
        concel3.place(x=200,y=220)
    menubar4.add_command(label="单木",command=it_command)
    menubar.add_cascade(label="模拟估计",menu=menubar4)
    def about_command():
        tk.messagebox.showinfo('关于','BY GMH ')
    menubar.add_command(label="关于",command=about_command)
    def help_command():
        help=tk.Tk()
        help.title("帮助")
        help.geometry("800x400+500+200")
        text_help=tk.Text(help,height=800,width=300,state="normal")
        text_help.pack()
        text_help.insert(tk.END,"\nQUSSI is a stand simulator, which can predict stand factors of certain tree species under certain site conditions. The specific structure is as follows\n")
        text_help.insert(tk.END,"\n<file>-----")
        text_help.insert(tk.END,"\n            <save>----You can save the displayed text to your computer")
        text_help.insert(tk.END,"\n            <open>----You can open the text stored on the computer to the interface")  
        text_help.insert(tk.END,"\n            <exit>----Exit the software")
        text_help.insert(tk.END,"\n<setting>--")
        text_help.insert(tk.END,"\n            <tree speices>----Choose the tree species you want to simulate")
        text_help.insert(tk.END,"\n            <stand condition>--Choose the stand condition you want to simulate")
        text_help.insert(tk.END,"\n            <finance>")
        text_help.insert(tk.END,"\n<table>----")   
        text_help.insert(tk.END,"\n            <normal stand yield table>-----Output the normal stand growth table of selected tree species")
        text_help.insert(tk.END,"\n            <site index table>-------------Output the site index table of selected tree species")
        text_help.insert(tk.END,"\n            <standard volume table>--------Output the binary volume table of the selected tree species")
        text_help.insert(tk.END,"\n<simualation>")
        text_help.insert(tk.END,"\n            <Growth and yield>-------------Simulate the growth and volume of the selected tree species under the site conditions")
        text_help.insert(tk.END,"\n<about>-----about this software")
    menubar.add_command(label="帮助",command=help_command)
    def clear_command():
        text.delete(0.0, 'end')
    menubar.add_command(label="清理页面",command=clear_command)
    root.config(menu=menubar)
    root.mainloop()
def language_selection2():
    root=tk.Tk()
    root.title("QUASSI")
    root.geometry("1200x500+200+200")
    text=tk.Text(root,height=800,width=300,state="normal")
    text.pack()
    ft=tf.Font(family="微软雅黑",size=10)
    text.tag_add("tag",tk.END)
    text.tag_config("tag",font=ft)
    menubar=tk.Menu(root)
    def open_file():
        global file_path
        global file_text
        file_path = filedialog.askopenfilename(title='select file', initialdir=(os.path.expanduser('H:/')))
        if file_path is not None:
            with open(file=file_path, mode='r+', encoding='utf-8') as file:
                file_text = file.read()
            text.insert('insert', file_text)
    def save_file():
        global file_path
        global file_text
        file_path = filedialog.asksaveasfilename(title='save file',initialfile='tree.text')
        file_text = text.get('1.0', tk.END)
        if file_path is not None:
            with open(file=file_path, mode='a+', encoding='utf-8') as file:
                file.write(file_text)
            text.delete('1.0', tk.END)
            dialog.Dialog(None, {'title': 'File Modified', 'text': 'ok', 'bitmap': 'warning', 'default': 0,
                                'strings': ('OK', 'Cancle')})
            print('保存完成')
    def exit_file():
        root.destroy()
    menubar1=tk.Menu(menubar,tearoff=False)
    menubar1.add_command(label="save",command=save_file)
    menubar1.add_command(label="open",command=open_file)
    menubar1.add_command(label="exit",command=exit_file)
    menubar.add_cascade(label="file",menu=menubar1)
    menubar2=tk.Menu(menubar,tearoff=False)
    def ts_command():
        root2=tk.Tk()
        root2.title("tree speices")
        root2.geometry("300x300+500+200")
        var = tk.StringVar()
        selecttree_label=tk.Label(root2,textvar=var,width=30,height=1,text="you must select a tree speice")
        selecttree_label.place(x=0,y=150)
        def print_selection1():
            global tree
            tree=1
        def print_selection2():
            global tree
            tree=2

        def print_selection4():
            global tree
            tree=4
        treespeices1=tk.Radiobutton(root2,text="Pinus tabulaeformis",var=var,value="Pinus tabulaeformis",command=print_selection1,indicatoron=False)
        treespeices1.place(x=40,y=20)
        treespeices2=tk.Radiobutton(root2,text="Pinus armandii",var=var,value="Pinus armandii",command=print_selection2,indicatoron=False)
        treespeices2.place(x=40,y=65)

        treespeices4=tk.Radiobutton(root2,text="Quercus aliena",var=var,value="Quercus aliena",command=print_selection4,indicatoron=False)
        treespeices4.place(x=40,y=110)
        def ok_command():
            root2.destroy()
        def Cancel_command():
            var.set(0)
            root2.destroy()
        ok=tk.Button(root2,text="OK",height=2,width=10,command=ok_command)
        ok.place(x=40,y=200)
        concel=tk.Button(root2,text="Concel",height=2,width=10,command=Cancel_command)
        concel.place(x=150,y=200)
    menubar2.add_command(label="tree speices",command=ts_command)
    def stand_condition():
        stand=tk.Tk()
        stand.title("stand condition")
        stand.geometry("450x300+500+200")
        l1=tk.Label(stand,text="Site class")
        l1.place(x=50,y=20)
        l2=tk.Label(stand,text="Stand age")
        l2.place(x=50,y=50)
        l3=tk.Label(stand,text="Average diameter")
        l3.place(x=50,y=80)
        l4=tk.Label(stand,text="Average height")
        l4.place(x=50,y=110)
        l5=tk.Label(stand,text="Stand density")
        l5.place(x=50,y=140)
        l6=tk.Label(stand,text="Stand volume")
        l6.place(x=50,y=170)
        l7=tk.Label(stand,text="Simulating age")
        l7.place(x=50,y=200)
        entry1=tk.Entry(stand)
        entry1.insert(0, '1')
        entry1.place(x=160,y=20)
        entry2=tk.Entry(stand)
        entry2.insert(0, '20')
        entry2.place(x=160,y=50)
        entry3=tk.Entry(stand)
        entry3.insert(0, '12')
        entry3.place(x=160,y=80)
        entry4=tk.Entry(stand)
        entry4.insert(0, '12')
        entry4.place(x=160,y=110)
        entry5=tk.Entry(stand)
        entry5.insert(0, '2000')
        entry5.place(x=160,y=140)
        entry6=tk.Entry(stand)
        entry6.insert(0, '150')
        entry6.place(x=160,y=170)
        entry7=tk.Entry(stand)
        entry7.insert(0, '50')
        entry7.place(x=160,y=200)
        def ok2_command():
            global t_xs
            global d_xs
            global h_xs
            global n_xs
            global v_xs
            global t_gjxs
            global k3
            global k4
            global k5
            global k6
            t_xs=int(entry2.get())
            d_xs=float(entry3.get())
            h_xs=float(entry4.get())
            n_xs=float(entry5.get())
            v_xs=float(entry6.get())
            t_gjxs=int(entry7.get())
            if tree==1:
                d_lx=ys_DHB(t_xs)
                h_lx=ys_H(t_xs)
                g_lx=ys_G(t_xs)
                n_lx=ys_N(g_lx,d_lx)
                v_lx=ys_V(h_lx,g_lx)
                k3=d_xs/d_lx
                k4=h_xs/h_lx
                k5=n_xs/n_lx
                k6=v_xs/v_lx
            if tree==2:
                d_lx=hs_DHB(t_xs)
                h_lx=hs_H(t_xs)
                g_lx=hs_G(t_xs)
                n_lx=hs_N(g_lx,d_lx)
                v_lx=hs_V(h_lx,g_lx)
                k3=d_xs/d_lx
                k4=h_xs/h_lx
                k5=n_xs/n_lx
                k6=v_xs/v_lx           
  
            if tree==4:
                d_lx=rc_DHB(t_xs)
                h_lx=rc_H(t_xs)
                g_lx=rc_G(t_xs)
                n_lx=rc_N(g_lx,d_lx)
                v_lx=rc_V(h_lx,g_lx)
                k3=d_xs/d_lx
                k4=h_xs/h_lx
                k5=n_xs/n_lx
                k6=v_xs/v_lx      
            stand.destroy() 
        def concel2_command():
            stand.destroy()
        ok2=tk.Button(stand,text="OK",height=2,width=10,command=ok2_command)
        ok2.place(x=50,y=220)
        concel2=tk.Button(stand,text="Concel",height=2,width=10,command=concel2_command)
        concel2.place(x=200,y=220)
    menubar2.add_command(label="stand condition",command=stand_condition)
    menubar.add_cascade(label="setting",menu=menubar2)
    menubar3=tk.Menu(menubar,tearoff=False)
    def jingjie_condition():
        jingjie=tk.Tk()
        jingjie.title("Diameter step setting")
        jingjie.geometry("450x300+500+200")
        jj1=tk.Label(jingjie,text="DBH range10-19.9（cm）")
        jj1.place(x=50,y=20)
        jj2=tk.Label(jingjie,text="DBH range20-34.9（cm）")
        jj2.place(x=50,y=50)
        jj3=tk.Label(jingjie,text="DBH range35+（cm）")
        jj3.place(x=50,y=80)
        entry11=tk.Entry(jingjie)
        entry11.insert(0, '840')
        entry11.place(x=300,y=20)
        entry22=tk.Entry(jingjie)
        entry22.insert(0, '234')
        entry22.place(x=300,y=50)
        entry33=tk.Entry(jingjie)
        entry33.insert(0, '14')
        entry33.place(x=300,y=80)
        jf1=tk.Label(jingjie,text="thinning method(crown thinning=1，Middle thinning =2， low thinning=3)")
        jf1.place(x=50,y=110)
        jj2=tk.Label(jingjie,text="Thinning intensity(%)")
        jj2.place(x=50,y=140)
        jj3=tk.Label(jingjie,text="Thinning time(年)")
        jj3.place(x=50,y=170)
        jf11=tk.Entry(jingjie)
        jf11.insert(0, '0')
        jf11.place(x=300,y=110)
        jf22=tk.Entry(jingjie)
        jf22.insert(0, '0')
        jf22.place(x=300,y=140)
        jf33=tk.Entry(jingjie)
        jf33.insert(0, '0')
        jf33.place(x=300,y=170)
        def ok3_command():
            global t_xs
            global d_xs
            global h_xs
            global n_xs
            global v_xs
            global t_gjxs
            global k3
            global k4
            global k5
            global k6
            t=0
            y01=int(entry11.get())
            y02=int(entry22.get())
            y03=int(entry33.get())
            ff=int(jf11.get())
            qd=int(jf22.get())
            qd=qd*0.01
            nf=int(jf33.get())
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n         Plants per hectare","tag")
            text.insert(tk.END,"\n       Qinling Quercus tabulaeformis mixed forest ","tag") 
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n      thinning method {} (crown thinning=1，Middle thinning =2， low thinning=3) ".format(ff),"tag") 
            text.insert(tk.END,"\n      Thinning intensity{}%  ".format(qd*100),"tag") 
            text.insert(tk.END,"\n      Thinning time{}年  ".format(nf),"tag")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\nAge   First diameter class   Second diameter class   Third diameter class")
            while t<85:
                if t/10 <1:
                    t=str(t)
                    t="0"+ t
                text.insert(tk.END,'\n'" {}       {}                  {}                 {}  ".format(t,y01,y02,y03),"tag")
                t=int(t)
                t=t+5 
                if ff==0:
                    y1=int(0.92*y01-0.29*y02-0.96*y03+109)
                    y2=int(0.04*y01+0.9*y02)
                    y3=int(0.02*y02+0.9*y03)
                    y01=y1
                    y02=y2
                    y03=y3
                    t=int(t)
                if ff==1:
                    y1=int(0.92*y01-0.29*y02-0.96*y03+109)
                    y2=int(0.04*y01+0.9*y02)
                    y3=int(0.02*y02+0.9*y03)
                    t=int(t)
                    if t % nf == 0:
                        y3=(1-qd)*y3
                    y01=int(y1)
                    y02=int(y2)
                    y03=int(y3)
                    t=int(t)
                if ff==2:
                    y1=int(0.92*y01-0.29*y02-0.96*y03+109)
                    y2=int(0.04*y01+0.9*y02)
                    y3=int(0.02*y02+0.9*y03)
                    t=int(t)
                    if t % nf == 0:
                        y2=(1-qd)*y2
                    y01=int(y1)
                    y02=int(y2)
                    y03=int(y3)
                    t=int(t)     
                if ff==3:
                    y1=int(0.92*y01-0.29*y02-0.96*y03+109)
                    y2=int(0.04*y01+0.9*y02)
                    y3=int(0.02*y02+0.9*y03)
                    t=int(t)
                    if t % nf == 0:
                        y1=(1-qd)*y1
                    y01=int(y1)
                    y02=int(y2)
                    y03=int(y3)
                    t=int(t)                          
            jingjie.destroy()
        def concel3_command():
            jingjie.destroy()
        ok3=tk.Button(jingjie,text="OK",height=2,width=10,command=ok3_command)
        ok3.place(x=50,y=220)
        concel3=tk.Button(jingjie,text="Concel",height=2,width=10,command=concel3_command)
        concel3.place(x=200,y=220)
    menubar2.add_command(label="Diameter step setting",command=jingjie_condition)

    menubar3=tk.Menu(menubar,tearoff=False)
    def nomal_table():
        t=20
        if tree==1:
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                Normal Stand Yield Table")
            text.insert(tk.END,"\n                                   Pinus tabulaeformis  ")   
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\nAGE        DBH         Height       BasalA         #tree       Volume        Average volume of individual             Annual growth       Average growth")
            while t<85:
                D=ys_DHB(t)
                d1=float("%.1f" % D)
                H=ys_H(t)
                h1=float("%.1f" % H)
                G=ys_G(H)
                g1="%.2f" % G
                V=ys_V(H,G)
                v1=float("%.1f" % V)
                N=ys_N(G,D)
                n1=int(N)
                yH=ys_H(t-1)
                yG=ys_G(yH)
                A1=ys_V(H,G)-ys_V(yH,yG)
                a1=float("%.1f" % A1)
                Av1=V/t
                av1=float("%.1f" % Av1)
                Avo=V/N
                avo1=float("%.4f" % Avo )
                if h1/10 <1:
                    h1=str(h1)
                    h1="0"+ h1
                if d1/10 <1:
                    d1=str(d1)
                    d1="0"+ d1
                if n1/1000 <1:
                    n1=str(n1)
                    n1="0"+ n1
                text.insert(tk.END,'\n'"{}     {}     {}     {}     {}     {}             {}                   {}           {}".format(t,d1,h1,g1,n1,v1,avo1,a1,av1),"tag")
                t=t+5 
        if tree==2:
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                Normal Stand Yield Table")
            text.insert(tk.END,"\n                                     Pinus armandii  ")   
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\nAGE        DBH         Height       BasalA         #tree       Volume        Average volume of individual             Annual growth       Average growth")
            while t<85:
                D=hs_DHB(t)
                d2=float("%.1f" % D)
                H=hs_H(t)
                h2=float("%.1f" % H)
                G=hs_G(H)
                g2="%.2f" % G
                V=hs_V(H,G)
                v2="%.1f" % V
                N=hs_N(G,D)
                n2=int(N)
                yH=hs_H(t-1)
                yG=hs_G(yH)
                A2=hs_V(H,G)-hs_V(yH,yG)
                a2=float("%.1f" % A2)
                Av2=V/t
                av2=float("%.1f" % Av2)
                Avo=V/N
                avo2=float("%.4f" % Avo )
                avo2=format(avo2, '.4f')
                if h2/10 <1:
                    h2=str(h2)
                    h2="0"+ h2
                if d2/10 <1:
                    d2=str(d2)
                    d2="0"+ d2
                if n2/1000 <1:
                    n2=str(n2)
                    n2="0"+ n2
                if a2/10 <1:
                    a2=str(a2)
                    a2="0"+ a2
                if av2/10 <1:
                    av2=str(av2)
                    av2="0"+ av2
                text.insert(tk.END,'\n'"{}     {}     {}     {}     {}     {}             {}                   {}           {}".format(t,d2,h2,g2,n2,v2,avo2,a2,av2),"tag")
                t=t+5

        if tree==4:
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                Normal Stand Yield Table")
            text.insert(tk.END,"\n                                      Quercus aliena ")   
            text.insert(tk.END,"\n---------------------------------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\nAGE        DBH         Height       BasalA         #tree       Volume        Average volume of individual             Annual growth       Average growth")
            while t<85:
                D=rc_DHB(t)
                d4=float("%.1f" % D)
                H=rc_H(t)
                h4=float("%.1f" % H)
                G=rc_G(H)
                g4="%.2f" % G
                V=rc_V(H,G)
                v4=float("%.1f" % V)
                N=rc_N(G,D)
                n4=int(N)
                yH=rc_H(t-1)
                yG=rc_G(yH)
                A4=rc_V(H,G)-rc_V(yH,yG)
                a4=float("%.1f" % A4)
                Av4=v4/t
                av4=float("%.1f" % Av4)
                Avo=v4/N
                avo4=float("%.4f" % Avo)
                avo4=format(avo4, '.4f')
                if h4/10 <1:
                    h4=str(h4)
                    h4="0"+ h4
                if d4/10 <1:
                    d4=str(d4)
                    d4="0"+ d4
                if n4/1000 <1:
                    n4=str(n4)
                    n4="0"+ n4
                text.insert(tk.END,'\n'"{}     {}     {}     {}     {}     {}             {}                   {}           {}".format(t,d4,h4,g4,n4,v4,avo4,a4,av4),"tag")
                t=t+5 
    menubar3.add_command(label="normal stand yield table",command=nomal_table)
    def index_table():
        def ys_index(H_dom,t0,t):
            s1=float(H_dom*((1-math.exp(-(t0/25.679)**1.465))/(1-math.exp(-(t/25.679)**1.465))))
            return s1
        def hs_index(H_dom,t0,t):
            s2=float(H_dom*((1+math.pow(t0/157.453,-0.789))/(1+math.pow(t/157.453,-0.789))))
            return s2
        def ly_index(H_dom,t0,t):
            s3=float(H_dom*math.exp(math.exp((16.821-t)/12.496)-math.exp((16.821-t0)/12.496)))
            return s3
        def rc_index(H_dom,t0,t):
            s4=float(H_dom*math.exp(15.4*(1/(t+2.95)-1/(t0+2.95))))
            return s4
        if tree==1:
            text.insert(tk.END,"\n-------------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                Site index table")
            text.insert(tk.END,"\n                                   Pinus tabulaeformis  ")   
            text.insert(tk.END,"\n-----------------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n  AGE    8       9       10      11      12      13      14      15")
            text.insert(tk.END,"\n")
            s1=0
            t=20
            H_dom=8
            while t<60:
                text.insert(tk.END,"  {}".format(t))
                H_dom=8
                while H_dom<16:
                    s1=ys_index(H_dom,30,t)
                    s1=float("%.1f" % s1)
                    if s1/10 <1:
                        s1=str(s1)
                        s1="0"+ s1
                    text.insert(tk.END,"    {}".format(s1))
                    H_dom=H_dom+1
                text.insert(tk.END,"\n")
                t=t+2
            text.insert(tk.END,"                                                                Standard age：30年")
        if tree==2:
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                Site index table")
            text.insert(tk.END,"\n                                 Pinus armandii    ")   
            text.insert(tk.END,"\n----------------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n  AGE    8       9       10      11      12      13      14      15")
            text.insert(tk.END,"\n")
            s2=0
            t=20
            H_dom=8
            while t<60:
                text.insert(tk.END,"  {}".format(t))
                H_dom=8
                while H_dom<16:
                    s2=hs_index(H_dom,30,t)
                    s2=float("%.1f" % s2)
                    if s2/10 <1:
                        s2=str(s2)
                        s2="0"+ s2
                    text.insert(tk.END,"    {}".format(s2))
                    H_dom=H_dom+1
                text.insert(tk.END,"\n")
                t=t+2
            text.insert(tk.END,"                                                                Standard age：30年")

        if tree==4:
            text.insert(tk.END,"\n-------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                Site index table")
            text.insert(tk.END,"\n                                 Quercus aliena    ")   
            text.insert(tk.END,"\n-------------------------------------------------------------------------------------------------------")
            text.insert(tk.END,"\n  AGE    8       9       10      11      12      13      14      15")
            text.insert(tk.END,"\n")
            s4=0
            t=20
            H_dom=8
            while t<60:
                text.insert(tk.END,"  {}".format(t))
                H_dom=8
                while H_dom<16:
                    s4=rc_index(H_dom,15,t)
                    s4=float("%.1f" % s4)
                    if s4/10 <1:
                        s4=str(s4)
                        s4="0"+ s4
                    text.insert(tk.END,"    {}".format(s4))
                    H_dom=H_dom+1
                text.insert(tk.END,"\n")
                t=t+2
            text.insert(tk.END,"                                                                Standard age：15年")
    menubar3.add_command(label="site index stand",command=index_table)
    def volumn_table():
        def ys_volume(D,H):
            v1=(0.719*3.14*D**(2-0.092)*H**(1-0.031))/40000
            return v1
        def hs_volume(D,H):
            v2=(0.686*3.14*D**(2-0.186)*H**1.105)/40000
            return v2
        def ly_volume(D,H):
            v3=0.001*D**1.719*H**1.204
            return v3
        def rc_volume(D,H):
            v4=(0.728*3.14*D**(2-0.166)*H**1.015)/40000
            return v4
        if tree==1:
            text.insert(tk.END,"\n     Height  6.0          8.0          10.0        12.0         14.0         16.0         18.0          20.0 ")
            text.insert(tk.END,"\ndiameter --------------------------------------------------------------------------------------------------")
            D=6
            while D<30:
                if D/10<1:
                    D=str(D)
                    D="0"+ D
                text.insert(tk.END,"\n  {}".format(D))
                D=int(D)
                H=6
                while H<21:
                    v1=ys_volume(D,H)
                    v1="%.4f" % v1
                    text.insert(tk.END,"       {}".format(v1))
                    H=H+2
                text.insert(tk.END,"\n")
                D=D+2
        if tree==2:
            text.insert(tk.END,"\n     Height  6.0          8.0          10.0        12.0         14.0         16.0         18.0          20.0 ")
            text.insert(tk.END,"\ndiameter --------------------------------------------------------------------------------------------------")
            D=6
            while D<30:
                if D/10<1:
                    D=str(D)
                    D="0"+ D
                text.insert(tk.END,"\n  {}".format(D))
                D=int(D)
                H=6
                while H<21:
                    v2=hs_volume(D,H)
                    v2="%.4f" % v2
                    text.insert(tk.END,"       {}".format(v2))
                    H=H+2
                text.insert(tk.END,"\n")
                D=D+2

        if tree==4:
            text.insert(tk.END,"\n     Height  6.0          8.0          10.0        12.0         14.0         16.0         18.0          20.0 ")
            text.insert(tk.END,"\ndiameter --------------------------------------------------------------------------------------------------")
            D=6
            while D<30:
                if D/10<1:
                    D=str(D)
                    D="0"+ D
                text.insert(tk.END,"\n  {}".format(D))
                D=int(D)
                H=6
                while H<21:
                    v4=rc_volume(D,H)
                    v4="%.4f" % v4
                    text.insert(tk.END,"       {}".format(v4))
                    H=H+2
                text.insert(tk.END,"\n")
                D=D+2
    menubar3.add_command(label="standard volume table",command=volumn_table)
    def biomass_table():
        t=20
        if tree==1:
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                     Biomass table")
            text.insert(tk.END,"\n                                     Pinus tabulaeformis ")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\nAGE       DBH      Height     Stem      Bark    Branch     Foliage     Root        Stand  ")
            while t<85:
                D=ys_DHB(t)
                d1=float("%.1f" % D)
                H=ys_H(t)
                h1=float("%.1f" % H)
                gan=ys_gan(D,H)
                gan1=float("%.1f" % gan)
                pi=ys_pi(D,H)
                pi1=float("%.1f" % pi)
                zhi=ys_zhi(D)
                zhi1=float("%.1f" % zhi)
                ye=ys_ye(D)
                ye1=float("%.1f" % ye)
                gen=ys_gen(D)
                gen1=float("%.1f" % gen)
                zong=gan1+pi1+zhi1+ye1+gen1
                zong1=float("%.1f" % zong)
                if h1/10 <1:
                    h1=str(h1)
                    h1="0"+ h1
                if d1/10 <1:
                    d1=str(d1)
                    d1="0"+ d1
                if gan1/100 <1:
                    gan1=str(gan1)
                    gan1="0"+ gan1
                if pi1/10<1:
                    pi1=str(pi1)
                    pi1="0"+ pi1
                if zhi1/10<1:
                    zhi1=str(zhi1)
                    zhi1="00"+ zhi1
                elif zhi1/100<1:
                    zhi1=str(zhi1)
                    zhi1="0"+zhi1   
                if ye1/10 <1:
                    ye1=str(ye1)
                    ye1="0"+ ye1 
                if gen1/10 <1:
                    gen1=str(gen1)
                    gen1="0"+ gen1
                if zong1/100<1:
                    zong1=str(zong1)
                    zong1="0"+zong1                                            
                text.insert(tk.END,'\n'" {}   {}   {}   {}  {}  {}   {}    {}    {}".format(t,d1,h1,gan1,pi1,zhi1,ye1,gen1,zong1),"tag")
                t=t+5 
        if tree==2:
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                     Biomass table")
            text.insert(tk.END,"\n                                      Pinus armandii ")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\nAGE       DBH      Height     Stem      Bark    Branch     Foliage     Root        Stand  ")
            while t<85:
                D=hs_DHB(t)
                d2=float("%.1f" % D)
                H=hs_H(t)
                h2=float("%.1f" % H)
                gan=hs_gan(D,H)
                gan2=float("%.1f" % gan)
                pi=hs_pi(D,H)
                pi2=float("%.1f" % pi)
                zhi=hs_zhi(D)
                zhi2=float("%.1f" % zhi)
                ye=hs_ye(D)
                ye2=float("%.1f" % ye)
                gen=hs_gen(D,H)
                gen2=float("%.1f" % gen)
                zong=gan2+pi2+zhi2+ye2+gen2
                zong2=float("%.1f" % zong)
                if h2/10 <1:
                    h2=str(h2)
                    h2="0"+ h2
                if d2/10 <1:
                    d2=str(d2)
                    d2="0"+ d2
                if gan2/100 <1:
                    gan2=str(gan2)
                    gan2="0"+ gan2
                if pi2/10<1:
                    pi2=str(pi2)
                    pi2="0"+ pi2
                if zhi2/10<1:
                    zhi2=str(zhi2)
                    zhi2="00"+ zhi2
                elif zhi2/100<1:
                    zhi2=str(zhi2)
                    zhi2="0"+zhi2   
                if ye2/10 <1:
                    ye2=str(ye2)
                    ye2="0"+ ye2 
                if gen2/10 <1:
                    gen2=str(gen2)
                    gen2="0"+ gen2
                if zong2/100<1:
                    zong2=str(zong2)
                    zong2="0"+zong2                                            
                text.insert(tk.END,'\n'" {}   {}   {}   {}  {}  {}   {}    {}    {}".format(t,d2,h2,gan2,pi2,zhi2,ye2,gen2,zong2),"tag")
                t=t+5 
  
        if tree==4:
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")    
            text.insert(tk.END,"\n                                    Biomass table")
            text.insert(tk.END,"\n                                      Quercus aliena ")   
            text.insert(tk.END,"\n------------------------------------------------------------------------------------------------------")   
            text.insert(tk.END,"\nAGE       DBH      Height     Stem      Bark    Branch     Foliage     Root        Stand  ")
            while t<85:
                D=rc_DHB(t)
                d3=float("%.1f" % D)
                H=rc_H(t)
                h3=float("%.1f" % H)
                gan=rc_gan(D,H)
                gan3=float("%.1f" % gan)
                pi=rc_pi(D,H)
                pi3=float("%.1f" % pi)
                zhi=rc_zhi(D)
                zhi3=float("%.1f" % zhi)
                ye=rc_ye(D)
                ye3=float("%.1f" % ye)
                gen=rc_gen(D)
                gen3=float("%.1f" % gen)
                zong=gan3+pi3+zhi3+ye3+gen3
                zong3=float("%.1f" % zong)
                if h3/10 <1:
                    h3=str(h3)
                    h3="0"+ h3
                if d3/10 <1:
                    d3=str(d3)
                    d3="0"+ d3
                if gan3/100 <1:
                    gan3=str(gan3)
                    gan3="0"+ gan3
                if pi3/10<1:
                    pi3=str(pi3)
                    pi3="0"+ pi3
                if zhi3/10<1:
                    zhi3=str(zhi3)
                    zhi3="00"+ zhi3
                elif zhi3/100<1:
                    zhi3=str(zhi3)
                    zhi3="0"+zhi3   
                if ye3/10 <1:
                    ye3=str(ye3)
                    ye3="0"+ ye3 
                if gen3/10<1:
                    gen3=str(gen3)
                    gen3="00"+ gen3
                elif gen3/100<1:
                    gen3=str(gen3)
                    gen3="0"+gen3 
                if zong3/100<1:
                    zong3=str(zong3)
                    zong3="0"+zong3                                            
                text.insert(tk.END,'\n'" {}   {}   {}   {}  {}  {}   {}    {}    {}".format(t,d3,h3,gan3,pi3,zhi3,ye3,gen3,zong3),"tag")
                t=t+5     
    menubar3.add_command(label="biomass table",command=biomass_table)
    menubar.add_cascade(label="table",menu=menubar3)
    menubar4=tk.Menu(menubar,tearoff=False)
    def gay_command():
        global d_gjxs
        global v_gjxs
        if tree==1:
            d_gjlx=ys_DHB(t_gjxs)
            h_gjlx=ys_H(t_gjxs)
            g_gjlx=ys_G(t_gjxs)
            n_gjlx=ys_N(g_gjlx,d_gjlx)
            v_gjlx=ys_V(h_gjlx,g_gjlx)
            d_gjxs=d_gjlx*k3
            d_gjxs_bl="%.1f" % d_gjxs
            h_gjxs=h_gjlx*k4
            h_gjxs_bl="%.1f" % h_gjxs
            n_gjxs_bl=int(n_gjlx*k5)
            v_gjxs=v_gjlx*k6
            v_gjxs_bl="%.1f" % v_gjxs
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\nPinus tabulaeformis\n","tag")
        if tree==2:
            d_gjlx=hs_DHB(t_gjxs)
            h_gjlx=hs_H(t_gjxs)
            g_gjlx=hs_G(t_gjxs)
            n_gjlx=hs_N(g_gjlx,d_gjlx)
            v_gjlx=hs_V(h_gjlx,g_gjlx)
            d_gjxs=d_gjlx*k3
            d_gjxs_bl="%.1f" % d_gjxs
            h_gjxs=h_gjlx*k4
            h_gjxs_bl="%.1f" % h_gjxs
            n_gjxs_bl=int(n_gjlx*k5)
            v_gjxs=v_gjlx*k6
            v_gjxs_bl="%.1f" % v_gjxs
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\nPinus armandii\n","tag")

        if tree==4:
            d_gjlx=rc_DHB(t_gjxs)
            h_gjlx=rc_H(t_gjxs)
            g_gjlx=rc_G(t_gjxs)
            n_gjlx=rc_N(g_gjlx,d_gjlx)
            v_gjlx=rc_V(h_gjlx,g_gjlx)
            d_gjxs=d_gjlx*k3
            d_gjxs_bl="%.1f" % d_gjxs
            h_gjxs=h_gjlx*k4
            h_gjxs_bl="%.1f" % h_gjxs
            n_gjxs_bl=int(n_gjlx*k5)
            v_gjxs=v_gjlx*k6
            v_gjxs_bl="%.1f" % v_gjxs
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\nQuercus aliena\n","tag")
        text.insert(tk.END,"\n ----------------------------------\n")
        text.insert(tk.END,"\nAt {}   years".format(t_gjxs),"tag")
        text.insert(tk.END,"\nStand average diameter = {} cm".format(d_gjxs_bl),"tag")
        text.insert(tk.END,"\nStand average height = {} m".format(h_gjxs_bl),"tag")
        text.insert(tk.END,"\nStand density= {} tree/ha".format(n_gjxs_bl),"tag")
        text.insert(tk.END,"\nStand volume = {} m3/ha".format(v_gjxs_bl),"tag")
        text.insert(tk.END,"\n ----------------------------------\n")
        def biomass_table():
            if tree==1:
                D=float(d_gjxs)
                H=float(h_gjxs)
                print (D,H)
                gan=ys_gan(D,H)
                gan="%.1f" % gan
                pi=ys_pi(D,H)
                pi="%.1f" % pi
                zhi=ys_zhi(D)
                zhi="%.1f" % zhi
                ye=ys_ye(D)
                ye="%.1f" % ye
                gen=ys_gen(D)
                gen="%.1f" % gen
                text.insert(tk.END,"\n ----------------------------------\n")
                text.insert(tk.END,"\nPinus tabulaeformis\n","tag")
                gan=float(gan)
                gan_tan="%.1f" % (gan*0.4995)
                pi=float(pi)
                pi_tan="%.1f" % (pi*0.4925)
                zhi=float(zhi)
                zhi_tan="%.1f" % (zhi*0.508)
                ye=float(ye)
                ye_tan="%.1f" % (ye*0.5145)
                gen=float(gen)
                gen_tan="%.1f" % (gen*0.4425)
            if tree==2:
                D=float(d_gjxs)
                H=float(h_gjxs)
                gan=hs_gan(D,H)
                gan="%.1f" % gan
                pi=hs_pi(D,H)
                pi="%.1f" % pi
                zhi=hs_zhi(D)
                zhi="%.1f" % zhi
                ye=hs_ye(D)
                ye="%.1f" % ye
                gen=hs_gen(D,H)
                gen="%.1f" % gen
                text.insert(tk.END,"\n ----------------------------------\n")
                text.insert(tk.END,"\nPinus armandii\n","tag")
                gan=float(gan)
                gan_tan="%.1f" % (gan*0.4832)
                pi=float(pi)
                pi_tan="%.1f" % (pi*0.4337)
                zhi=float(zhi)
                zhi_tan="%.1f" % (zhi*0.5037)
                ye=float(ye)
                ye_tan="%.1f" % (ye*0.5135)
                gen=float(gen)
                gen_tan="%.1f" % (gen*0.4759)

            if tree==4:    
                D=float(d_gjxs)
                H=float(h_gjxs)
                gan=rc_gan(D,H)
                gan="%.1f" % gan
                pi=rc_pi(D,H)
                pi="%.1f" % pi
                zhi=rc_zhi(D)
                zhi="%.1f" % zhi
                ye=rc_ye(D)
                ye="%.1f" % ye
                gen=rc_gen(D)
                gen="%.1f" % gen
                text.insert(tk.END,"\n ----------------------------------\n")
                text.insert(tk.END,"\nQuercus aliena\n","tag")
                gan=float(gan)
                gan_tan="%.1f" % (gan*0.4679)
                pi=float(pi)
                pi_tan="%.1f" % (pi*0.4791)
                zhi=float(zhi)
                zhi_tan="%.1f" % (zhi*0.4661)
                ye=float(ye)
                ye_tan="%.1f" % (ye*0.4328)
                gen=float(gen)
                gen_tan="%.1f" % (gen*0.4857)
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n Simulation --Biomass","tag")
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n biomass of stem {} t/ha".format(gan),"tag")
            text.insert(tk.END,"\n biomass of bark {} t/ha".format(pi),"tag")
            text.insert(tk.END,"\n biomass of branch {} t/ha".format(zhi),"tag")
            text.insert(tk.END,"\n biomass of foliage {} t/ha".format(ye),"tag")
            text.insert(tk.END,"\n biomass of root {} t/ha".format(gen),"tag")
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n Simulation --Carbon","tag")
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n Carbon of stem {} t/ha".format(gan_tan),"tag")
            text.insert(tk.END,"\n Carbon of bark {} t/ha".format(pi_tan),"tag")
            text.insert(tk.END,"\n Carbon of branch {} t/ha".format(zhi_tan),"tag")
            text.insert(tk.END,"\n Carbon of foliage {} t/ha".format(ye_tan),"tag")
            text.insert(tk.END,"\n Carbon of root {} t/ha".format(gen_tan),"tag")     
            text.insert(tk.END,"\n ----------------------------------\n")   
        command_biomass=tk.Button(root,text="Biomass and carbon",height=2,width=20,command=biomass_table)
        command_biomass.place(x=600,y=20)
    menubar4.add_command(label="Growth and Yield",command=gay_command)
    def it_command():
        it=tk.Tk()
        it.title("individual tree")
        it.geometry("450x300+500+200")
        l11=tk.Label(it,text="basal area in larger trees")
        l11.place(x=50,y=20)
        l22=tk.Label(it,text=" stand total basal area")
        l22.place(x=50,y=50)
        l33=tk.Label(it,text="individual tree diameter at breast height")
        l33.place(x=50,y=80)
        l44=tk.Label(it,text="site fertility class")
        l44.place(x=50,y=110)
        entry11=tk.Entry(it)
        entry11.insert(0, '40')
        entry11.place(x=250,y=20)
        entry22=tk.Entry(it)
        entry22.insert(0, '2000')
        entry22.place(x=250,y=50)
        entry33=tk.Entry(it)
        entry33.insert(0, '20')
        entry33.place(x=250,y=80)
        entry44=tk.Entry(it)
        entry44.insert(0, '4')
        entry44.place(x=250,y=110)
        def ok3_command():
            global GD
            global G
            global d
            global h30
            GD=int(entry11.get())
            G=float(entry22.get())
            d=float(entry33.get())
            h30=float(entry44.get())
            i=ii(GD,G,d,h30)
            i=float("%.2f" % i)
            p=pp(d,GD)
            p=float("%.4f" % p)
            H=Hh(h30,d)
            H=float("%.2f" % H)
            text.insert(tk.END,"\n ----------------------------------\n")
            text.insert(tk.END,"\n5-year diameter increment:{}".format(i),"tag")
            text.insert(tk.END,"\nprobability to survive for the coming 5 years:{}".format(p),"tag")
            text.insert(tk.END,"\nindividual tree height: {}".format(H),"tag")
            text.insert(tk.END,"\n ----------------------------------\n")
            it.destroy()
        def concel3_command():
            it.destroy()
        ok3=tk.Button(it,text="OK",height=2,width=10,command=ok3_command)
        ok3.place(x=50,y=220)
        concel3=tk.Button(it,text="Concel",height=2,width=10,command=concel3_command)
        concel3.place(x=200,y=220)
    menubar4.add_command(label="individual tree",command=it_command)

    menubar.add_cascade(label="simualation",menu=menubar4)
    def about_command():
     tk.messagebox.showinfo('about','BY GMH ')
    menubar.add_command(label="about",command=about_command)
    def help_command():
        help=tk.Tk()
        help.title("Help")
        help.geometry("800x400+500+200")
        text_help=tk.Text(help,height=800,width=300,state="normal")
        text_help.pack()
        text_help.insert(tk.END,"\nQUSSI is a stand simulator, which can predict stand factors of certain tree species under certain site conditions. The specific structure is as follows\n")
        text_help.insert(tk.END,"\n<file>-----")
        text_help.insert(tk.END,"\n            <save>----You can save the displayed text to your computer")
        text_help.insert(tk.END,"\n            <open>----You can open the text stored on the computer to the interface")  
        text_help.insert(tk.END,"\n            <exit>----Exit the software")
        text_help.insert(tk.END,"\n<setting>--")
        text_help.insert(tk.END,"\n            <tree speices>----Choose the tree species you want to simulate")
        text_help.insert(tk.END,"\n            <stand condition>--Choose the stand condition you want to simulate")
        text_help.insert(tk.END,"\n            <finance>")
        text_help.insert(tk.END,"\n<table>----")   
        text_help.insert(tk.END,"\n            <normal stand yield table>-----Output the normal stand growth table of selected tree species")
        text_help.insert(tk.END,"\n            <site index table>-------------Output the site index table of selected tree species")
        text_help.insert(tk.END,"\n            <standard volume table>--------Output the binary volume table of the selected tree species")
        text_help.insert(tk.END,"\n<simualation>")
        text_help.insert(tk.END,"\n            <Growth and yield>-------------Simulate the growth and volume of the selected tree species under the site conditions")
        text_help.insert(tk.END,"\n<about>-----about this software")
    menubar.add_command(label="help",command=help_command)
    def clear_command():
        text.delete(0.0, 'end')
    menubar.add_command(label="clear",command=clear_command)
    root.config(menu=menubar)
    root.mainloop()
var = tk.StringVar()
language1=tk.Radiobutton(root_lan,text="简体中文",var=var,value="简体中文",command=language_selection1,indicatoron=False,height=3,width=10)
language1.place(x=100,y=50)
language2=tk.Radiobutton(root_lan,text="English",var=var,value="English",command=language_selection2,indicatoron=False,height=3,width=10)
language2.place(x=100,y=130)
root_lan.mainloop()
