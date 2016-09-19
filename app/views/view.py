from flask import Blueprint, render_template
import logging as loger

loger.basicConfig(filename='main.log', level=loger.DEBUG)

mod = Blueprint('test', __name__, template_folder='templates/book_views')


@mod.route('/index')
@mod.route('/')
def test_hello():
    loger.info("Hello")
    return 'Hello'
