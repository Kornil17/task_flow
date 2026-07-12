-- create 'user' table.
-- depends: 20260712_01_Mrkqq-create-status-table
CREATE TABLE users (
  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  username varchar NOT NULL,
  surname varchar NOT NULL,
  email varchar UNIQUE NOT NULL,
  role varchar NOT NULL,
  created_at timestamp DEFAULT (NOW()),
  updated_at timestamp DEFAULT (NOW()),
  deleted_at timestamp
);

CREATE UNIQUE INDEX ON users (email);
CREATE INDEX ON users (username);

COMMENT ON TABLE users IS 'Данные по зарегистрированным пользователям.';
COMMENT ON COLUMN users.id IS 'ID пользователя (Автогенерация).';
COMMENT ON COLUMN users.username IS 'Имя пользователя.';
COMMENT ON COLUMN users.surname IS 'Фамилия пользователя.';
COMMENT ON COLUMN users.email IS 'Почта пользователя.';
COMMENT ON COLUMN users.role IS 'Роль пользователя в системе.';
COMMENT ON COLUMN users.created_at IS 'Дата создания пользователя (Автогенерация).';
COMMENT ON COLUMN users.updated_at IS 'Дата обновления данных о пользователе (Автообновление).';
COMMENT ON COLUMN users.deleted_at IS 'Дата удаления пользователя.';
