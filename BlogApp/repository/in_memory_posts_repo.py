from itertools import islice
from injector import inject
from werkzeug.datastructures import FileStorage
from repository.posts_data import dummy_posts
from repository.users_data import dummy_users
from repository.image_data import dummy_image
from repository.posts_repo import PostsRepo
from repository.in_memory_users_repo import InMemoryUsersRepo
from repository.in_memory_image_repo import InMemoryImageRepo

DEFAULT_IMG = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HA"\
                  "wCAAAAC0lEQVR42mNkMAYAADkANVKH3ScAAAAASUVORK5CYII="
class InMemoryPostsRepo(PostsRepo):
    @inject
    def __init__(self, user_repo: InMemoryUsersRepo, db_image: InMemoryImageRepo):
        self.user_repo = user_repo
        self.db_image = db_image

    def find_by_id(self, pid):
        found_post = None
        for post in dummy_posts:
            if post.post_id == pid:
                found_post = post
        found_post.name = self.user_repo.find_by_id(int(found_post.owner)).name
        return found_post

    def get_all(self, owner_id=0, records_per_page=3, offset=0):
        if owner_id > 0:
            posts_by_owner = []
            for post in dummy_posts:
                if int(post.owner) == owner_id:
                    if not isinstance(post.created_at, str):
                        post.created_at = post.created_at.strftime("%d %B %Y")
                    post.img = self.db_image.get(post.img_id)
                    posts_by_owner.append(post)
            return list(islice(posts_by_owner, offset, records_per_page + offset))

        posts = list(islice(dummy_posts, offset, records_per_page + offset))

        for post in posts:
            post.img = self.db_image.get(post.img_id)
            if not isinstance(post.created_at, str):
                post.created_at = post.created_at.strftime("%d %B %Y")
            for user in dummy_users:
                if int(post.owner) == user.user_id:
                    post.name = user.name
        return posts

    def edit(self, post):
        index = dummy_posts.index(post)
        if isinstance(post.img, FileStorage):
            img_list = self.db_image.edit(post.img_id, post.img)
            post.img = img_list[1]
            post.img_id = img_list[0]
        dummy_posts[index] = post

    def delete(self, pid):
        post = self.find_by_id(pid)
        img_id = post.img_id
        dummy_posts.remove(post)
        self.db_image.delete(img_id)

    def add(self, post):
        if post.img.filename == '':
            img_list = ['id0', DEFAULT_IMG]
            dummy_image.insert(0, img_list)
            post.img_id = img_list[0]
            post.img = img_list[1]

        else:
            img_list = self.db_image.add(post.img)
            post.img_id = img_list[0]
            post.img = img_list[1]
        dummy_posts.insert(0, post)

    def get_count(self, owner_id):
        if owner_id > 0:
            count = 0
            for post in dummy_posts:
                if int(post.owner) == owner_id:
                    count = count + 1
            return count
        return len(dummy_posts)
