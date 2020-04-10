运行方法：<br>
首先安装python和scrapy，可以用pycharm直接打开文件夹<br>

编写爬虫的方法:<br>
在spiders包下新建一个python文件，可以参考cells_net_spider的写法<br>

scrapy的工作流程大致如下：spider爬取网页信息，然后抽取网页的信息到item中，item在items.py中定义，
对于每一个item，由pipline来进行操作，比如对数据进行持久化等。目前还没有编写过pippline的代码。

怎么调试编写的爬虫代码？<br>
在main.py中，把execute(['scrapy', 'crawl', 'name'])中的name参数改为爬虫名称即可<br>

其余scrapy的用法百度即可