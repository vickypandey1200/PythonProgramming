import urllib.request, webbrowser, http.client
##loginPage = urllib.request.urlopen('http://10.66.98.155:18793/sbm/bpmportal/login.jsp')
##for line in loginPage:
##    print(line.strip())
##webbrowser.open_new_tab("http://example.net")
##print("Should be working ??")
h1 = http.client.HTTPConnection('www.python.org')
print(h1.request("GET","www.python.org"))
