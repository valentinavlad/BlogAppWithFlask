from app import db
from models.post import Post
from repository.posts_repo import PostsRepo

class DbPostsRepoSqlalchemy(PostsRepo):
    
    def find_by_id(self, pid):
        try:
            cur = self.db_connect.get_cursor()
            sql = 'SELECT post_id, title, owner, name, contents, posts.created_at,\
                   posts.modified_at FROM posts INNER JOIN users\
                   ON owner = user_id WHERE post_id=%s'
            cur.execute(sql, (pid,))
            row = cur.fetchone()
            post = Post.get_post(row)
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()
        return post

    def edit(self, post):
        sql = """UPDATE posts
                    SET title=%s, owner=%s,
                    contents=%s,
                    created_at=%s,
                    modified_at=%s
                    WHERE post_id=%s"""
        record_to_update = (post.title, session['user_id'], post.contents,
                            post.created_at, post.modified_at, post.post_id)
        try:
            cur = self.db_connect.get_cursor()
            cur.execute(sql, record_to_update)
            conn = self.db_connect.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()

    def delete(self, pid):
        db.session.delete(pid)
        db.session.commit()

    def add(self, post):
        db.session.add(post)
        db.session.commit()

    def get_all(self, owner_id=0, records_per_page='all', offset=0):
        posts = []
        where_clause = "WHERE posts.owner = {}" if owner_id != 0 else " "
        check_owner = where_clause.format(owner_id)
        sql = """SELECT post_id, title, owner, name, contents, posts.created_at,
                            posts.modified_at FROM posts INNER JOIN users 
                            ON owner = user_id 
							{}
							ORDER BY created_at desc
							LIMIT {} OFFSET {};"""
        try:
            cur = self.db_connect.get_cursor()

            cur.execute(sql.format(check_owner, records_per_page, offset))
            rows = cur.fetchall()
            for row in rows:
                post = Post.get_post(row)
                posts.append(post)
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_connect.conn is not None:
                self.db_connect.conn.close()

        return posts

    def get_count(self, owner_id=0):
        where_clause = ' where posts.owner = {}' if owner_id != 0 else " "
        check_owner = where_clause.format(owner_id)
        sql = "SELECT count(*) from posts {};"
        cur = self.db_connect.get_cursor()
        cur.execute(sql.format(check_owner))
        row = cur.fetchone()
        cur.close()

        return row[0]



