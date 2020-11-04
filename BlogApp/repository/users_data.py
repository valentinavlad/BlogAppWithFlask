from werkzeug.security import generate_password_hash
from models.user import User

password = generate_password_hash('123')
user_one = User(name='maia', email='maia@gmail.com', password=password)
user_one.created_at = 'January 6, 2018'
user_one.modified_at = 'January 8, 2018'
user_one.user_id = 2

user_two = User(name='tia', email='tia@gmail.com', password=password)
user_two.created_at = 'May 6, 2017'
user_two.modified_at = 'January 9, 2018'
user_two.user_id = 1

user_three = User(name='admin', email='admin@gmail.com', password=password)
user_three.created_at = 'May 6, 2017'
user_three.modified_at = 'January 9, 2018'
user_three.user_id = 3

user_four = User(name='bobby', email='bobby@gmail.com', password=password)
user_four.created_at = 'May 6, 2017'
user_four.modified_at = 'January 9, 2018'
user_four.user_id = 4

user_five = User(name='kolo', email='kolo@gmail.com', password=password)
user_five.created_at = 'May 6, 2017'
user_five.modified_at = 'January 9, 2018'
user_five.user_id = 5

user_six = User(name='ben', email='ben@gmail.com', password=password)
user_six.created_at = 'May 6, 2017'
user_six.modified_at = 'January 9, 2018'
user_six.user_id = 6

user_seven = User(name='goia', email='', password=None)
user_seven.created_at = 'May 6, 2017'
user_seven.modified_at = 'January 9, 2018'
user_seven.user_id = 7

user_eight = User(name='marc', email='marc@gmail.com', password=password)
user_eight.created_at = 'May 6, 2017'
user_eight.modified_at = 'January 9, 2018'
user_eight.user_id = 8

dummy_users = [user_one, user_two, user_three, user_four,\
              user_five, user_six, user_seven, user_eight]
