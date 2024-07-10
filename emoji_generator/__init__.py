from flask import Flask
from .apis import enable_all_apis


app = Flask(__name__, instance_relative_config=True)

enable_all_apis(app)

from emoji_generator import views
