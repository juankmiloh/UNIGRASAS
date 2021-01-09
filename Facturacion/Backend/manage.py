#!/usr/bin/env python
import os
from src import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)

@manager.command
def test():
    from subprocess import call

    os.environ['FLASK_CONFIG'] = 'testing'
    call(['nosetests', '-v',
          '--with-coverage', '--cover-package=app', '--cover-branches',
          '--cover-erase', '--cover-html', '--cover-html-dir=cover'])

if __name__ == '__main__':
    # print("_______ app.config.get('ENV') _____________")
    # print(app.config.get("ENV"))
    # print("____________________")

    if app.config.get("ENV") == 'production': # Cambiar dependiendo el servidor donde se despliegue la aplicacion (development || production)
        app.run() # Correr la aplicacion localmente
    else:
        manager.run() # Correr la aplicacion desplegada en servidor