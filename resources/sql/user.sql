-- This table should be kept minimal and anything other than login credentials should be stored elsewhere.
-- The purpose is to prevent accidental modifications of user data because these don't change often.
CREATE TABLE app_user (
    id SERIAL PRIMARY KEY ,
    pid uuid DEFAULT uuid_generate_v4(),
    username VARCHAR(200) UNIQUE NOT NULL,  -- If an email login is used, then this should be replaced with generated name.
    password_hash VARCHAR(200) NOT NULL
);
