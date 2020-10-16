from models.user import User

user_one = User(name='Maia', email='maia@gmail.com', password='123')
user_one.created_at = 'January 6, 2018'
user_one.modified_at = 'January 8, 2018'

user_two = User(name='Tia', email='tia@gmail.com', password='123')
user_two.created_at = 'May 6, 2017'
user_two.modified_at = 'January 9, 2018'

dummy_users = [user_one, user_two]
