CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY ASC, name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS courses (
  id INTEGER PRIMARY KEY ASC, name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS saves (
  id INTEGER PRIMARY KEY ASC, user_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL, lesson_no INTEGER NOT NULL,
  exercise_no INTEGER NOT NULL, data TEXT,
  FOREIGN KEY(user_id) REFERENCES users(id),
  FOREIGN KEY(course_id) REFERENCES courses(id),
  CONSTRAINT user_ex_unique UNIQUE (user_id, course_id, lesson_no, exercise_no)
);
