from tkinter import *
from tkinter import ttk
from tkinter import filedialog as dia
import tkinter.messagebox as tkmsg
from icrawler.builtin import BingImageCrawler
from tkinter import filedialog


def crawling():
    crawler = BingImageCrawler(storage={"root_dir": path.get()})
    crawler.crawl(keyword=word.get(), max_num=num.get())
    tkmsg.showinfo("", "完了しました")

# フォルダー参照


def folder_select():
    idir = 'C:\\'
    folder_path = dia.askdirectory(initialdir=idir)
    entry_path.delete(0, END)
    entry_path.insert(0, folder_path)  # パスの表示
    #make_folder = folder_path+"\\"+str(folder.get)


root = Tk()
root.title('TkCrawler')

#folder = StringVar()
word = StringVar()
num = IntVar()
path = StringVar()

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=14)

style = ttk.Style()
style.configure(".", font=("メイリオ", 10))


label_word = ttk.Label(frame1, text='検索語句')
entry_word = ttk.Entry(frame1, textvariable=word, width=22, font=("メイリオ", 10))


label_num = ttk.Label(frame1, text='収集枚数(半角数字)')

spin_num = ttk.Spinbox(
    frame1,
    format='%1.0f',
    textvariable=num,
    from_=0,
    to=1000,
    width=20,
    font=("メイリオ", 10))

"""label_foldername = ttk.Label(frame1, text='フォルダ名')
entry_foldername = ttk.Entry(
    frame1, textvariable=folder, width=22, font=("メイリオ", 10))"""


# todo:word folder_select 変数
label_path = ttk.Label(frame1, text='フォルダの保存先')
entry_path = ttk.Entry(frame1, width=14, font=("メイリオ", 10), textvariable=path)
button_path = ttk.Button(frame1, text="参照", width=6, command=folder_select)
run_button = ttk.Button(
    frame1,
    text='実行',
    command=crawling,
    width=18)

widget = [frame1, label_word, entry_word,
          label_num, spin_num, label_path]

# レイアウト
for a in widget:
    a.grid(row=widget.index(a), columnspan=3)

entry_path.grid(columnspan=3, row=8, sticky=W)
button_path.grid(column=2, row=8, sticky=E)

run_button.grid(columnspan=3, row=9)

# ウィンドウの表示開始
root.mainloop()
