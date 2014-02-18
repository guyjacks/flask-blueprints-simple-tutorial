from flask import Blueprint, render_template

fish = Blueprint('fish', __name__, template_folder='templates')

@fish.route('/')
def list():
    return render_template('fish/list.html')

@fish.route('/create')
def create():
    return 'create fish'

@fish.route('/read')
def read():
    return 'read fish'

@fish.route('/update')
def update():
    return 'update fish'

@fish.route('/delete')
def delete():
    return 'delete fish'
