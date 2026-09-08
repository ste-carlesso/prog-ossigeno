Setup on Microsoft Windows 11

Se non c'é creare un file secret.toml

```
[main]
# base_dir is written according to Python pathlib, using slash not backslash.
# Windows 'D:/'
# Linux '/home/ste/D'
base_dir = '/home/ste/D'

[api]
name = 'ossigeno-03 upload service'
token = 'sk_XXXXXXXXX'
```


Poi creare un ambinete Python e installare la libreria requests

```
python.exe -m venv env

env\Script\activate.bat 

pip install --upgrade pip

pip install requests

```


