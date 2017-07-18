.
├── README.md
├── requirements.txt
└── supeqcento
    ├── build.py
    ├── bussiness
    │   ├── asset
    │   │   └── __init__.py
    │   ├── data
    │   │   ├── __init__.py
    │   │   └── model.py
    │   ├── device
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── organization
    │   │   └── __init__.py
    │   ├── routes.py
    │   └── user
    │       ├── __init__.py
    │       ├── test_user.py
    │       ├── user_operation.py
    │       ├── user_route.py
    │       └── user_service.py
    ├── extensions
    │   ├── email
    │   │   └── __init__.py
    │   ├── __init__.py
    │   └── lbmp
    │       └── __init__.py
    ├── __init__.py
    ├── __init__.pyc
    ├── libs
    │   └── __init__.py
    └── run.py

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
