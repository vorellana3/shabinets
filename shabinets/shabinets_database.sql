drop database if exists shabinets;
create database if not exists shabinets;
use shabinets;

create table food (
	id decimal(9, 0) not null,
    food_name char(10) not null,
    units char(10) not null,
    primary key (id)
);

create table recipes (
	id decimal(9, 0) not null,
    recipe_name char(10) not null,
    primary key (id)
);

create table recipe_ingredient (
	food_id decimal(9,0) not null,
    recipe_id decimal(9, 0) not null,
    amount decimal(9,0) not null,
    primary key (food_id, recipe_id)
);

create table user_food (
	food_id decimal(9,0) not null,
    bought_date date not null,
    expire_date date,
    amount decimal(9,0) not null,
    primary key (food_id)
);

alter table recipes add column (
    preference decimal(9, 0) not null
);
