# -*- utf-8 -*-
import http.cookiejar as cookie
import urllib
import urllib.parse
import urllib.request

import requests


class getResource:
    def get_html(self):
        urls = 'http://urp.npumd.cn/validateCodeAction.do?random=0.14807469019073965'
        headers = {'user-agent': 'User-Agent	Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                   'Connection': 'keep-alive'}
        req = urllib.request.Request(url=urls, headers=headers)

        cok = cookie.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookiejar=cok)
        opener = urllib.request.build_opener(handler)
        r = opener.open(req)
        with open("d:/w.jpeg", "wb") as f:
            f.write(r.read())
        print(cok)
        for index in cok:
            print(index.name)
            print(index.value)

        # zjh1 = & tips = & lx = & evalue = & eflag = & fs = & dzslh = & zjh = 131292 & mm = 131292 & v_yzm = 1111
        ss = input("请输入验证码")
        print(ss)
        result = {'zjh1': '', 'tips': '', 'evalue': '', 'eflag': '', 'fs': '', 'dzslh': '',
                  'zjh': '131292', 'mm': '131292', 'v_yzm': ss}
        rs = urllib.parse.urlencode(result).encode(encoding='UTF8')
        url_login = 'http://urp.npumd.cn/loginAction.do'
        req_login = urllib.request.Request(url=url_login, headers=headers, data=rs)
        rr = opener.open(req_login)
        print(rr.read())
        for index in cok:
            print(index.name)
            print(index.value)

        url_add = urllib.parse.urlencode({'lnxndm': "2016-2017学年第二学期(三学期)"})
        print(url_add)
        url_all = 'http://urp.npumd.cn/gradeLnAllAction.do?type=ln&oper=qbinfo&' + url_add
        req_al = urllib.request.Request(url=url_all, headers=headers)
        result_all = opener.open(req_al)
        print(result_all.read().decode('gbk'))

    def req_html(self):
        urls = 'http://urp.npumd.cn/validateCodeAction.do?random=0.14807469019073965'
        headers = {'user-agent': 'User-Agent	Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                   'Connection': 'keep-alive'}

        ss = requests.get(url=urls, headers=headers)
        s_cookie = ss.cookies
        print(type(ss.cookies))
        sa = requests.utils.dict_from_cookiejar(ss.cookies)
        print(sa)
        with open("d:/w.jpeg", "wb") as f:
            f.write(ss.content)
        ssa = input("请输入验证码")
        print(ssa)
        result = {'zjh1': '', 'tips': '', 'evalue': '', 'eflag': '', 'fs': '', 'dzslh': '',
                  'zjh': '131292', 'mm': '131292', 'v_yzm': ssa}
        rs = urllib.parse.urlencode(result).encode(encoding='UTF8')
        url_login = 'http://urp.npumd.cn/loginAction.do'
        ssrq = requests.session()
        requests.utils.add_dict_to_cookiejar(ssrq.cookies, sa)
        resp = ssrq.post(url_login, data=rs, headers=headers)
        print(resp.text)


if __name__ == '__main__':
    getResource().req_html()
