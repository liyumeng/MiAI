#!/usr/bin/env python3

import connexion
from swagger_server.encoder import JSONEncoder
import os,sys

app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
app.app.json_encoder = JSONEncoder
app.app.config.from_object('config')
app.add_api('swagger.yaml', arguments={'title': 'MIAI'})
application=app.app

if __name__ == '__main__':
    app.run(port=12030,server='tornado')
    #app.run(port=12030)
