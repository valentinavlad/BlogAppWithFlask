from itertools import islice

class UserStatistic:
    def __init__(self, posts):
        self.posts = posts

    def get_user_posts(self):
        statistics = {}
        for post in self.posts:
            get_date = post.created_at.split(' ')
            key = (get_date[2], get_date[1])
           
            if key in statistics:
              statistics[key].append(post)
            else:
              statistics[key] = [post]
        return statistics

    def get_all(self, records_per_page=3, offset=0):
        posts_dict = self.get_user_posts()
        posts = dict(islice(posts_dict.items(), offset, records_per_page + offset))
      
        return posts
