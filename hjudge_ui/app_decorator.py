from flask import request, render_template, jsonify, send_from_directory, redirect
from flask_bootstrap import Bootstrap


class UiDecorator(object):
    def __init__(self):
        pass

    def __call__(self, app):
        @app.route('/ui/')
        def ui():
            return render_template('ui.html')

        @app.route('/')
        def main_page():
            return redirect('/ui/')


class ApiDecorator(object):
    def __init__(self, handler):
        self.handler = handler

    def __call__(self, app):
        @app.route('/api', methods=["POST"])
        def api():
            data = request.get_json(force=True)
            result = self.handler.handle(data)
            return jsonify(result)


class BootstrapDecorator(object):
    def __init__(self):
        pass

    def __call__(self, app):
        return Bootstrap(app)

