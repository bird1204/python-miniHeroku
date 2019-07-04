# -*- coding: UTF-8 -*-
import os
import sys
import tarfile
import subprocess

from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        os.makedirs(app.root_path + '/storage')
    except OSError:
        pass

    # 路由和處理函式配對
    @app.route('/', methods=['GET'])
    def index():
        return 'Hello World!'

    @app.route('/uploads/new', methods=['GET'])
    def new():
        return render_template('uploads/new.html', name=__name__)

    @app.route('/uploads', methods=['POST'])
    def create():
        f = request.files['file']
        file_path = app.root_path + '/storage/' + secure_filename(f.filename)
        f.save(file_path)

        with tarfile.open(file_path) as tf:
          try:
            tf.extractall(path=app.root_path + '/storage/')
          except IOError:
            pass

        subprocess.call(['python3', file_path.split('.')[0] + '/manage.py', 'runserver', '5000'])
        return 'file upload, go to: http://localhost:5000'

    return app

