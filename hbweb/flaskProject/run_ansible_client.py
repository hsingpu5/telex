# /usr/bin/env python3
import os
import json
from flask import Flask

app = Flask(__name__)


@app.route('/kfk/v1/list')
def index():
    res = os.popen('ansible kafka -m shell  -a "/usr/java/jdk1.8.0_181/bin/jps | grep afka | wc -l"   -o')
    result = res.read().split('\n')
    # for i in res.read().split('\n'):
    # r=i.split('|')
    # print (r[0],r[-1])
    print(result)
    return json.dumps(result)


if __name__ == '__main__':
    app.run(host='133.0.124.212', debug=True)
