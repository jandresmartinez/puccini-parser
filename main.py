from app import create_app
from config import config

app = create_app()
app.config.from_object(config['default'])
app.run(port=config['default'].PORT)
