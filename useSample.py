# -*- coding=utf8 -*-
import harborclient_v2_0
import urllib3

urllib3.disable_warnings()

class GetHarborApi(object):
    def __init__(self, host, user, password, protocol="https"):
        self.host = host
        self.user = user
        self.password = password
        self.protocol = protocol
        self.client = harborclient_v2_0.HarborClient(self.host, self.user, self.password, self.protocol)

    def main(self):
        print(self.client.get_projects())

if __name__ == '__main__':
    host = "xx.xx.xx.xx"
    user = "x"
    password = "x"
    protocol = "https"
    cline_get = GetHarborApi(host, user, password, protocol)
    cline_get.main()