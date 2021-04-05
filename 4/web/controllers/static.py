# 后台搭建

# 解决加载静态资源问题
from flask import Blueprint, send_from_directory
from application import app

# 本地加载所需项
route_static = Blueprint('static', __name__)


@route_static.route("/<path:filename>")
def index(filename):
    return send_from_directory(app.root_path + "/web/static/", filename)