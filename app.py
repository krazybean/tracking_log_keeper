#!flask/bin/python
import json
from flask import Flask, jsonify
from utils.connectors import Mysql

app = Flask(__name__)

VERSION = 'v1.0'

db_conf = 'db.conf'

config = json.loads(open(db_conf, 'r').readlines()[0])

db = Mysql()

mysql = db.connect(host=config['host'],
                   user=config['user'],
                   passwd=config['passwd'],
                   db=config['db'])


@app.route('/{0}/subsystems/'.format(VERSION), methods=['GET'])
def get_all_subsystems():
    subsystems = {'test': 'test_data',
                  'test2': 'test_data2'}
    return jsonify({'subsystems': subsystems})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002, debug=True)
