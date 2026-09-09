## Schedulare

I primi due task sono schedulati con cronical

from an elevated console  install the service

cronical.exe --install

and then start it up using Windows Services, or simply

net start cronical


L'ultimo task (invio a Fosforo compresi i RAW) e` schedulato con "C:\Windows\system32\taskschd.msc"
Utilita di piamificazione di Windows

Fa schifo il fatto di usare sue sistemi diversi, ma l'ultimo non funziona con cronical.



## setup ssh

Creo chiave fondazione@ossigeno `ssh-keygen`

la copio su Fosforo in /home/fondazione/.ssh/authorized_keys

suo ossigeno creo file ~/.ssh/config

```
Host fosforo
HostName 10.8.0.1
User fondazione
```