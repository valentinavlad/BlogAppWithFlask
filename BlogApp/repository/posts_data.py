import datetime
from models.post import Post
from repository.image_data import dummy_image

post_one = Post(title='Python', owner='2',
                contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_one.created_at = datetime.datetime(2018, 1, 6)
#post_one.created_at = '06 January 6 2018'
post_one.modified_at = datetime.datetime(2018, 1, 8)
post_one.img_id = dummy_image[0][0]

post_two = Post(title='Php', owner='1',
                contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_two.created_at = datetime.datetime(2017, 12, 10)
post_two.modified_at = datetime.datetime(2017, 12, 15)
post_two.img_id = dummy_image[1][0]

post_three = Post(title='Java', owner='2',
                  contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet, consectetuer 
                    adipiscing elit.Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Lorem ipsum dolor sit amet, consectetuer adipiscing elit.""")
post_three.created_at = datetime.datetime(2017, 12, 2)
post_three.modified_at = datetime.datetime(2018, 5, 2)
post_three.img_id = dummy_image[2][0]

post_four = Post(title='Javascript', owner='1',
                 contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor. Aenean commodo ligula eget dolor""")
post_four.created_at = datetime.datetime(2019, 6, 13)
post_four.modified_at = datetime.datetime(2019, 6, 15)
post_four.img_id = dummy_image[3][0]

post_five = Post(title='Angular', owner='2',
                 contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, 
                    tellus eget condimentum rhoncus, sem quam semper libero, 
                    sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id,
                    lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. 
                    Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. 
                    Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,
                    Aenean commodo ligula eget dolor.""")
post_five.created_at = datetime.datetime(2020, 3, 13)
post_five.modified_at = datetime.datetime(2020, 6, 13)
post_five.img_id = dummy_image[4][0]

post_six = Post(title='C++', owner='1',
                contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, 
                    tellus eget condimentum rhoncus, sem quam semper libero, 
                    sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id,
                    lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. 
                    Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. 
                    Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,
                    Aenean commodo ligula eget dolor.""")
post_six.created_at = datetime.datetime(2020, 3, 13)
post_six.modified_at = datetime.datetime(2020, 6, 8)
post_six.img_id = dummy_image[5][0]

post_seven = Post(title='Vue Js', owner='1',
                  contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_seven.created_at = datetime.datetime(2018, 1, 6)
post_seven.modified_at = datetime.datetime(2018, 1, 8)
post_seven.img_id = dummy_image[6][0]

post_eight = Post(title='Laravel', owner='2',
                  contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_eight.created_at = datetime.datetime(2018, 1, 6)
post_eight.modified_at = datetime.datetime(2018, 1, 8)
post_eight.img_id = dummy_image[7][0]

post_nine = Post(title='Ajax', owner='5',
                 contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_nine.created_at = datetime.datetime(2018, 1, 6)
post_nine.modified_at = datetime.datetime(2018, 1, 6)
post_nine.img_id = dummy_image[8][0]

post_ten = Post(title='Sql', owner='5',
                contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_ten.created_at = datetime.datetime(2015, 1, 6)
post_ten.modified_at = datetime.datetime(2020, 1, 8)
post_ten.img_id = dummy_image[9][0]

post_eleven = Post(title='MySql', owner='6',
                   contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_eleven.created_at = datetime.datetime(2012, 1, 6)
post_eleven.modified_at = datetime.datetime(2015, 1, 8)
post_eleven.img_id = dummy_image[10][0]

dummy_posts = [post_one, post_two, post_three, post_four, post_five,\
   post_six, post_seven, post_eight, post_nine, post_ten, post_eleven]
dummy_posts.sort(key=lambda x: x.created_at, reverse=True)
