# 使用

## 需要安装的模块

```python
pip install -i requirements.txt
```


## 数据库的设置
> 修改 k8sstudy/settings.py 文件
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'k8sstudy',  # 数据库名，先前创建的
        'USER': 'k8sstudyuser',     # 用户名，可以自己创建用户
        'PASSWORD': 'ihbl3qt123',  # 密码
        'HOST': '192.168.153.120',  # mysql服务所在的主机ip
        'PORT': '3306',         # mysql服务端口
    }
}
```

