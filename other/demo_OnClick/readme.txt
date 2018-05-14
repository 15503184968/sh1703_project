# -*- encoding: utf-8 -*-

浏览器点击链接后，发生的事情：
1. 浏览器解析页面的链接
    1) 页面内部的链接
    2) 页面外部的链接url
        (1) 域名
        (2) ip地址
    3) 发http请求
        (1) http包格式
            参见：
                image/http包格式.jpeg
            请求体：
                post, put, patch, ...
    4) nginx
    5) gunicorn
    6) django
    7) django的视图函数处理请求
    8) django把HttpResponse转换成http数据包
    9) http数据包, 返回浏览器




2. 域名解析
    /etc/hosts
    DNS
    ARP
        ip addr <----> 网卡addr

3. TCP/IP详解 卷1：协议
    http://www.52im.net/topic-tcpipvol1.html

