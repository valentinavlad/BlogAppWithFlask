ALTER TABLE posts ADD COLUMN owner_cp VARCHAR (64);

UPDATE posts SET owner_cp = owner;

ALTER TABLE posts DROP COLUMN owner;

ALTER TABLE posts ADD COLUMN owner INT NULL;


ALTER TABLE posts add constraint fk_owner foreign key(owner) 
REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE;
