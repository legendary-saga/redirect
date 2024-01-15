# redirect
easy setup redirect script

# usage
1. by command arguments
```bash
python redirect.py --target https://legenradysaga.org --port 8888 
```

2. by running
```bash
python redirect.py

Enter the target URL: https://legendarysaga.org
Enter the port number: 8888                        
```

# result
```bash
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8888 (Press CTRL+C to quit)  
```

* server now available on `http://0.0.0.0:8888` or `http://localhost:8888`

# install
1. Clone repository
```bash
git clone https://github.com/legendary-saga/redirect.git

cd redirect
```

2. Install python requirements 
```bash
pip install -r requirements.txt
```