#!python
print("Content-Type: text/html; charset=utf-8\n")
print()
import cgi #'cgi라는 모듈을 사용하겠다''라고 파이썬에게 얘기해주는것
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello web'
print('''<!DOCTYPE html>
<html>
  <head>
    <title>WEB - welcome</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <div id="grid">
      <ol>
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</a></li>
      </ol>
      <div id="article">
    <h2>{title}</h2>
    <p>{desc}</p>
      </div>
    </div>
  </body>
</html>'''.format(title=pageId, desc=description))
