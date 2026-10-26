# Десктоп-клиент

Стек: <...>

Умеет: подключение по адресу и токену, выбор и монтирование папки в `/work`, чат и поток событий, отмена, переподключение.

## Headless / CLI-режим

Нужен для UI- и инфраструктурных тестов:

```bash
client connect --server <url> --token <token>
client mount --folder ./workdir --mode rw
client send "<сообщение>"
client edit --file input.txt --append READY   # изменение файла по сценарию
client cancel
```
