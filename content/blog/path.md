+++
title = "Path"
date = "2026-01-13T16:18:07+01:00"
draft= false
+++

In Python you can use Paths like an Object.

```python
from pathlib import Path
p = Path("/tmp")
print(p)

print(p.exists())
print(p.is_dir())
```

To get the filename:
```python
p.name
```

To get the suffix:
```python
p.suffix
```

To get the filename without extension ( basename ):
```python
p.stem
```

To get the path with an new filename/extension use:
```python
p.with_name("test.txt")
p.with_suffix(".md")
p.with_stem("result")
```

Get the current working directory:
```python
p.cwd()
```

Get users home directory:
```python
p.home()
```

To read the file:
```python
p.read_text()
```

To write into the file:
```python
p.write_text("test")
```



