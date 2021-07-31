db = {
    'user': 'root',
    'password': 'dlsrb@41632',
    'host': '49.50.166.134',
    'port': '3306',
    'database': 'Flask_Project'}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}\
        :{db['port']}/{db['database']}?charset=utf8"
