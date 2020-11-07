# Mystery file 2

Wenn man den Befehl `file` ausführt, kommt folgendes heraus:
```
file: gzip compressed data, last modified: Sat Nov  7 15:42:20 2020, max compression, from Unix, original size modulo 2^32 2048
```
Die Datei ist also ein gzip Archiv. Wenn wir das ganze dekomprimiert, mit `gunzip -d file.gz` kommt ein tar Archiv heraus. Mit `tar xvf file` bekommt man schließlich die Datei mit dem Flag.

Das Flag ist `JHHDCTF{now_you_can_see_there_are_useful_tools}`
