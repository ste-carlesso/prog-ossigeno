2026-09-09
Setup on Microsoft Windows 11

Se non c'é creare un file secret.toml

```
[api]
name = 'ossigeno-03 upload service'
token = 'sk_XXXXXXXXX'
```


Poi creare un ambiente virtuale Python e installare la libreria requests

```
python.exe -m venv env

env\Script\activate.bat 

pip install --upgrade pip

pip install requests

```
In questa cartella c'é Cronical.exe che é installato come servizio (Gestione computer --> servizi)
Esso legge cronical.dat e all'ora stabilita esegue lo script tizio.bat.
A sua volta lo script bat contiene le istruzioni per eseguire lo script Python tizio.py
(nell'ambiente virtuale), e scrivere il file di log corrispondente tizio.log


L'invio a Fosforo deve essere fatto manualmente dopo aver attivato la VPN fosforo.
