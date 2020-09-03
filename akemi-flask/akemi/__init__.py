import os
import json

from flask import Flask, render_template, jsonify
from akemi.db import get_db

# Aquest document es el principal de la nostra aplicació


def create_app(test_config=None):
    # crea i configura la app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'akemi.sqlite'),
    )

    if test_config is None:
        # carreguem la configuració del 'instance' si hi ha
        app.config.from_pyfile('config.py', silent=True)
    else:
        # carreguem la configuració si hi ha
        app.config.from_mapping(test_config)

    # asegurar que existeix la carpeta 'instance'
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # metode per pasar la base de dades actual sqlite a JSON
    @app.route('/akemi/products/')
    def akemiproducts():

        # agafem les dades de la base de dades fent una consulta
        db = get_db()
        data = db.execute(
            ' SELECT id, name, price, src '
            ' FROM products '
        ).fetchall()

        # amb aquesta linea fem un bucle amb les dades trobades i les pasa a JSON
        prod = [{'id': products['id'], 'name':products['name'],
                 'price':products['price'], 'src':products['src']} for products in data]

        return jsonify(prod)

    from . import db
    db.init_app(app)

    return app


