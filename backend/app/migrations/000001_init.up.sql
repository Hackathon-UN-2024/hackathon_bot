CREATE TABLE IF NOT EXISTS histories (
    id SERIAL PRIMARY KEY,
    user_message TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    feedback BOOLEAN,
    timestamp TIMESTAMP(0) WITHOUT TIME ZONE NULL DEFAULT NOW()
);