"""
=================================================
@Project -> File    : Share_And_Talk -> update
@IDE                : VS Code
@Author             : Starry Trace Sky
@Date               : 2023/06/23 19:46
@Last edit          : 2024/05/13 20:18
@Usage              : 
@email              : starrytracesky@qq.com
==================================================
"""
import re
import os
import sys
from github import Github

import pysnooper


with pysnooper.snoop():
    pattern = r"-+(v\d+\.\d+\.\d+.*)-+"
    # github token
    token = os.environ.get('GITHUB_TOKEN')
    g = Github(token)
    # latest tag
    repo = g.get_repo('StarrySky-skyler/Share_And_Talk')
    latestTag = repo.get_tags()[0]
    tagName = latestTag.name
    originTagName = latestTag.name

@pysnooper.snoop()
def updateMD(file):
    """
    update README
    param: file: README path
    """
    global tagName

    with open(file, encoding='utf-8') as f:
        content = f.readlines()
    Content = ''.join(content)
    result = re.findall(pattern, Content)[0]

    # already up to date
    if result == tagName:
        print("Info: README is up to date. No need to update again.")
        sys.exit()

    if '-' in tagName:
        tagName = tagName.replace('-', '_')

    tagName = '-' + tagName + '-'
    Content = re.sub(pattern, tagName, Content)

    # update REAMDE.md
    with open(file, 'w', encoding='utf-8') as f:
        f.write(Content)

@pysnooper.snoop()
def release():
    """提交更改"""
    # 获取最新的提交对象
    global originTagName
    latestCommit = repo.get_commits()[0]

    # create release

    # 获取最新提交的 commit message 属性
    try:
        tagMessage = latestCommit.commit.message
    except AttributeError:
        tagMessage = originTagName
    repo.create_git_release(tag=originTagName, name=originTagName, message=tagMessage)

if __name__ == '__main__':
    updateMD('README.md')
    updateMD('README_zh_cn.md')
    release()
