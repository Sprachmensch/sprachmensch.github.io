+++
title = "Parse Commandline Arguments"
date = "2026-01-15T23:01:37+01:00"
draft = false
+++

quick'n'dirty with `argparse`
```python
import argparse

parser =argparse.ArgumentParser()

parser.add_argument("name")         # required argument
parser.add_argument("--age","-a")   # optional argument

args = parser.parse_args()
print(f"Name {args.name} - {args.age}")
```

For bigger Projects/Production ready ones take a look at [click](https://click.palletsprojects.com/).

```python
pip install click
```

```python
import click

@click.command()
@click.option("--name", default="anon")
def username(name):
    print(f"name {name}")

if __name__ == '__main__':
    username()
```
