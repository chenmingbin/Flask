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

## URL与视图

### 1.URL与函数的映射

 