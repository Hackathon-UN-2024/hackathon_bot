CREATE TABLE IF NOT EXISTS histories (
    id SERIAL PRIMARY KEY,
    user_message VARCHAR(255) NOT NULL,
    bot_response VARCHAR(255) NOT NULL,
    feedback BOOLEAN,
    timestamp TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);