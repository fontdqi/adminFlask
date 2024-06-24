# Flask框架入门
## 简介：
Flask是一个非常小的PythonWeb框架，被称为微型框架；只提供了一个稳健的核心，其他功能全部是通过扩展实现的；意思就是我们可以根据项目的需要量身定制，也意味着我们需要学习各种扩展库的使用。
## 特点：
Django虽然功能比较多，但是相对笨重，开发时间成本远大于Flask。

## 前期准备工作
### 一、安装虚拟环境前的准备：
> Windows操作系统，Visual Studio Code编写代码。 

我使用的`Python`是python3.XX版本。`python2`的版本就是不是这样的子的安装方式，它 无法使用`venv` 模块，必须安装 `virtualenv`才能使用。这里我就不多说`python2`太多，如果是想用`python2`运行`Flask`，请参考一下[官方文档](https://flask.github.net.cn/installation.html#id4)。
#### 步骤一：
创建一个项目文件夹（不推荐在C盘默认盘创建）->，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 `venv` 文件夹。
```js
mkdir myproject
cd myproject
py -3 -m venv venv
```

#### 步骤二：


激活虚拟环境，前面步骤我们已经进入`myproject`文件夹中,激活虚拟环境变量
```js
venv\Scripts\activate
```
出现带（venv）则激活成功，

![屏幕截图 2024-06-24 092019.png](https://img.cdn.apipost.cn/upload/user/191631738001571840/log/58665cbb-15a8-430c-b640-a2460a19987e.png "屏幕截图 2024-06-24 092019.png")
#### 步骤三：
安装 `Flask` ，在已激活的虚拟环境中可以使用进行命令安装 ：
```js
pip install Flask
```
## 创建一个简单的小应用
#### 步骤一：
进入 `myproject`文件夹中，我们在根目录下下创建个`app.py`
```js
#导入模块
from flask import Flask
#Flask(__name__)中的__name__参数是当前模块的名称，用于区分不同的Flask应用。这个函数是Flask框架的入口，通过这个函数可以定义路由、处理请求和返回响应等。

app = Flask(__name__)
#路由
@app.route('/')
#定义函数名为 hello_world ，你也可以改成其他，例如index、home...等这里不固定，也可以hello_world('/user/<username>')的括号里面传参数,以后会说到
def hello_world():
#返回值：字符串类型 的 Hello, World!
    return 'Hello, World!'
```
#### 步骤二：
需要在终端里导出 `FLASK_APP` 环境变量:一般默认变量名是`app.py`以防出现运行问题，我们就多个步骤配置一下，运行`Flask`命令：
```js
set FLASK_APP=app.py
flask run
```
:::highlight yellow 💡
tips：因为之前已经创建虚拟环境，也安装了Flask，那么运行的环境选择也要是在虚拟环境下运行，要不然我们之前安装的虚拟环境就没什么意义。
:::
在 `Visual Studio Code`的右下角确认运行Python是否为虚拟环境。

![屏幕截图 2024-06-24 100404.png](https://img.cdn.apipost.cn/upload/user/191631738001571840/log/9ef7525a-d8e4-40cf-a3cd-0863e31059a6.png "屏幕截图 2024-06-24 100404.png")
出现venv则说明成功。如果使用`PyCharm`编写则需要设置解释器。

运行成功结果：

![屏幕截图 2024-06-24 101022.png](https://img.cdn.apipost.cn/upload/user/191631738001571840/log/00f72e31-5078-4074-9689-ffbb52432b3c.png "屏幕截图 2024-06-24 101022.png")





:::tip
这样是运行成功了，但是会出现个问题，你每次在app.py修改的代码，例如：` return 'Hello, World!'`，你改为了`return 'Hello'`。你点击浏览器访问你修改结果返回值还是`Hello, World!`。你需要`ctrl+c`退出运行`flask run`页面访问结果值才会是`Hello`，它不会自动加载结果，会大大降低开发进度。

如果自己的Flask 版本是 2.3 或更高版本可以直接使用命令开启`调试模式`进行自动重载
```js
flask run --debug
```
:::

![屏幕截图 2024-06-24 102824.png](https://img.cdn.apipost.cn/upload/user/191631738001571840/log/5c744df9-ba4b-49ee-a158-fe95c9f872e6.png "屏幕截图 2024-06-24 102824.png")









