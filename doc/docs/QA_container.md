## 如何开启jupyter?
* 安装jupyter
```
# 先升级一下ipython
$ pip install ipython --upgrade

# 安装jupyter
$ pip install jupyter notebook
```

### 配置远程访问jupyter

* 生成密码
```
$ ipython
```
* 在python命令行里分别输入：
```
$ from notebook.auth import passwd
$ passwd()
```
* 输完之后，设定一个密码，会生成一个sha1的秘钥会有如下的结果：
![](img/jupyter.png)
* 记录生成的sha1秘钥，然后退出
```
quit()
```
* 生成jupyter notebook的配置文件
```
$ jupyter notebook --generate-config
$ vim ~/.jupyter/jupyter_notebook_config.py

##  加入如下内容
c.NotebookApp.ip='*'
c.NotebookApp.password = u'sha1:41e4da01dde4:e820dc9c0398eda2dc9323c9e4a51ea1228166a2' ## 将生成的sha1密钥填写在这里。
c.NotebookApp.open_browser = False
```
* 进入计算节点(node xx)，开启反向代理:

由于我们无法在本地直接访问计算节点(node xx)，所以我们需要先进入计算节点添加反向代理。

```
$ ssh nodexx # 进入计算节点
# 注意端口需要用到分配的ADMIN_PORT 3xxxx - 3xxxx中的其中一个, 下面以30339为例
$ ssh -CNfR 30339:0.0.0.0:30339 admin
```

* 在开启反向代理的那个节点(node xx)开启jupyter:
```
$ jupyter notebook --allow-root --ip=0.0.0.0 --port=30339
```

* 最后我们可以在浏览器中通过访问  **10.19.124.11:30339**, 进入jupyter

## 如何开启visdom?
*  下载visdom
```
$ pip install visdom
```
* 打开visdom   
第一次打开visdom会比较慢，因为visdom需要自己下载一些脚本.
```
# 注意端口需要用到分配的ADMIN_PORT 3xxxx - 3xxxx中的其中一个, 下面以30330为例
$ python -m visdom.server -p 30330 ##
```

* 如何在程序中使用visdom，请移步[visdom github](https://github.com/facebookresearch/visdom)主页， 里面有详细的教程。
