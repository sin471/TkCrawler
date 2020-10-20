from icrawler.builtin import BingImageCrawler

folder=input("Foldername>>>")
word=input("Keyword>>>")
num=input("Num>>>")
path=input("Folder Path>>>")

dest=path+"\\"+folder

crawler = BingImageCrawler(storage={"root_dir": dest})
crawler.crawl(keyword=word ,max_num=int(num))