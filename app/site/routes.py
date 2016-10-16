# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template

site = Blueprint('site', __name__)


@site.route("/")
def index():
    """
    Pagina de inicio
    """
    return render_template("site/index.html")