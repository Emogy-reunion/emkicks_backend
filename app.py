from core import create_app
from core.utils.create_db import create_tables

app = create_app()

with app.app_context():
    create_tables()

if __name__ == '__main__':
    app.run(debug=True)

