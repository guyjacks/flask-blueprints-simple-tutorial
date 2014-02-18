from flask import Blueprint, render_template

minnows = Blueprint('minnows', __name__, template_folder='minnows')

@minnows.route('/')
def list():
    #return 'minnows list'
    return render_template('minnows/list.html')

@minnows.route('/create')
def create():
    return 'create minnows'

@minnows.route('/read')
def read():
    return 'read minnows'

@minnows.route('/update')
def update():
    return 'update minnows'

@minnows.route('/delete')
def delete():
    return 'delete minnows'
