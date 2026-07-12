-- create 'status' table.
-- depends: 
CREATE TABLE status (
  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name varchar UNIQUE NOT NULL
);

COMMENT ON TABLE status IS 'Справочник допустимых статусов задачи.';
COMMENT ON COLUMN status.id IS 'ID статуса задачи (Автогенерация).';
COMMENT ON COLUMN status.name IS 'Название статуса.';
