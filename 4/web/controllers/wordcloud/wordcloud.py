# 词云系统

  
from flask import Blueprint, request, redirect
from common.models.model import News2
from common.libs.Helper import ops_render
from application import app
from common.libs.wordc.wordc import cut, wordcloudpic
# import jieba

route_wordcloud = Blueprint('wordcloud_page',__name__)

@route_wordcloud.route('/')
def wordcloud():
    # resp_data = {}
    # wanted = "保卫处"
    # result = Cucnew.query.filter_by(department=wanted).all()
    # resp_data['list'] = result
    # return ops_render("/wordcloud/wordcloud.html",resp_data)
    return redirect('/wordcloud/search')


@route_wordcloud.route('/search')
def search():
    resp_data = {}
    wanted = request.args.get("wanted",type=str)
    if wanted == None:
        wanted = " "
    result = News2.query.filter(News2.content.like("%"+wanted+"%"))
    resp_data['list'] = result
    words = ""
    for r in result:
        words += r.content
    # # 加载自定义词库
    # jieba.load_userdict('docs/AIDict.txt')
    # # 加载停顿词
    # with open('docs/stopword.txt','r',encoding='utf-8') as ft:
    #     stopword = ft.read()
    picname,datetime = wordcloudpic(cut(words))
    picaddress = "/outputs/news"+datetime+".jpg"
    resp_data['href'] = picaddress
    app.logger.info(resp_data['href'])
    return ops_render("/wordcloud/wordcloud.html",resp_data)
