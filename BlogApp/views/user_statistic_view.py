from injector import inject
from flask import Blueprint, render_template, request, url_for
from utils.setup_decorators import is_config_file
from utils.authorization import login_required
from services.user_statistic import UserStatistic
from functionality.pagination import Pagination


user_statistic_blueprint = Blueprint('user_statistic', __name__,\
   template_folder='templates', static_folder='static')

@inject
@user_statistic_blueprint.route('/', methods=['GET'])
@is_config_file
@login_required
def get_statistic(user_stat: UserStatistic):
    page = request.args.get('page', 1, type=int)
    user_posts = user_stat.get_user_posts()

    pagination = Pagination(page, len(user_posts))
    posts = user_stat.get_all(pagination.records_per_page, pagination.offset)
    next_url = url_for('user_statistic.get_statistic', page=str(pagination.next_page)) \
                   if pagination.has_next() else None
    prev_url = url_for('user_statistic.get_statistic', page=str(pagination.prev_page)) \
                   if pagination.has_prev() else None

    return render_template('user_statistic.html', data=posts, \
        next_url=next_url, prev_url=prev_url)
