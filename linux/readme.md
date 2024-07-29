
## 准备hosts文件更新代码
即把 `update_host_for_normalGit_linux.py`放到本地特定目录。  
如放到home下， 该python代码路径： ~/update_host_for_normalGit_linux.py  


## 准备运行python代码的shell脚本
即把shell脚本`github.sh`放到本地特定目录
如放到home下， 该脚本路径： ~/github.sh  
设置脚本的可执行权限： `sudo chmod  +x  ~/github.sh`  


## 设置开机自启动

### 编写自启服务
```
cd /etc/systemd/system
sudo vim autoupdate_githudns.service

在打开文件中写入以下内容：

[Unit]
Description=svc-test
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=xl
ExecStart=/bin/bash ~/github.sh
killMode=control-group

[Install]
WantedBy=multi-user.target

## 注意：`User=xl`，即当前使用的用户名，根据自己系统修改
```


### 重载系统服务  
`sudo systemctl daemon-reload`

### 将服务注册为开机启动  

`sudo systemctl enable autoupdate_githudns.service`

### 测试自启动服务

1. 重启：`sudo systemctl restart autoupdate_githudns.service`
2. 状态：`sudo systemctl status autoupdate_githudns.service`


## 注意

1. 如果更换了脚本内容，需要重启服务: `sudo systemctl restart autoupdate_githudns.service`
2. 如果更改了`autoupdate_githudns.service`的内容，需要重载+重启服务：
   `sudo systemctl daemon-reload`
   `sudo systemctl enable autoupdate_githudns.service`
   `sudo systemctl restart autoupdate_githudns.service`
