CREATE TABLE posts (
        post_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        owner VARCHAR(255) NOT NULL,
        contents Text NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified_at DATE NULL
        )