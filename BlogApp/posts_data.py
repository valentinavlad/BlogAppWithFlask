from post import Post

post_one = Post(title='Python', owner= 'D.B.Higgins',
                    contents='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
                    created_at='2020, September, 20',
                    modified_at='2020, September, 22')

post_two = Post(title='Php', owner= 'D.B.Poppask',
                    contents='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
                    created_at='2020, September, 10',
                    modified_at='2020, September, 23')
post_three = Post(title='Java', owner= 'D.B.Goliloaw',
                    contents='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
                    created_at='2020, April, 20',
                    modified_at='2020, September, 20')
post_four = Post(title='Javascript', owner= 'D.B.Poppask',
                    contents='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.',
                    created_at='2020, May, 20',
                    modified_at='2020, September, 22')

dummy_posts = [ post_one, post_two, post_three, post_four ]