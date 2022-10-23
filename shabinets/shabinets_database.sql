drop database if exists shabinets;
create database if not exists shabinets;
use shabinets;

create table food (
	id decimal(9, 0) not null,
    food_name char(10) not null,
    units char(10) not null,
    primary key (id)
) engine = innodb;

create table recipes (
	id decimal(9, 0) not null,
    recipe_name char(10) not null,
    primary key (id)
) engine = innodb;

create table recipe_ingredient (
	food_id decimal(9,0) not null,
    recipe_id decimal(9, 0) not null,
    amount decimal(9,0) not null,
    primary key (food_id, recipe_id)
) engine = innodb;

create table user_food (
	food_id decimal(9,0) not null,
    bought_date date not null,
    expire_date date,
    amount decimal(9,0) not null,
    primary key (food_id)
) engine = innodb;

alter table recipes add column (
    link varchar(1024) not null
)

alter table recipe_ingredient add column (
    display_line varchar(1024) not null
)