# Share And Talk 博客网站

[![](https://starry-trace-sky-moe-counter.vercel.app/get/@share_and_talk?theme=rule34)](https://github.com/StarrySky-skyler/Share_And_Talk)

[English](./README.md) | 中文(简体)

![](https://img.shields.io/badge/后端开发-星痕Sky-blue)
![](https://img.shields.io/badge/前端开发-XuJiaqi999-purple)

![](https://img.shields.io/badge/许可证-MIT-red)
![](https://img.shields.io/badge/后端程序-Python-blue)
![](https://img.shields.io/badge/框架-Django-yellow)
![](https://img.shields.io/badge/最新版本v1.4.16brightgreen)

![网站主页](example.png)

# 1. 介绍😁

1. 多用户（用户头像目前只支持 qq 头像和 gravatar 头像）
2. 博客的发布，点赞，编辑，删除
3. 支持一级分类和二级分类标签
4. 支持文章 markdown 语法，高亮代码，Katex 科学公式，flowchart 流程图

# 环境

- win10x64 及以上
- Python 3.11.2
- Mysql 8.0.32
- Apache 2.4.46

# 2. 安装🍔

## 2.0 方式一: docker 安装(推荐)

> 请先安装好 docker

### 2.0.1 克隆项目至本地

```bash
git clone https://github.com/StarrySky-skyler/Share_And_Talk.git
```

### 2.0.2 运行

终端`cd`进入项目根目录, 输入以下命令启动

```bash
docker compose up -d
```

### 2.0.3 关闭

输入以下命令停止运行

```bash
docker compose stop
```

### 2.0.4 删除服务

输入以下命令删除容器

```bash
docker compose down
```

## 2.1 方式二：手动安装

### 2.1.1 克隆项目至本地

```bash
git clone https://github.com/StarrySky-skyler/Share_And_Talk.git
```

### 2.1.2 安装依赖

推荐先创建并进入**venv**或者其他虚拟环境

```bash
pip install wheel
pip install -r requirements.txt
```

### 2.1.3 配置数据库

先创建好网站需要的数据库, 使用`utf8mb4`编码

打开`ShareAndTalk/config.py`

```python
# Database settings
dbName = 'share_and_talk'
dbUser = 'root'
dbPassword = 'skyler'
# Email settings
EMAIL_USER = 'Your email'
EMAIL_PASSWORD = 'Your password'
DEFAULT_FROM = 'Your email'

```

需要配置的字段

- `dbName`: 数据库名
- `dbUser`: 数据库用户名
- `dbPassword`: 对应用户的密码

输入命令

```bash
py manage.py makemigrations
py manage.py migrate
```

导入示例数据库

```bash
py manage.py loaddata backup/example.json
```

注意:

示例数据库包含

1. 一个初始超级管理员, 账号是 root, 密码是 skyler

2. 一个帮助页面

3. 一些默认分类

### 2.1.4 配置语言与时区

默认语言: 简体中文

默认时区: 东八区

参见`ShareAndTalk/settings.py`

```python
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

详细配置参见：

[语言标识符列表🚅](http://www.i18nguy.com/unicode/language-identifiers.html)

[时区列表1 wikipedia🧪](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

[时区列表2🎈](https://www.zeitverschiebung.net/cn/all-time-zones.html)

若需修改为其他语言，还需删除`ShareAndTalk/settings.py`的以下代码

```python
# Default language
LANGUAGES = [
    ('zh-hans', '中文（简体）'),
]
```

### 2.1.5 配置邮箱(可选)

用于主页底部的**用户反馈**

打开`ShareAndTalk/config.py`

```python
# Database settings
dbName = 'share_and_talk'
dbUser = 'root'
dbPassword = 'skyler'
# Email settings
EMAIL_USER = 'Your email'
EMAIL_PASSWORD = 'Your password'
DEFAULT_FROM = 'Your email'

```

字段含义

- `EMAIL_USER`: 收件邮箱
- `EMAIL_PASSWORD`: 邮箱秘钥
- `DEFAULT_FROM`: 寄出邮箱地址

详细参考[ django 邮箱配置](https://docs.djangoproject.com/zh-hans/4.1/ref/settings/)

### 2.1.6 创建超级管理员

在本项目根目录下，打开`cmd`或者`powershell`或者其他终端，输入以下命令

```bash
py manage.py createsuperuser
```

根据提示进行创建即可

### 2.1.7 部署🌭

1. 打开`ShareAndTalk/settings.py`，将

```python
DEBUG = True
```

改为

```python
DEBUG = False
```

2. 打开`powershell`，进入到仓库根目录后，运行以下命令，将静态文件拷贝到`static`文件夹中

```bash
py manage.py collectstatic
```

> `static`文件夹在运行命令后会自动创建，若需更改文件夹位置，请修改`ShareAndTalk/settings.py`的以下代码

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
if not DEBUG:
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '/static/'), # Change your static folder here
    )
    STATIC_ROOT = os.path.join(BASE_DIR,'static') # Change your static folder here
```

3. 配置 apache2 , 参见[ Notion 笔记](https://www.notion.so/starrytracesky/windows-django-0ae4b2c1562f43fc81f24d755e77f8a5)

# 3. 补充💻

网站用户上传文件位置保存在`uploads`文件夹中，如需更改，请定位到`ShareAndTalk/settings.py`末尾的以下代码

```python
# mdeditor
X_FRAME_OPTIONS = 'SAMEORIGIN'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'
```

将`MEDIA_ROOT`修改为包含绝对路径的字符串即可

# 常用命令

1. 恢复表结构（进入mysql）

```
mysql> source backup/db_structure.sql;
```

2. 还原数据库数据

```bash
py manage.py loaddata backup/xxx.json
```

3. Django Shell

```bash
py manage.py shell
```

4. 备份json数据

```bash
py -Xutf8 manage.py dumpdata > db.json
```

# [MIT 许可证](https://github.com/StarrySky-skyler/Share_And_Talk/blob/main/LICENSE)
