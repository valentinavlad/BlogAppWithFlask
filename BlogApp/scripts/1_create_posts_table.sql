CREATE TABLE IF NOT EXISTS posts (
        post_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        owner VARCHAR(255) NOT NULL,
        contents Text NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified_at DATE NULL
        );
insert into posts (title, owner, contents) values ('99','tia','dummy content');
insert into posts (title, owner, contents) values ('Las Vegas','bob','dummy content');