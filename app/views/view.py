from flask import Blueprint, render_template
from app import loger
from app.book_builder import BookGenerator

mod = Blueprint('test', __name__, template_folder='templates/book_views')


@mod.route('/index')
@mod.route('/')
def test_hello():
    loger.info("Start create svg")
    bg = BookGenerator("Hi")
    bg.paster_in_svg.delay("app/templates/book_builder/svg_template/2.svg",
                           "/home/kryvonis/PycharmProjects/CeleryTask/app/templates/book_builder/svg_template/2.svg")
    bg.generate_page_pdf.delay("app/templates/book_builder/svg_template/2.svg",
                               "app/templates/book_builder/pdf_template/2.pdf")
    return 'Hello'
