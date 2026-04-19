from flask import Flask, render_template

from bpClientes import bpClientes
from bpProductos import bpProductos
import bpProductos


app = Flask(__name__)

app.register_blueprint(bpClientes)
app.register_blueprint(bpProductos)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)