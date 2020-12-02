from flask import Blueprint, render_template

user_statistic_blueprint = Blueprint('user_statictic', __name__,\
   template_folder='templates', static_folder='static')


@user_statistic_blueprint.route('/', methods=['GET'])
def get_statistic():
    return render_template('user_statistic.html')
