# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template

site = Blueprint('site', __name__)  # Create the blueprint for this module


# Make the first entry route
@site.route('/')
def index():
    """
    Index site page.
    """
    return render_template("site/index.html")