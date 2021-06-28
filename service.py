#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

current_ip = ''


@app.route('/save_ip', methods=['GET', 'POST'])
def get_service_info():
    global current_ip
    current_ip = request.args.get('ip', 'No ip')
    return jsonify({'result': 'done'})


@app.route('/get_ip', methods=['GET', 'POST'])
def update_subscription_statistics():
    return jsonify({'result': current_ip})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
