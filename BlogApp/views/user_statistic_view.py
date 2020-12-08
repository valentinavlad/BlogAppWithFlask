from injector import inject
from datetime import datetime
from flask import Blueprint, render_template, session, request, url_for
from utils.setup_decorators import is_config_file
from utils.authorization import login_required
from services.user_statistic import UserStatistic
from repository.posts_repo import PostsRepo
from functionality.pagination import Pagination


user_statistic_blueprint = Blueprint('user_statistic', __name__,\
   template_folder='templates', static_folder='static')

@inject
@user_statistic_blueprint.route('/', methods=['GET'])
@is_config_file
@login_required
def get_statistic(repo: PostsRepo, user_stat: UserStatistic):
    owner_id = 0 if session.get("user_id") is None else int(session['user_id'])

    count_posts = repo.get_count(owner_id)

    all_posts = repo.get_all(owner_id, count_posts, 0)

    user_posts = user_stat.get_user_posts(all_posts)
    
    return render_template('user_statistic.html', data=user_posts)
