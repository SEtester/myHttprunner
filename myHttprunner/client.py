import requests


class HttpClient():

    def __init__(self, request_desc, client=None):
        self.request_desc = request_desc
        self.client = client

    def __del__(self):
        self.client.close()

    def send_response(self):
        if not self.client:
            self.client = requests.Session()
        resp = self.client.request(**self.request_desc)
        return resp

    def run(self):
        # 组装请求
        # 前置脚本
        # 发送http请求
        resp = self.send_response()

        # 后置脚本
        # 断言
