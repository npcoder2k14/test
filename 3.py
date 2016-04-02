from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/hi')
def hello():
    return 'yo yo honey singh'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
    #app.run()
