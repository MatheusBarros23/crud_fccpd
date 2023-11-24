
CREATE TABLE IF NOT EXISTS teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    team_id INTEGER REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS games (
    id SERIAL PRIMARY KEY,
    team_id_home INTEGER REFERENCES teams(id) ON DELETE CASCADE,
    team_id_away INTEGER REFERENCES teams(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    location VARCHAR(100) NOT NULL
);

INSERT INTO teams (name) VALUES
    ('Team D'),
    ('Team E'),
    ('Team F');

INSERT INTO players (name, team_id) VALUES
    ('Player 1', 1),
    ('Player 2', 1),
    ('Player 3', 2),
    ('Player 4', 2),
    ('Player 5', 3),
    ('Player 6', 3);

INSERT INTO games (team_id_home, team_id_away, date, location) VALUES
    (1, 2, '2022-01-01', 'Location 1'),
    (1, 3, '2022-01-02', 'Location 2'),
    (2, 3, '2022-01-03', 'Location 3'),
    (2, 1, '2022-01-04', 'Location 4'),
    (3, 1, '2022-01-05', 'Location 5'),
    (3, 2, '2022-01-06', 'Location 6');
