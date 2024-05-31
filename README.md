# Описание
MainServiceManager - менеджер сервисов (аналогично `systemctl` в `Linux`). Каждый пользователь может запустить свой сервер MainServiceManager при условии, что они запущены на разных портах. Программы, у которых есть пароль, могут использовать API для управления всем сервером и всеми сервисами. Сервисы могут использовать API для управления собой (ограниченный доступ).
# Использование встроенного API
```python
from MainServiceManager import Launcher
# Инициализация API
launcher=Launcher({"user":"admin","password":"qwerty :)"})
# Проверить статус сервера
try:
  launcher.admin_status()
  print("Сервер доступен")
except:
  print("Сервер недоступен")
# Остановить сервер
launcher.admin_stop()
```
# Конфиг сервера
По умолчанию настройки сервера хранятся в файле `~/.config/MainServiceManager/cfg.json`
Если файл не существует, он будет создан
Настройки по умолчанию:
```json
{
  "host":"127.0.0.1",
  "password":"",
  "port":8960,
  "services_dir":"{папка с конфигом}/services",
}
```
- `host` - IP адрес, на котором будет запущен сервер
- `port` - порт, на котором будет запущен сервер
- `password` - пароль от аккаунта `admin`. Не забудьте его изменить!
- `services_dir` - папка с файлами сервисов
# Файлы сервисов
Если параметр не указан, он равен `null`
Недопустимые параметры игнорируются, но видны при получении информации о сервисе
Тип записи:
- `параметр` (`тип`) - описание
## Обязательные параметры
- `args` (`list`) - список аргументов для запуска
## Дополнительные параметры
- `autostart` (`bool`) - включать сервис при запуске сервера?
- `data_path` (`str`) - путь к файлу JSON для записи информации о сервисе (в том числе персональный пароль)
- `cwd` (`str`) - рабочая папка
- `env` (`dict`) - переменные среды
- `clean_env` (`bool`) - отключить наследование ENV от процесса сервера?
- `restart` (`str`) - условие для автоматического перезапуска
- | `"always"` - перезапускать при любой остановке процесса
- | `"on_error"` - перезапускать если процесс остановился с кодом ≠0
- | `"code=N"` - (в будущем) перезапускать если процесс остановился с кодом N
- | `"code!=N"` - (в будущем) перезапускать если процесс остановился с кодом ≠N
- | `null` - не перезапускать
## Параметры для Linux
Если параметры недоступны, они игнорируются
- `user` (`str`) - пользователь, от имени которого нужно запускать процесс
- `group` (`str`) - группа, в которой нужно запускать процесс
- `extra_groups` (`unknown`) - неизвестно, не рекомендуется для использования