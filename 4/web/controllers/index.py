# 词云系统

from flask import Blueprint
# from common.libs.Helper import ops_render
from common.libs.Helper import ops_render

route_index = Blueprint('index_page',__name__)


@route_index.route('/')
def index():
    # return "欢迎关注小徐的GitHub：https://github.com/xd-stupid/yuqing"
    return ops_render("index/index.html")