CREATE TABLE games (
    id SERIAL PRIMARY KEY
);

CREATE TABLE rounds (
    id SERIAL PRIMARY KEY,      -- Auto-incrementing primary key
    game_id INT REFERENCES games(id),     -- String column, required
    round_number INT NOT NULL,      -- String column, required
    asker INT NOT NULL,  -- Unique and required email address
    helper INT NOT NULL,            -- Optional phone number
    person VARCHAR(15) NOT NULL,             -- Required date
    weapon VARCHAR(11) NOT NULL,  -- Foreign key referencing a 'jobs' table
    room VARCHAR(13) NOT NULL, -- Numeric column with constraint
    card VARCHAR(15)                  -- Optional department ID
);

INSERT INTO games DEFAULT VALUES;
INSERT INTO rounds (game_id, round_number, asker, helper, person, weapon, room, card)
VALUES
    (1,1,0,1,'MISS_SCARLETT','SPANNER','DINING_ROOM','SPANNER'),
    (1,2,1,3,'MISS_SCARLETT','CANDLESTICK','STUDY',NULL),
    (1,3,2,3,'PROFESSOR_PLUM','LEAD_PIPE','LIBRARY',NULL),
    (1,4,3,0,'MISS_SCARLETT','CANDLESTICK','LIBRARY',NULL),
    (1,5,0,1,'MISS_SCARLETT','CANDLESTICK','DINING_ROOM','DINING_ROOM'),
    (1,6,1,0,'MISS_SCARLETT','LEAD_PIPE','STUDY',NULL),
    (1,7,2,3,'COLONEL_MUSTARD','REVOLVER','LIBRARY',NULL),
    (1,8,3,0,'REVEREND_GREEN','LEAD_PIPE','LOUNGE',NULL),
    (1,9,0,1,'MISS_SCARLETT','REVOLVER','BALLROOM','MISS_SCARLETT');