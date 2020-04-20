#!python
print("Content-Type: text/html; charset=utf-8\n")
print()
import cgi, os #'cgi,os라는 모듈을 사용하겠다' 라고 파이썬에게 얘기해주는것

files = os.listdir('data')
listStr = ''
for item in files:
    # listStr = listStr + item  #기존값 + item
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
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
        {listStr}
      </ol>
    </div>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
    </form>
  </body>
</html>'''.format(title=pageId, desc=description, listStr=listStr))
