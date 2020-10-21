from tkinter import *
from tkinter import ttk
from tkinter import filedialog as dia
import tkinter.messagebox as tkmsg
from icrawler.builtin import BingImageCrawler
from tkinter import filedialog
import subprocess


# クロール
def crawling():
    crawler = BingImageCrawler(storage={"root_dir": path.get()})
    crawler.crawl(keyword=word.get(), max_num=num.get())
    open_folder()
    #tkmsg.showinfo("", "完了しました")


# フォルダー参照
def folder_select():
    idir = 'C:\\'
    folder_path = dia.askdirectory(initialdir=idir)
    entry_path.delete(0, END)
    entry_path.insert(0, folder_path)  # パスの表示


def open_folder():
    path2 = path.get().replace('/', '\\')
    subprocess.Popen(["explorer", path2])


# ウィンドウの作成
root = Tk()
root.title('TkCrawler')

# 型を定義
word = StringVar()
num = IntVar()
path = StringVar()


style = ttk.Style()
style.configure(".", font=("メイリオ", 10))

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=14)
frame1.grid(row=1, columnspan=3)


label_word = ttk.Label(frame1, text='検索語句')
label_word.grid(row=2, columnspan=3)

entry_word = ttk.Entry(frame1, textvariable=word, width=22, font=("メイリオ", 10))
entry_word.grid(row=3, columnspan=3)


label_num = ttk.Label(frame1, text='収集枚数(半角数字)')
label_num.grid(row=4, columnspan=3)

spin_num = ttk.Spinbox(frame1, format='%1.0f', textvariable=num,
                       from_=0, to=1000, width=20, font=("メイリオ", 10))
spin_num.grid(row=5, columnspan=3)


label_path = ttk.Label(frame1, text='フォルダの保存先')
label_path.grid(row=6, columnspan=3)

entry_path = ttk.Entry(frame1, width=14, font=("メイリオ", 10), textvariable=path)
entry_path.grid(columnspan=3, row=8, sticky=W)

button_path = ttk.Button(frame1, text="参照", width=6, command=folder_select)
button_path.grid(column=2, row=8, sticky=E)


run_button = ttk.Button(frame1, text='実行', command=crawling, width=18)
run_button.grid(row=9, columnspan=3)

# ウィンドウの表示開始
root.mainloop()
