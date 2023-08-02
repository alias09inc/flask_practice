import os
import click
from flask_migrate import Migrate
from app import create_app

app = create_app('default')

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, Role=Role)
