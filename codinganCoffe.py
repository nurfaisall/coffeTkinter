from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Rekapitulasi Data Penjualan Kopi Harian")
root.geometry("200x300")

harga_kopi = {"luwak":20000,
"lampung":40000,
"robusta":30000,
"gayo":45000,
"arabica":55000}

jumlahtotal=[]
def penjualankopi(*args):

    c=b.get()
    jumlahtotal.append(c)
    x=a.get()
    if x==1:
        print("kopi Luwak")
        print("harganya adalh",harga_kopi["luwak"])
    if x==2:
        print("Kopi Lampung")
        print("harganya adalh",harga_kopi["lampung"])
    if x==3:
        print("kopi Robusta ")
        print("harganya adlh",harga_kopi["robusta"])
    elif x==4:
        print("kopi Gayo")
        print("harganya adlh",harga_kopi["gayo"])
    elif x==5:
        print("kopi Arabica")
        print("harganya adlh",harga_kopi["arabica"])
    return

def rekap():
    print("Rekapitulasi Pesanan")
    d=sum(jumlahtotal)
    print("sales terakhir menginput data :", d, "joni")

Label(root, text= "GUI Input Data Penjualan Kopi Harian").place(x=150,y=20)

a= IntVar()
def tombol(value):
    teks = Label(root,text= value).pack()

a=IntVar()
Radiobutton(root,text ="kopi Luwak",variable = a , value = 1).place(x=30,y=70)
Radiobutton(root,text="kopi Lampung",variable = a, value = 2).place(x=30,y=105)
Radiobutton(root,text= "Kopi Robusta", variable = a, value = 3 ).place(x=30,y=140)
Radiobutton(root,text= "kopi Gayo", variable = a, value = 4 ).place(x=30,y=175)
Radiobutton(root,text = "kopi Arabica", variable = a, value = 5 ).place(x=30,y=210)


b=IntVar()
c1=Checkbutton(root,text='Roast',variable=b,onvalue=1,offvalue=0)
c1.pack()
c2=Checkbutton(root, text='Grind', variable=b,onvalue=2,offvalue=0)
c2.pack()

# edit
feet = StringVar()
feet_entry = ttk.Entry(root, width=7, textvariable=feet)
feet_entry.place()

meters = StringVar()
ttk.Label(root, textvariable=meters).place(x=1, y=1)


# label
Label(root, text=  "RP 20.0000,00").place(x=150,y=70)
Label(root, text= "RP 40.000,00").place(x=150,y=105)
Label(root, text= "RP 30.000,00").place(x=150,y=140)
Label(root, text= "RP 45.000,00").place(x=150,y=175)
Label(root, text= "RP 55.000,00").place(x=150,y=210)
b=IntVar()
jumlah=Entry(root, width=50, textvariable=b, fg='black').place(x=420,y=300)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Rekapitulasi Data Penjualan Kopi Harian", command=rekap)


Button(root,text="Input Data", command=penjualankopi).place(x=320,y=200)



root.config(menu=menubar)

root.bind("<Return>", penjualankopi())
root.mainloop()