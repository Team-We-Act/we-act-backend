import sqlite3
import click
import os
from flask import current_app,g 
from flask.cli import with_appcontext
def get_db():
    if 'db' not in g:
        print('현재 경로',current_app.root_path)
        g.db = sqlite3.connect(os.path.join(current_app.root_path,'WeAct.db'),
        detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory=sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()

# conn - sqlite3.connect()
# c = conn.cursor() 
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

## cmd 실행 후 2차
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database')