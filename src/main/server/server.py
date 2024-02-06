from flask import Flask
from src.main.routes.tag_routes import tag_route_BP

app = Flask(__name__)
app.register_blueprint(tag_route_BP)
