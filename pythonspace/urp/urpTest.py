import urllib.error
if __name__ == "__main__":
    try:
        import urllib.request

        url = "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_6049b1c219b74e689d3c5f78660048ef"
        # req = urllib.request.Request(url)
        # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0')
        proxy = urllib.request.ProxyHandler({"http": "11.3.78.12:000"})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)

        # request = urllib.request.Request(url)

        data = urllib.request.urlopen(url, timeout=10).read()

        fileurp = open("e:\wpy.html", "wb")
        fileurp.write(data)
        fileurp.close()
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.reason)
