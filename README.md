# 小米水滴平台（小米AI音箱）第三方技能接入

> 小米AI音箱所在的小米水滴平台允许接入自己的后端处理，本项目提供了一个使用Python编写的Demo，实现了authorization的验证，并重述刚刚听到的话。
小米AI音箱目前也有很多可以改进的地方，但它提供了第三方技能接入的功能，可以自己进行定制，例如，可以自己接入发邮件、发微信的功能、查询成绩、语音指令下载电影、控制更多品牌的智能插座等。

## 运行环境
Python 3.5.2+
Flask 0.12

## 本地启动
```
# 安装所需环境
pip3 install -r requirements.txt
# 启动
python runserver.py
```
访问下面的网址进行端口测试
```
http://localhost:12030/v1/ui
```

## 线上部署

记得修改config.py中的`MI_KEY_ID`，`MI_SECRET`。

> 线上部署需要有自己的云服务器、域名，小米的水滴平台要求接口是https的，因此还需要申请https的证书。

云服务器可使用国内的阿里云[链接](www.aliyun.com)、腾讯云[链接](cloud.tencent.com)，
国外的搬瓦工[链接](https://bandwagonhost.com/aff.php?aff=29201)、hostmybytes[链接](https://clients.hostmybytes.com/aff.php?aff=748&pid=178)、Digital Ocean[链接](https://m.do.co/c/73c1f5a60b4f)等。

域名注册的话，阿里云、腾讯云、godaddy等网站也很便宜，如果使用国内的云服务器的话，别忘了进行域名实名认证和备案。

Https证书使用的`Let's Encrypt`的免费证书，结合nginx部署起来也十分容易，具体看参见`https://certbot.eff.org/#ubuntuxenial-nginx`

我使用的是ubuntu 14.04，安装过程如下：
```angular2html
# 安装certbot
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx 
# 安装nginx
sudo apt-get install nginx
```
修改nginx的配置文件, 我的nginx的配置文件在`/etc/nginx/sites-enabled/default`，在server block内添加以下内容： 
```angular2html
location ~ /.well-known {
        allow all;
}
```

## 安装https证书
```
sudo certbot --authenticator webroot --installer nginx
# 其间需要输入自己的域名及web-root
# web-root是指网站的根目录，我的路径是/var/www/html
```
最终，我的nginx配置文件内容如`nginx_config/default`中所示。

这个证书每90天会过期一次，需要重新获取证书，这里我们可以把它加入计划任务。运行`crontab -e`, 添加以下内容
```angular2html
30 3 * * 1 /usr/bin/certbot renew --quiet --no-self-upgrade
35 3 * * 1 /etc/init.d/nginx reload
```

## 部署flask网站
可以先运行`python runserver.py`进行测试，之后使用gunicorn进行部署。
