import markdown2
import datetime

header = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>My Github actions Testsite</title>
</head><body>"""
date=datetime.datetime.today()
footer = f'<br><p>Last updated on: {date}</p></body>'

file = open("index.html", "w")
file.write(header)
file.write(markdown2.markdown_path("src/index.md"))

file.write(footer)
file.close()
print("Done!")
