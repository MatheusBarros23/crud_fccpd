
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
    ('Nautico'),
    ('Sport'),
    ('Santa Cruz'),
    ('Petrolina'),
    ('Salgueiro'),
    ('Retro');

INSERT INTO players (name, team_id) VALUES
    ('André Silva', 1),    
    ('Bruna Oliveira', 1),
    ('Carlos Oliveira', 1),
    ('Camila Souza', 1),
    ('Diego Lima', 1),
    ('Gustavo Santos', 2),
    ('Gabriela Oliveira', 2),
    ('Henrique Silva', 2),
    ('Heloísa Lima', 2),
    ('Igor Souza', 2),
    ('Lucas Oliveira', 3),
    ('Larissa Souza', 3),
    ('Marcelo Silva', 3),
    ('Mariana Lima', 3),
    ('Natan Santos', 3),
    ('Rafael Oliveira', 4),
    ('Renata Souza', 4),
    ('Samuel Lima', 4),
    ('Sofia Santos', 4),
    ('Thiago Oliveira', 4),
    ('Xavier Santos', 5),
    ('Ximena Oliveira', 5),
    ('Yago Lima', 5),
    ('Yasmin Souza', 5),
    ('Zé Silva', 5),
    ('Ubirajara Oliveira', 6),
    ('Walter Lima', 6),
    ('Wesley Oliveira', 6),
    ('Xena Souza', 6),
    ('Xavier Lima', 6);

INSERT INTO games (team_id_home, team_id_away, date, location) VALUES
    (1, 2, '2022-01-01', 'Aflitos'),
    (1, 3, '2022-01-02', 'Aflitos'),
    (2, 3, '2022-01-03', 'Ilha do Retiro'),
    (2, 1, '2022-01-04', 'Ilha do Retiro'),
    (3, 1, '2022-01-05', 'Arruda'),
    (3, 2, '2022-01-06', 'Arruda'),
    (4, 1, '2022-01-07', 'Paulo Coelho'),    
    (4, 2, '2022-01-08', 'Paulo Coelho'),    
    (5, 3, '2022-01-09', 'Cornelio de Barros'),   
    (5, 1, '2022-01-10', 'Cornelio de Barros'), 
    (6, 3, '2022-01-11', 'Arena de Pernambuco'),   
    (6, 2, '2022-01-12', 'Arena de Pernambuco'),
    (4, 5, '2022-01-01', 'Paulo Coelho'),
    (4, 6, '2022-01-02', 'Paulo Coelho'),
    (5, 6, '2022-01-03', 'Cornelio de Barros'),
    (5, 4, '2022-01-04', 'Cornelio de Barros'),
    (6, 4, '2022-01-05', 'Arena de Pernambuco'),
    (6, 5, '2022-01-06', 'Arena de Pernambuco'); 
