#!python

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

# print(title, description)
opened_file = open('data/'+title, 'w')
opened_file.write(description)

#Redirection
print("Location: index.py?id="+title)
print()
