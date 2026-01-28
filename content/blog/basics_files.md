+++
title = "File handling"
date = "2026-01-13T16:18:07+01:00"
draft= false
+++

Read a file (Textfile):

```python
with open("filename") as file:
        print(file.read())
```

Write a file:

```python
with open("filename","w") as file:
        file.write("Test")
```

Basics out of the way. 

TODO
append/replace/...
seek
binary
