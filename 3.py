from flask import Flask
import os
app = Flask(__name__)


class yoyo:
    def hello_world(self):
        return 'Hello World!'

    def hello(self):
        return 'yo yo honey singh'

if __name__ == '__main__':
    tt=yoyo()
    app.add_url_rule('/x/',view_func=tt.hello)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
    #app.run()
