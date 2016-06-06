class CheckBrowser(object):
    # Request预处理函数,调用时机在 Django 接收到 request
    # 之后，但仍未解析URL以确定应当运行的 view 之前。Django 向它传入相应的
    # HttpRequest 对象，以便在方法中修改。
    def process_request(self,request):
        # 将会在后台返回一串信息，包含浏览器信息，这里指定打出浏览器信息
        print (request.META['HTTP_USER_AGENT']) 