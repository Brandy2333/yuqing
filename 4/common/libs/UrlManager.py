# 搭建 flask-MVC框架
class UrlManager(object):
    def __init__(self):
        pass

    # 静态方法
    @staticmethod
    def buildUrl(path):
        return path

    # 本地地址
    @staticmethod
    def buildStaticUrl(path):
        # ver = "%s" % (11111)
        ver = "%s" % 1.0
        path = "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl(path)