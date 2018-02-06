import urllib.request

opener = urllib.request.FancyURLopener({})
url = "http://dantri.com.vn/"
f = opener.open(url)
content = f.read().decode('utf8')

print(content)
