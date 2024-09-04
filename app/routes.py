from flask import Blueprint, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return f'<h1>Index</h1>'

@main.route('/help')
def help():
    return f'<h1>Help</h1>'