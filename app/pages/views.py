from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)


@pages.route('/')
@pages.route('/index')
def index():
    return render_template('index.html')
