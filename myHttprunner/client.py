import requests


class HttpClient():

    def __init__(self, request_desc, client=None):
        self.request_desc = request_desc
        self.client = client

    def send_response(self):
        if not self.client:
            self.client = requests.Session()
        resp = self.client.request(**self.request_desc)
        return resp

    def run(self):
        # 组装请求
        # 前置脚本
        # 发送http请求
        # 后置脚本
        # 断言
        pass
