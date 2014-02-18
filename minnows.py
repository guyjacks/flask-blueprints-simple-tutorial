from flask import Blueprint, render_template

minnows = Blueprint('minnows', __name__, template_folder='templates/minnows')

@minnows.route('/')
def list():
    #return 'minnows list'
    return render_template('list.html')

@minnows.route('/create')
def create():
    return 'create shark'

@minnows.route('/read')
def read():
    return 'read shark'

@minnows.route('/update')
def update():
    return 'update shark'

@minnows.route('/delete')
def delete():
    return 'delete shark'
