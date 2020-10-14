from tkinter import *
from tkinter import ttk
from icrawler.builtin import BingImageCrawler


def crawling():
    crawler = BingImageCrawler(storage={"root_dir": folder.get()})
    crawler.crawl(keyword=word.get(), max_num=num.get())


root = Tk()
root.title('crawler_GUI')

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=14)

folder = StringVar()
word = StringVar()
num = IntVar()

label1 = ttk.Label(frame1, text='Folder name')
entry1 = ttk.Entry(frame1, textvariable=folder)

label2 = ttk.Label(frame1, text='Search words')
entry2 = ttk.Entry(frame1, textvariable=word)

label3 = ttk.Label(frame1, text='num')
entry3 = ttk.Entry(frame1, textvariable=num)


button1 = ttk.Button(
    frame1,
    text='Run',
    command=crawling)

pac = [label1, entry1, label2, entry2, label3, entry3, button1]
# レイアウト
frame1.pack()
for a in pac:
    a.pack(anchor=NW)

# ウィンドウの表示開始
root.mainloop()
