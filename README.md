## 目录
[项目任务](https://github.com/fujunchao88/supeqcento/wiki/SupeqCento-Tasks)  
[目录结构](https://github.com/fujunchao88/supeqcento/wiki/SupeqCento-Catalog-Struct)  
[数据脚本](https://github.com/fujunchao88/supeqcento/wiki/SupeqCento-DB-Initial-Script)

## 启动
```
python run.py -h

usage: run.py [-h] --host HOST --port PORT [--workers WORKERS] [--debug]
              {supeqcento,email}

positional arguments:
  {supeqcento,email}  choose server from (supeqcento|email)

optional arguments:
  -h, --help          show this help message and exit
  --host HOST
  --port PORT
  --workers WORKERS   multiple processes,by default using only one CPU core
  --debug
```
