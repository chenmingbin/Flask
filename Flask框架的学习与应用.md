# Flask框架的学习与应用

**安装Flask：PIP install Flask**

```python
@app.route('/')
def hello_world():
return 'hello,world'
if __name__ == '__main__'
app.run()
```

> @app.route('/')
>
> 声明一个路由，URL路径为根，与下面的def方法进行一个绑定
>
> def hello_world():
>
> 声明一个方法名为：hello_world
>
> return 'hello,world'
>
> 返回字符串hello,world
>
> if __name__ == '__main__'
> app.run()
>
> main函数，运行用。

**默认IP地址为http://127.0.0.1:5000**

 

## 1.项目配置：

**开启Debug：**

```python
app.run(debug=True)
```

**配置文件**

```python
app = Flask（__name__）
app.config['JSON_AS_ACSII'] = Ture
```

> 如果配置项过多的话可以添加一个config.py文件进行储存。

> 正常工作中都是需要创建一个config.py文件来存放所有的配置。好处就是代码比较简洁并美观。

> 注：flask的配置项目都是大写字母

```python
#config.py文件中添加
JSON_AS_ACSII = Ture
.....
#然后在运行文件中导入该方法
import config
app = Flask(__name__)
app.config.from_object(config)
```

## 2.URL与视图：

### 1.URL与视图函数的映射

 @app.route中声明\<类型:变量名>然后在def中传入该变量名完成映射

```python
@app.route('/<int:book>')
def book_path(book)
```

> <>尖括号是固定写法
>
> 可用类型有：
>
> int：整型
>
> float：浮点型
>
> path：和string类似，但是可以传递斜杠" / "
>
> string：字符串类型
>
> uuid：uuid类型的字符串
>
> any：可用指定多种路径，

> 这种映射方法可以用在数据库连接、excel或字典、列表、元组等

> 这里引出一个测试点：在进行接口测试时需要注意类型的传递，可能会因为类型不同的情况出现BUG

### 2.构造URL

