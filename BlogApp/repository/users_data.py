from models.user import User

user_one = User(name='Maia', email='maia@gmail.com', password='123')
user_one.created_at = 'January 6, 2018'
user_one.modified_at = 'January 8, 2018'
user_one.user_id = 2

user_two = User(name='Tia', email='tia@gmail.com', password='123')
user_two.created_at = 'May 6, 2017'
user_two.modified_at = 'January 9, 2018'
user_two.user_id = 1

user_three = User(name='admin', email='admin@gmail.com', password='123')
user_three.created_at = 'May 6, 2017'
user_three.modified_at = 'January 9, 2018'
user_three.user_id = 3

user_four = User(name='Bobby', email='bobyb@gmail.com', password='123')
user_four.created_at = 'May 6, 2017'
user_four.modified_at = 'January 9, 2018'
user_four.user_id = 4

user_five = User(name='Kolo', email='kolo@gmail.com', password='123')
user_five.created_at = 'May 6, 2017'
user_five.modified_at = 'January 9, 2018'
user_five.user_id = 5
dummy_users = [user_one, user_two, user_three, user_four, user_five]
