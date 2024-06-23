# views.py：路由+视图函数
# 蓝图
from flask import Blueprint
from .models import *

blue = Blueprint('user', __name__)

@blue.route('/adminapi/menu/getMenuTree')
def index():
    return '你好啊'