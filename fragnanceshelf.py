from app import app, db
from app.models import Fragnance, Brand

@app.shell_context_processor
def make_shell_context():
    return {
    "db": db,
    "Fragnance": Fragnance,
    "Brand": Brand
    }