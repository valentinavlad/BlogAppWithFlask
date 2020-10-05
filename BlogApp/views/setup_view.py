from flask import Blueprint, render_template

setup_blueprint = Blueprint('setup_blueprint', __name__, template_folder='templates',
                            static_folder='static')

@setup_blueprint.route('/', methods=['GET', 'POST'])
def setup():
     return render_template('setup.html')