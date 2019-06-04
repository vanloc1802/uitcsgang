from flask import Flask, render_template, request, send_from_directory, redirect, url_for, send_file
import os
from searching import searchEngine

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/.well-known/pki-validation/<filename>")
def send_ssl(filename):
    return send_file(filename)

@app.route("/")
def index():
    q = request.args.get("query")
    if q == '' or q is None:
        render_template('index.html')
    return render_template('index.html', value=q)


@app.route("/image/<filename>")
def send_image(filename):
    return send_from_directory("dataset", filename)


@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        query = request.form['query']
    else:
        query = request.args.get("query")
    if query == '' or query is None:
        return redirect(url_for('index'))
    else:
        images = searchEngine(query)
        return render_template('search.html', value=query, images=images)


if __name__ == '__main__':
    app.run(debug=False)
