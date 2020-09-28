import datetime
from flask import request
from repository.posts_data import dummy_posts
from models.post import Post
from repository.interface_repo import InterfaceRepo

class InMemoryDb(InterfaceRepo):
    """description of class"""
    def __init__(self):
        pass
    def find_post_id(self, pid):
        found_post = None
        for post in dummy_posts:
            if post.post_id == pid:
                found_post = post
        return found_post    
    def view_posts(self):
        return dummy_posts
    def edit(self, pid):
        found_post= None
        found_post = self.find_post_id(pid)
        if found_post is not None:
            date_now = datetime.datetime.now()
            post = Post(title=request.form.get("title"),owner= request.form.get("owner"),
                        contents=request.form.get("contents"))
            post.created_at = date_now.strftime("%B %d, %Y")
            post.modified_at = date_now.strftime("%B %d, %Y")
            dummy_posts.remove(found_post)
            dummy_posts.insert(0, post)
            return found_post     
        return None
    def delete(self, found_post, pid):
        found_post = self.find_post_id(pid)  
        dummy_posts.remove(found_post)
    def add(self):
        date_now = datetime.datetime.now()
        post = Post(title=request.form.get("title"),owner= request.form.get("owner"),
                    contents=request.form.get("contents"))
        post.created_at = date_now.strftime("%B %d, %Y")
        post.modified_at = date_now.strftime("%B %d, %Y")
        dummy_posts.insert(0, post)


    