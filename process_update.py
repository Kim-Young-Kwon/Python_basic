#!python

import cgi, os

form = cgi.FieldStorage()
pageId = form.getvalue("pageId")
title = form.getvalue("title")
description = form.getvalue("description")

opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()

# 현재파일 이름, 변경할 파일 이름
os.rename('data/'+pageId, 'data/'+title)

print("Location: index.py?id="+title) 
print()