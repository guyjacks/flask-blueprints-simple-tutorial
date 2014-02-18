from flask import Blueprint, render_template

fish = Blueprint('fish', __name__, template_folder='templates/fish')

@fish.route('/')
def list():
    return render_template('fish/list.html')

@fish.route('/create')
def create():
    return 'create shark'

@fish.route('/read')
def read():
    return 'read shark'

@fish.route('/update')
def update():
    return 'update shark'

@fish.route('/delete')
def delete():
    return 'delete shark'
