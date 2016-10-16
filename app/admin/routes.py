# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template

mod = Blueprint('admin', __name__) # Create the blueprint for this module


@mod.route("/")
def index():
    """
    Admin home page.
    """
    return render_template("admin/admin.html")