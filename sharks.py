from flask import Blueprint, render_template

sharks = Blueprint('sharks', __name__, template_folder='templates')

@sharks.route('/')
def list():
    #return 'sharks list'
    return render_template('sharks/list.html')

@sharks.route('/create')
def create():
    return 'create shark'

@sharks.route('/read')
def read():
    return 'read shark'

@sharks.route('/update')
def update():
    return 'update shark'

@sharks.route('/delete')
def delete():
    return 'delete shark'
