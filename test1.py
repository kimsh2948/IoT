import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip()
<html class="svgless" lang="ko">

<head>

<meta charset="utf-8"/>

<meta content="origin" name="Referrer"/>