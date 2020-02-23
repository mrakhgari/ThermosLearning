from app import app, db
from app.models import User, Post


@app.shell_context_processor
# called when use flask shell
def make_shell_context():
    return {'db': db, 'User': User, 'Post':Post}
