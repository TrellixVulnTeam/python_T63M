import urllib.request
import urllib.error

def use_proxy(url,proxy_addr):
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)  #第二个参数默认为urllib.request.HTTPHandler
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return data

proxy_addr = "219.138.58.000:8"#这个IP是当时测试时候用的，自己更换就行
url = "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_6049b1c219b74e689d3c5f78660048ef"
data = use_proxy(url,proxy_addr)
print((data))