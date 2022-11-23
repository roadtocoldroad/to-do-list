DROP TABLE IF EXISTS todo;

CREATE TABLE "todo" (
    "todo_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "title" text,
    "completed" bool default false,
    "url" text)