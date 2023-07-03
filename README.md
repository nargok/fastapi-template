Fast API Template
===

## How to run application
```
poerty install
poetry shell
uvicorn main:app --reload
```

## How to add packages
```
poetry add <package_name>
```

## How to enable VSCode Debug

1. create .venv directory
```
poetry config virtualenvs.in-project true
```

2. create virtual environment
```
poetry shell
```

3. open VS Code
```
code .
```

## Memo

https://zenn.dev/pesuchin/articles/4c128aeb60cb42204311#%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E7%9B%B4%E4%B8%8B%E3%81%A7%E4%BB%AE%E6%83%B3%E7%92%B0%E5%A2%83%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B%E3%82%88%E3%81%86%E3%81%ABpoetry%E3%81%AE%E8%A8%AD%E5%AE%9A%E3%82%92%E5%A4%89%E6%9B%B4%E3%81%99%E3%82%8B



https://speakerdeck.com/iktakahiro/ddd-and-onion-architecture-in-python
