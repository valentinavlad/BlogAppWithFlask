from models.post import Post

post_one = Post(title='Python', owner= 'D.B.Higgins',
                    contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""",created_at = 'January 6, 2018',
                    modified_at = 'January 8, 2018')
post_two = Post(title='Php', owner= 'D.B.Poppask',
                    contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""",created_at = 'December 10, 2017',
                    modified_at = 'December 15, 2017')
post_three = Post(title='Java', owner= 'D.B.Goliloaw',
                    contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet, consectetuer 
                    adipiscing elit.Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Lorem ipsum dolor sit amet, consectetuer adipiscing elit.""",created_at = 'December 2, 2017',
                    modified_at = 'May 2, 2018')
post_four = Post(title='Javascript', owner= 'D.B.Poppask',
                    contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor. Aenean commodo ligula eget dolor""",created_at = 'June 13, 2019',
                    modified_at = 'June 15, 2019')
post_five = Post(title='Angular', owner= 'V.W. Craig',
                    contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, 
                    tellus eget condimentum rhoncus, sem quam semper libero, 
                    sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id,
                    lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. 
                    Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. 
                    Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,
                    Aenean commodo ligula eget dolor.""",created_at = 'March 13, 2020',modified_at = 'June 13, 2020')
dummy_posts = [ post_one, post_two, post_three, post_four,post_five ]
dummy_posts.sort(key=lambda x: x.created_at, reverse=True)
