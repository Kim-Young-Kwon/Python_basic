#!python
print("Content-Type: text/html")   
print()
import cgi, view

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form.getvalue("id")
    description = open('data/'+pageId, 'r').read()
    description = description.replace('<','&lt;')
    description = description.replace('>','&gt;')
else:
    pageId = "Welcome"
    description = 'Hello, Web'

print('''<!doctype html>  
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList()))