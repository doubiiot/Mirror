# Mirror
## With MagicMirror, use pyqt to write a similar interface.

    项目地址：https://github.com/MichMich/MagicMirror 

原项目是用JavaScript写的，我对这个了解得不多，刚学了python然后有一点Qt的基础，然后就用了pyqt来写这个。<br>
代码界面是按照显示屏尺寸800*480写的，是微雪7寸的显示屏。<br>

运行：
在树莓派上安装好python3以及pyqt环境之后运行：<br>
```
sudo python3 mainwindow.py
```

### mainProject 文件夹是主要代码区，包括了各个日期、时间、天气以及句子模块。
* 顶部的日期模块有一点小问题，代码可能比较累赘，因为天气的一个API里获取了一些日期的数据，应该有更简单的办法来获取。<br>

* 天气接口一开始在阿里云找了一个接口，其实上面数据蛮全的，但是由于当时没有认真研究返回的json就换了和风天气的接口。<br>

* 句子模块是从服务器端数据库定时读取数据显示在屏幕上。

### server文件中包含了远程向服务器添加自定义语句以及服务器端接收的代码。

服务器端运行: <br>
```
sudo python3 server.py
```
然后通过运行input文件远程向服务器数据库中存取数据

* 另外，因为自己用的是七寸的显示屏，屏幕显示的内容有限暂时弄了这个界面，弄界面蛮麻烦的，后期考虑封装一下，更好的对界面以及内容进行增添和修改。

#### 各位大佬如果有什么想法或者意见，请指教一下。
#### 博客地址：https://doubiiot.cn 
