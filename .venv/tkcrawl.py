from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkmsg
from icrawler.builtin import BingImageCrawler


def crawling():
    crawler = BingImageCrawler(storage={"root_dir": folder.get()})
    crawler.crawl(keyword=word.get(), max_num=num.get())
    tkmsg.showinfo("", "完了しました")


root = Tk()
root.title('TkCrawler')

folder = StringVar()
word = StringVar()
num = IntVar()

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=14)

font = ("メイリオ", 10)
style = ttk.Style()
style.configure(".", font=font)

label1 = ttk.Label(frame1, text='自動でフォルダを作成し\nそこに画像を保存します')
label2 = ttk.Label(frame1, text='フォルダ名')
entry1 = ttk.Entry(frame1, textvariable=folder, width=22, font=font)

label3 = ttk.Label(frame1, text='検索語句')
entry2 = ttk.Entry(frame1, textvariable=word, width=22, font=font)

label4 = ttk.Label(frame1, text='収集枚数(半角数字)')

spin1 = ttk.Spinbox(
    frame1,
    format='%1.0f',
    textvariable=num,
    from_=0,
    to=1000,
    width=20,
    font=font)

button1 = ttk.Button(
    frame1,
    text='実行',
    command=crawling)

widget = [frame1, label1, label2, entry1,
          label3, entry2, label4, spin1, button1]

# レイアウト
for a in widget:
    a.grid(row=widget.index(a))

# ウィンドウの表示開始
root.mainloop()
