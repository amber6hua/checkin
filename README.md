# checkin

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/amber6hua/checkin.git)

You can deploy without cloning this repo to test it out.

## 开发过程
- telegram 每日向机器人发送签到很麻烦
- 在github 上看到关于python的telethon登录并发送消息
- 通过定时器循环执行
- 由于telethon 需要登录验证，为了托管在heroku,利用quart作为web框架，请求接口，发送验证码登录
- 默认登录后生成.session的文件存储登录信息
- 但是heroku 的 web和clock进程 无法互通.session
- 通过AlchemySessionContainer,heroku的postgresql作为存储数据库
- 终于部署在heroku，结果发现无法发送验证码，也没有报错
- 最后通过执行auth.py在本地登录，把登录信息储存在heroku的postgresql
- 然后运行定时器 clock

## 说明
- 本来想利用quart框架web api 方式 登录telethon (不知道为什么heroku上无法发送获得验证码)
- 后来改用 heroku 的 run console, 进入bash 执行 auth.py 登录telethon
- 然后 进入Resources 分页启动 worker python auto_checkin.py 试试能否正常签到
- 最后启动 clock python clock.py 定时执行

## GG
Procfile文件
~~web: hypercorn app:app~~

## 踩坑
- telethon-session-sqlalchemy-fork 原作者的telethon-session-sqlalchemy有点问题，发现有个fork版的竟然可以用
- AlchemySessionContainer不太了解，第一次启动没问题 container = AlchemySessionContainer(DATABASE_URL)
- 第二次启动会报key重复，我这么修改的 container = AlchemySessionContainer(DATABASE_URL, manage_tables=False)