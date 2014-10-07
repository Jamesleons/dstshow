drop table if exists dstshow;
create table dstshow (
  id integer primary key autoincrement,
  processed int not null,
  unprocessed int not null
);
