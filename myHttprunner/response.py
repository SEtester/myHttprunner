import json


class ResponseObject(object):

    def __init__(self, resp_obj):
        """ initialize with a requests.Response object

        Args:
            resp_obj (instance): requests.Response instance

        """
        self.resp_obj = resp_obj

    def __getattr__(self, key):
        try:
            if key == "json":
                value = self.resp_obj.json()
            elif key == "cookies":
                value = self.resp_obj.cookies.get_dict()
            elif key == "request_body":
                value = self.resp_obj.request.body
                try:
                    value = json.loads(value)
                except ValueError:
                    # 待改造
                    pass
                    # from utils import DataHandler
                    # value = DataHandler.parse_form_to_dict(value)
            else:
                value = getattr(self.resp_obj, key)

            self.__dict__[key] = value
            return value
        except AttributeError:
            err_msg = "ResponseObject does not have attribute: {}".format(key)
            # logger.log_error(err_msg)
            # raise exceptions.ParamsError(err_msg)