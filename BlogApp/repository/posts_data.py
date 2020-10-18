from models.post import Post

post_one = Post(title='Python',
                contents="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor.Lorem ipsum dolor sit amet, 
                    consectetuer adipiscing elit.Lorem ipsum dolor sit amet,
                    consectetuer adipiscing elit.""")
post_one.created_at = 'January 6, 2018'
post_one.modified_at = 'January 8, 2018'
post_one.owner ='D.B.Higgins'

dummy_posts = [post_one]
dummy_posts.sort(key=lambda x: x.created_at, reverse=True)
