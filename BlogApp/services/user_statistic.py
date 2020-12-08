class UserStatistic:
    @staticmethod
    def get_user_posts(posts):
        statistics = {}

        for post in posts:
            get_date = post.created_at.split(' ')
            key = (get_date[2], get_date[1])
           
            if key in statistics:
              statistics[key].append(post)
            else:
              statistics[key] = [post]
        return statistics
