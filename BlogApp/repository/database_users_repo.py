import psycopg2
from werkzeug.security import  generate_password_hash
from models.user import User
from setup.db_operations import DbOperations
from repository.users_repo import UsersRepo


class DatabaseUsersRepo(UsersRepo):
    db_operations = DbOperations()

    def find_by_id(self, pid):
        try:
            cur = self.db_operations.get_cursor()
            sql = "SELECT * FROM users WHERE user_id=%s"
            cur.execute(sql, (pid,))
            row = cur.fetchone()
            user = User.get_user(row)
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()
        return user

    def check_user_exists(self, email):
        try:
            cur = self.db_operations.get_cursor()
            sql = "SELECT * FROM users WHERE email = %s"
            cur.execute(sql, (email,))
            row = cur.fetchone()
            user = User.get_user(row)
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()
        return user

    def edit(self, user):
        sql = """UPDATE users
                    SET name=%s, email=%s,
                    password=%s,
                    created_at=%s,
                    modified_at=%s
                    WHERE user_id=%s"""
        record_to_update = (user.name, user.email, user.password,
                            user.created_at, user.modified_at, user.user_id)
        try:
            cur = self.db_operations.get_cursor()
            cur.execute(sql, record_to_update)
            conn = self.db_operations.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()

    def delete(self, pid):
        try:
            cur = self.db_operations.get_cursor()
            sql = "DELETE FROM users WHERE user_id=%s"
            cur.execute(sql, (pid, ))
            conn = self.db_operations.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()
                #generate_password_hash(user.password)
    def add(self, user):
        sql = """INSERT INTO users(name, email, password,
                        created_at,modified_at)
                 VALUES(%s,%s,%s,%s,%s) RETURNING user_id;"""
        record_to_insert = (user.name, user.email, user.password,
                            user.created_at, user.modified_at)
        user_id = None
        try:
            cur = self.db_operations.get_cursor()
            cur.execute(sql, record_to_insert)
            user_id = cur.fetchone()[0]
            conn = self.db_operations.conn
            conn.commit()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()
        return user_id

    def view_all(self):
        users = []
        try:
            cur = self.db_operations.get_cursor()
            cur.execute("SELECT * FROM users")
            row = cur.fetchone()
            while row is not None:
                user = User.get_user(row)
                users.append(user)
                row = cur.fetchone()
            cur.close()
        except (ConnectionError, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.db_operations.conn is not None:
                self.db_operations.conn.close()
        return users
