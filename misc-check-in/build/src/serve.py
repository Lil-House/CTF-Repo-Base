from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open('/flag', 'r') as f:
        flag = f.read().strip()
    return f'Welcome to the challenge! Here is your flag: {flag}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)