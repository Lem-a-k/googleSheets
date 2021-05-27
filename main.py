import os
from flask import Flask

app = Flask(__name__)


@app.route('/<text>')
def index(text):
    return 'schoolX'


def main():
    if 'HEROKU' in os.environ:
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    else:
        app.run()
if __name__ == '__main__':
    main()


