from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wiki/<path:filename>')
def wiki_files(filename):
    wiki_dir = os.path.join(app.static_folder, 'wiki')
    if os.path.isfile(os.path.join(wiki_dir, filename)):
        return send_from_directory(wiki_dir, filename)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)