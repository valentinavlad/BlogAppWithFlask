from models.post import Post
post_one = Post(title='Python', owner='2',
                contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_one.created_at = 'January 6, 2018'
post_one.modified_at = 'January 8, 2018'
#post_one.name = 'maia'


post_two = Post(title='Php', owner='1',
                contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_two.created_at = 'December 10, 2017'
post_two.modified_at = 'December 15, 2017'
post_two.name = 'tia'
post_three = Post(title='Java', owner='2',
                  contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet, consectetuer 
                    adipiscing elit.Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Lorem ipsum dolor sit amet, consectetuer adipiscing elit.""")
post_three.created_at = 'December 2, 2017'
post_three.modified_at = 'May 2, 2018'
post_three.name = 'maia'
post_four = Post(title='Javascript', owner='1',
                 contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor. Aenean commodo ligula eget dolor""")
post_four.created_at = 'June 13, 2019'
post_four.modified_at = 'June 15, 2019'
post_four.name = 'tia'
post_five = Post(title='Angular', owner='2',
                 contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, 
                    tellus eget condimentum rhoncus, sem quam semper libero, 
                    sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id,
                    lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. 
                    Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. 
                    Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,
                    Aenean commodo ligula eget dolor.""")
post_five.created_at = 'March 13, 2020'
post_five.modified_at = 'June 13, 2020'
post_five.name = 'maia'
post_six = Post(title='C++', owner='1',
                contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, 
                    tellus eget condimentum rhoncus, sem quam semper libero, 
                    sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id,
                    lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. 
                    Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. 
                    Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,
                    Aenean commodo ligula eget dolor.""")
post_six.created_at = 'March 13, 2020'
post_six.modified_at = 'June 13, 2020'
post_six.name = 'tia'
post_seven = Post(title='Vue Js', owner='1',
                  contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_seven.created_at = 'January 6, 2018'
post_seven.modified_at = 'January 8, 2018'
post_seven.name = 'tia'
post_eight = Post(title='Laravel', owner='2',
                  contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_eight.created_at = 'January 6, 2018'
post_eight.modified_at = 'January 8, 2018'
post_eight.name = 'maia'
dummy_posts = [post_one, post_two, post_three, post_four, post_five,\
   post_six, post_seven, post_eight]
dummy_posts.sort(key=lambda x: x.created_at, reverse=True)
