drop table if exists dstshow;
create table dstshow (
  id integer primary key autoincrement,
  ptime string not null,
  username string not null,
  reply string not null
);
