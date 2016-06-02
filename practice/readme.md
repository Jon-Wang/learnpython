![python](http://s7.51cto.com/wyfs02/M01/24/2F/wKiom1NMlT-z_hrsAAA1lJYopPE323.gif)
#python爬虫操作实战

在python基础知识学习的基础上，进行的一些操作实战，在实战中加深python基础内容的理解，并学习新的知识。

python版本：2.7.11

    糗事百科程序：

1. [qsbk_01.py](https://github.com/Jon-Wang/learnpython/blob/master/practice/qsbk_01.py)爬取糗事百科的8小时最新页的段子。
2. [qsbk_02.py](https://github.com/Jon-Wang/learnpython/blob/master/practice/qsbk_02.py)是在[qsbk_01.py](https://github.com/Jon-Wang/learnpython/blob/master/practice/qsbk_01.py)的基础上，引入类和方法，进行优化和封装，爬取糗事百科的24小时热门页的段子。
3. [qsbk_10.py](https://github.com/Jon-Wang/learnpython/blob/master/practice/qsbk_10.py)进一步优化，每按一次回车更新一条内容，当前页的内容抓取完毕后，自动抓取下一页，按‘q’退出。

    百度贴吧程序：
1. [batb_01.py](https://github.com/Jon-Wang/learnpython/blob/master/practice/bdtb_01.py)爬取百度贴吧[帖子](http://tieba.baidu.com/p/3138733512)中的内容(只爬取楼主)。
2. [batb_10.py](https://github.com/Jon-Wang/learnpython/blob/master/practice/bdtb_10.py)将爬取的帖子内容保存到文件中，文件以帖子的标题命名，只要输入帖子的链接，可以爬取任意一个帖子。