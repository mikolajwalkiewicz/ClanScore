from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

# from clanscore import routes
