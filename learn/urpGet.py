# -*- utf-8 -*-
import http.cookiejar as cookie
import urllib
import urllib.parse
import urllib.request


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
        with open("C:/Users/k/gitme/python/w.jpeg", "wb") as f:
            f.write(r.read())
        print(cok)
        for index in cok:
            print(index.name)
            print(index.value)

        # zjh1 = & tips = & lx = & evalue = & eflag = & fs = & dzslh = & zjh = 131292 & mm = 131292 & v_yzm = 1111
        ss = input("请输入验证码")
        print(ss)
        result = {'zjh1': '', 'tips': '', 'evalue': '', 'eflag': '', 'fs': '', 'dzslh': '',
                  'zjh': '131292', 'mm': '131292', 'v_yzm': ss, 'lx': ''}
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
        from requests_html import HTMLSession
        sess = HTMLSession()

        urls = 'http://urp.npumd.cn/validateCodeAction.do?random=0.14807469019073965'
        headers = {'user-agent': 'User-Agent	Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                   'Connection': 'keep-alive', 'Host': 'urp.npumd.cn', 'Referer': 'http://urp.npumd.cn/'}

        ss = sess.get(url=urls, headers=headers)

        print((ss.cookies))
        with open("C:/Users/k/gitme/python/w.jpeg", "wb") as f:
            f.write(ss.content)
        ssa = input("请输入验证码")
        print(ssa)
        result = {'zjh1': '', 'tips': '', 'evalue': '', 'eflag': '', 'fs': '', 'dzslh': '',
                  'zjh': '141275', 'mm': '141275', 'v_yzm': ssa, 'lx': ''}
        # rs = urllib.parse.urlencode(result).encode(encoding='UTF8')
        url_login = 'http://urp.npumd.cn/loginAction.do'
        # ,cookies=requests.utils.dict_from_cookiejar(ss.cookies)
        print(sess.cookies)
        resp = sess.post(url_login, data=result
                         , headers=headers)
        # cookies=requests.utils.dict_from_cookiejar(ss.cookies))

        # with open("C:/Users/k/gitme/python/w.html", "wb") as f:
        #     f.write(resp.text.encode())
        txt = sess.get(url="http://urp.npumd.cn/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2016-2017学年第二学期(三学期)")
        tp = txt.html.find('body', first=True)
        ts = tp.find('td')
        print(ts)
        for index in ts:
            print(index.text)

        from lxml import etree
        print(txt.text)
        htm = etree.HTML(txt.text)
        html_data = htm.xpath('/html/body/table/td')
        print(html_data)


if __name__ == '__main__':
    getResource().req_html()
    # ss = "b'sssasa"
    # print(ss[2:-1])
