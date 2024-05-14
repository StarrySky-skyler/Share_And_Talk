# Share And Talk Blog Website

[![](https://starry-trace-sky-moe-counter.vercel.app/get/@share_and_talk?theme=rule34)](https://github.com/StarrySky-skyler/Share_And_Talk)

English | [中文(简体)](./README_zh_cn.md)

![](https://img.shields.io/badge/Backend_Developer-星痕Sky-blue)
![](https://img.shields.io/badge/Frontend_Developer-XuJiaqi999-purple)

![](https://img.shields.io/badge/License-MIT-red)
![](https://img.shields.io/badge/Program-Python-blue)
![](https://img.shields.io/badge/Framework-Django-yellow)
![](https://img.shields.io/badge/Latest_Version-v1.4.14_alpha-brightgreen)

![Website Homepage](example.png)

# 1. Introduction😁

1. Multi-user (currently only supports qq avatars and gravatar avatars)
2. Blog publishing, liking, editing, deleting
3. Support for primary and secondary classification tags
4. Support for article markdown syntax, code highlighting, Katex scientific formulas, and flowchart diagrams

# Environments

- win10x64 and above
- Python 3.11.2
- Mysql 8.0.32
- Apache 2.4.46

# 2. Installation🍔

## 2.1 Method 1: Manual Installation

### 2.1.1 Clone the project to local

```bash
pip install wheel
git clone https://github.com/Skyler-Sun/Share_And_Talk.git
```

### 2.1.2 Install dependencies

It is recommended to create venv or other virtual environment first

```bash
pip install -r requirements.txt
```

### 2.1.3 Configure the database

First, create a new database, using utf8mb4

Open `ShareAndTalk/config.py`

```python
# Database settings
dbName = 'Your database name'
dbUser = 'Your account name'
dbPassword = 'Your password'
# Email settings
EMAIL_USER = 'Your email'
EMAIL_PASSWORD = 'Your password'
DEFAULT_FROM = 'Your email'

```

Detailes:

- `dbName` : Database name
- `dbUser` : Database username
- `dbPassword` : Password for the corresponding user

Enter commands below

```bash
py manage.py makemigrations
py manage.py migrate
```

### 2.1.4 Configure language and timezone

Default language: Simplified Chinese

Default timezone: GMT+8

See `ShareAndTalk/settings.py`

```python
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

Detailed configuration reference:

[Language Identifier List🚅](http://www.i18nguy.com/unicode/language-identifiers.html)

[Time Zone List 1 Wikipedia🧪](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

[Time Zone List 2🎈](https://www.zeitverschiebung.net/cn/all-time-zones.html)

If you need to change to another language, you also need to delete the following code from `ShareAndTalk/settings.py`

```python
# Default language
LANGUAGES = [
    ('zh-hans', '中文（简体）'),
]
```

### 2.1.5 Configure email (optional)

Used for "user feedback" at the bottom of the homepage

Open `ShareAndTalk/config.py`

```python
# Database settings
dbName = 'Your database name'
dbUser = 'Your account name'
dbPassword = 'Your password'
# Email settings
EMAIL_USER = 'Your email'
EMAIL_PASSWORD = 'Your password'
DEFAULT_FROM = 'Your email'
```

Details:

- `EMAIL_USER` : Recipient email
- `EMAIL_PASSWORD` : Email key
- `DEFAULT_FROM` : Sending email address

See detailed reference [django email configuration](https://docs.djangoproject.com/en/4.1/ref/settings/)

### 2.1.6 Create a superuser

In the root directory of this project, open cmd or powershell or other terminals and enter the following command

```bash
py manage.py createsuperuser
```

Follow the prompts to create

### 2.1.7 Deployment🌭

1. Open `ShareAndTalk/settings.py` and change

```python
DEBUG = True
```

to

```python
DEBUG = False
```

2. Open powershell, go to the repository root directory, and run the following command to copy the static files to the `static` folder

```bash
py manage.py collectstatic
```

> The `static` folder will be automatically created after running the command. If you need to change the folder location, please modify the following code in `ShareAndTalk/settings.py`

```python
STATIC_URL = "static/"
if not DEBUG:
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '/static/'), # Change your static folder here
    )
    STATIC_ROOT = os.path.join(BASE_DIR,'static') # Change your static folder here
```

3. Configure apache2, see [Notion Note](https://www.notion.so/starrytracesky/windows-django-0ae4b2c1562f43fc81f24d755e77f8a5)

# 3. Supplementary Information💻

The location where website users upload files is saved in the `uploads` folder. If you need to change it, locate the following code at the end of `ShareAndTalk/settings.py`

```python
# mdeditor
X_FRAME_OPTIONS = 'SAMEORIGIN'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'

Just modify MEDIA_ROOT to a string containing the absolute path
```

# Common Commands

1. Restore table structure (enter mysql first)

```bash
source backup/db_structure.sql;
```

2. Restore database data

```bash
py manage.py loaddata backup/xxx.json
```

3. Django Shell

```bash
py manage.py shell
```

4. Backup json data

```bash
py -Xutf8 manage.py dumpdata > db.json
```

# [MIT License](https://github.com/StarrySky-skyler/Share_And_Talk/blob/main/LICENSE)
