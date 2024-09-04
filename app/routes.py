from flask import Blueprint, redirect, url_for
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return f'<h1>Index</h1>'

@main.route('/help')
def help():
    return f'<h1>Help</h1>'

@main.route('/req')
def req():
    url = 'www.google.com'

    page = requests.get(url)

    try:
        if not page.status_code == 200:
            return f'status code: {page.status_code}'
        else:
            return f'{page.text}'
    except Exception as e:
        return str(e)