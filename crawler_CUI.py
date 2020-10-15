from icrawler.builtin import BingImageCrawler

file=input("Filename>>>")
word=input("Keyword>>>")
num=input("Num>>>")
crawler = BingImageCrawler(storage={"root_dir": file})
crawler.crawl(keyword=word ,max_num=int(num))