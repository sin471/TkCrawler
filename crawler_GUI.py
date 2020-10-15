from tkinter import *
from tkinter import ttk
from icrawler.builtin import BingImageCrawler
import string

def crawling():
    crawler = BingImageCrawler(storage={"root_dir": folder.get()})
    crawler.crawl(keyword=word.get(), max_num=num.translate(table))

#型の変換
folder = StringVar()
word = StringVar()
num = IntVar()

#数字の全半角変換
table=str.maketrans("０１２３４５６７８９",string.digits)
num

root = Tk()
root.title('画像収集')

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=14)

label1 = ttk.Label(frame1, text='自動でフォルダを新規作成し、そこに画像を保存します')
label2 = ttk.Label(frame1, text='フォルダ名')
entry1 = ttk.Entry(frame1, textvariable=folder)

label3 = ttk.Label(frame1, text='検索語句')
entry2 = ttk.Entry(frame1, textvariable=word)
# todo:全角数字変換
label4 = ttk.Label(frame1, text='収集枚数')
entry3 = ttk.Entry(frame1, textvariable=num)

# todo:スピンボタンの追加
button1 = ttk.Button(
    frame1,
    text='実行',
    command=crawling)
# todo:配置方法の変更
pac = [label1, label2, entry1, label3, entry2, label4, entry3, button1]
# レイアウト
frame1.pack()
for a in pac:
    a.pack(anchor=NW)

# ウィンドウの表示開始
root.mainloop()
