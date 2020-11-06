CREATE TABLE IF NOT EXISTS posts (
        post_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        owner VARCHAR(255) NOT NULL,
        contents Text NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified_at DATE NULL);

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NULL,
    password TEXT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified_at DATE NULL);

INSERT INTO users (name) SELECT 'admin' WHERE not exists (
    select 1 from users where name = 'admin');

INSERT INTO users(name) SELECT DISTINCT owner FROM posts 
WHERE EXISTS (SELECT data_type FROM information_schema.columns
WHERE table_name = 'posts' AND column_name = 'owner' AND data_type = 'character varying');

UPDATE posts set owner=users.user_id from users where posts.owner::varchar = users.name;

ALTER TABLE posts ALTER COLUMN owner TYPE INT USING owner::integer;

ALTER TABLE POSTS DROP CONSTRAINT IF EXISTS fk_owner;

ALTER TABLE posts add constraint fk_owner foreign key(owner) 
REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE;