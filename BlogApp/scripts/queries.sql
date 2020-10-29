CREATE TABLE IF NOT EXISTS posts (
        post_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        owner VARCHAR(255) NOT NULL,
        contents Text NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified_at DATE NULL
        );
insert into posts (title, owner, contents) values ('Ella','tia','dummy content') RETURNING post_id;
insert into posts (title, owner, contents) values ('Las Vegas','bob','dummy content');

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NULL,
    password TEXT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified_at DATE NULL);

INSERT INTO users(name) SELECT owner FROM posts;

ALTER TABLE posts ADD COLUMN owner_cp VARCHAR (64);

UPDATE posts SET owner_cp = owner;

ALTER TABLE posts DROP COLUMN owner;

ALTER TABLE posts ADD COLUMN owner INT NULL;

ALTER TABLE posts add constraint fk_owner foreign key(owner) 
REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE;

UPDATE posts p
SET    owner = u.user_id
FROM   users u
WHERE  p.owner_cp = u.name;

ALTER TABLE posts DROP COLUMN owner_cp;