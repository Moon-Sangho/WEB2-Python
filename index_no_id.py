#!python
print("Content-Type: text/html; charset=utf-8\n")
print()
import cgi #'cgi라는 모듈을 사용하겠다''라고 파이썬에게 얘기해주는것
pageId = 'Welcome'
print('''<!DOCTYPE html>
<html>
  <head>
    <title>WEB - welcome</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1><a href="index_no_id.py">WEB</a></h1>
    <div id="grid">
      <ol>
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</a></li>
      </ol>
      <div id="article">
    <h2>{title}</h2>
    <p>
      The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991.
    </p>
      </div>
    </div>
  </body>
</html>'''.format(title=pageId))
