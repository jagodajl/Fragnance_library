from app import app, db
from app.models import Brand, Fragnance


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Brand": Brand,
        "Fragnance": Fragnance
    }

