import urllib.request
link = "http://www.jd.com"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.7271 SLBChan/105"
}
request = urllib.request.Request(link, headers=header)
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")
print(html)