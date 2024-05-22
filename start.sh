#!/bin/bash

# 等待 MySQL 服务和数据库准备就绪
echo "等待数据库准备就绪..."
python3 manage.py check
while [ $? -ne 0 ]; do
    echo "数据库未准备就绪，继续等待..."
    sleep 5
    python3 manage.py check
done

# 初始化表结构
echo "初始化表结构..."
python3 manage.py migrate

# 导入数据
echo "导入数据..."
python3 manage.py loaddata ./backup/example.json

# 启动 Django 项目
echo "启动 Django 项目..."
python3 manage.py runserver 0.0.0.0:8000
