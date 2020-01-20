# 基于 coolq 和 nonebot 的机器人

## 包含复读，发送最新的月曜日のたわわ漫画等功能

## 准备
- 需要有docker环境，并且安装docker-compose工具
- 需要有python3.6+的环境
- 最好可以安装 virtualenv 并创建一个python3的虚拟环境，以免产生包冲突

## 安装

**克隆代码到本地**  
`git clone https://github.com/alive1944/tawawa_crawler.git`  


**运行包安装**  
`pip install -r requirements.txt`，有可能是 `pip3` 命令，根据你python3和对应pip的安装过程决定


## 运行 
**配置**  
1. 将下列文件的 `.example` 文件copy一份出来，并去掉 `.example` 部分  
`cp docker-compose.example.yml docker-compose.yml`  
`cp bot/config/bot_config.example.py bot/config/bot_config.py`  

2. 修改 `docker-compose.yml` 内容， 主要修改`environment`下的参数  
```
VNC_PASSWD=password # 登录CNV系统时的密码
COOLQ_ACCOUNT=123456789 # 要登录的qq账号，会在登录qq时自动填写进qq号一栏
CQHTTP_WS_REVERSE_API_URL=ws://host.docker.internal:8080/ws/api/ # ws api地址，macos下地址用host.docker.internal，其他系统大概率是172.17.0.1
CQHTTP_WS_REVERSE_EVENT_URL=ws://host.docker.internal:8080/ws/event/ # 地址设置同上
CQHTTP_USE_WS_REVERSE=true # 不用改他
COOLQ_URL=http://dlsec.cqp.me/cqa-tuling # 下载的酷Q版本，pro版本将 cqa-tuling 修改为 cqp-tuling
```

3. 修改 `bot/config/bot_config.py` 中的配置，主要是 `SUPERUSERS`，在集合中填写qq号，数字类型  


**启动**  
在项目目录下执行 `docker-compose up -d`  
访问你的 `ip:9000` （如果是本地就是 `127.0.0.1:9000`）按操作填写密码，登录qq   

在项目目录下 `python main.py`(根据你的python3安装方法，等等，可能是`python3 main.py`)，出现如下格式的提示则表示成功了  
```
[2020-01-05 12:03:17,113] xxx.xxx.xxx.xxx:xxxx GET /ws/api/ 1.1 101 - 986
[2020-01-05 12:03:17,145] xxx.xxx.xxx.xxx:xxxx GET /ws/event/ 1.1 101 - 551  
```


## 插件


插件名 | 文件位置 | 备注 | 状态
---|---|---|---
复读机 | bot/plugins/repeat | | <span color="green">done</span>
比村乳业漫画 | bot/plugins/tawawa | | <span color="green">done</span>
P站爬图 | bot/plugins/pixiv | | <span color="red">create task</span>
定时任务 | bot/plugins/task | | <span color="red">create task</span>