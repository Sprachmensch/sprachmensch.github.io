+++
title = "Check for elevated Privileges"
date = "2026-01-15T23:01:37+01:00"
draft= false
+++

On Linux you can use the `os` module to first check the os and the get the user id

```python
import os

if os.name == 'posix':
    print(os.getuid())
```

Complete Function to check if the script is running with elevated Privileges
```python
import os

def is_elevated():
    if os.name == 'posix':
        return os.getuid() == 0
    else:
        return False

print(is_elevated())
```
