#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pythones.net

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return ("visita https://pythones.net!")

if __name__ == "__main__":
    app.run()
