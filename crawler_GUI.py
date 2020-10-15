from tkinter import *
from tkinter import ttk
from icrawler.builtin import BingImageCrawler

def crawling():
    crawler = BingImageCrawler(storage={"root_dir": folder.get()})
    crawler.crawl(keyword=word.get(), max_num=num.get())

root = Tk()
root.title('画像収集')

folder = StringVar()
word = StringVar()
num = IntVar()

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=14)

label1 = ttk.Label(frame1, text='自動でフォルダを作成し\nそこに画像を保存します')
label2 = ttk.Label(frame1, text='フォルダ名')
entry1 = ttk.Entry(frame1, textvariable=folder)

label3 = ttk.Label(frame1, text='検索語句')
entry2 = ttk.Entry(frame1, textvariable=word)

label4 = ttk.Label(frame1, text='収集枚数(半角数字)')
entry3 = ttk.Entry(frame1, textvariable=num)

# todo:スピンボタンの追加
button1 = ttk.Button(
    frame1,
    text='実行',
    command=crawling)

widget = [frame1,label1, label2, entry1, label3, entry2, label4, entry3, button1]
#todo:終了時にポップアップ
#レイアウト
for a in widget:
    a.grid(row=widget.index(a))

# ウィンドウの表示開始
root.mainloop()
