# -*- encoding:utf-8 -*-
from flask_assets import Environment, Bundle

assets = Environment()

main_js = Bundle(
    'libs/jquery/dist/jquery.min.js',
    'libs/bootstrap/dist/js/bootstrap.min.js',
    filters='jsmin',
    output='js/main.min.js'
)

main_css = Bundle(
    'libs/bootstrap/dist/css/bootstrap.min.css',
    'libs/font-awesome/css/font-awesome.min.css',
    filters='cssmin',
    output='css/common.min.css'
)

custom_css = Bundle(
    'css/ltestyle.min.css',
    'css/custom.css',
    filters='cssmin',
    output='css/custom.min.css'
)

fonts = Bundle(
    'libs/bootstrap/fonts/*',
    'libs/font-awesome/fonts/*',
    output='fonts/'
)

assets.register('main_js', main_js)
assets.register('main_css', main_css)
assets.register('css', custom_css)
assets.register('fonts', fonts)