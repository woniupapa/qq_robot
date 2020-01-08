# 一个基于nonebot的爬取星期一的丰满漫画的qq机器人

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
`cp bot/config.example.py bot/config.py`  
`cp bot/plugins/tawawa/catach_tawawa/config.exmaple.py bot/plugins/tawawa/catach_tawawa/config.py`  

2. 修改 `docker-compose.yml` 内容， 主要修改下列参数  
`VNC_PASSWD` 在登录VNC时用的密码  
`COOLQ_ACCOUNT` 要登录的qq号  

3. 修改 `bot/config.py` 中的配置，主要是 `SUPERUSERS`，在集合中填写qq号，数字类型  

4. 修改 `bot/plugins/tawawa/catach_tawawa/config.py` 主要修改 email info 注释下的三个选项  


**启动**  
在项目目录下执行 `docker-compose up -d`  
访问你的 `ip:9000` （如果是本地就是 `127.0.0.1:9000`）按操作填写密码，登录qq   
登录qq后，在项目目录中找到文件 `coolq/app/io.github.richardchien.coolqhttpapi/config/[你登录的qq号].ini` (有可能是json)，并追加如下内容  
```
[你登录的qq号]
ws_reverse_api_url = ws://host.docker.internal:8080/ws/api/  
ws_reverse_event_url = ws://host.docker.internal:8080/ws/event/  
use_ws_reverse = true
```
ws地址，根据不同的机器，ip是不同的，centos等可能是172.17.0.1
如果是json格式，则按照json的规范填写上述内容  
重启httpAPI插件（在浏览器访问的窗口中，右击浮悬窗>应用>HTTP API>重启应用）

在项目目录下 `python main.py`(根据你的python3安装方法，等等，可能是`python3 main.py`)，出现如下提示则是成功了  
```
[2020-01-05 12:03:17,113] xxx.xxx.xxx.xxx:xxxx GET /ws/api/ 1.1 101 - 986
[2020-01-05 12:03:17,145] xxx.xxx.xxx.xxx:xxxx GET /ws/event/ 1.1 101 - 551
```

