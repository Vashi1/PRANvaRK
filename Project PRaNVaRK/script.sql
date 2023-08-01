create database PRaNVaRK;
use PRanVaRK;
create table Users(
	name char(255),
    role char(255)
    );
insert into Users values ('admin', 'ADMIN');
insert into Users values ('abc', 'USER');
grant all privileges on pranvark.* to 'raks'@localhost
create table stock(
	mname char(255),
    bname char(255),
    price int(255),
    quantity int(255)
);
select * from Users;
select user from mysql.user;
