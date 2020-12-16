from flask import Blueprint, request, redirect, url_for
from flask import render_template


home = Blueprint("home", __name__)


@home.route('/')
def base_page():
    return render_template('home.html')


@home.route('/<random>')
def error_page(random):
    return render_template('not_found.html')