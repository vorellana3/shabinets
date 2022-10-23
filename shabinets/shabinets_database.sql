drop database if exists shabinets;
create database if not exists shabinets;
use shabinets;

create table food (
	id INT not null AUTO_INCREMENT,
    food_name varchar(100) not null,
    units varchar(100) not null,
    primary key (id)
);

create table recipes (
	id INT not null AUTO_INCREMENT,
    recipe_name VARCHAR(1024) not null,
    pic_link VARCHAR(1024),
    instructions_link VARCHAR(1024),
    primary key (id),
);

create table recipe_ingredient (
    id INT not null AUTO_INCREMENT,
	food_id INT not null,
    recipe_id INT not null,
    amount FLOAT,
    display_line VARCHAR(1024) not null,
    primary key (id)
);

create table user_food (
	id INT not null AUTO_INCREMENT,
    food_id INT not null,
    bought_date DATE,
    expire_date DATE,
    amount FLOAT,
    primary key (id)
);

insert into food (food_name, units)
values ("salt", "pounds"),
("quartz", "milligrams"),
("diamond", "carats"),
("milk", "gallons"),
("water", "gallons"),
("ink", "ounces"),
("food color", "packets"),
("steak", "pounds"),
("sugar", "pounds"),
("cream", "cups"),
("lox", "ounces");

insert into recipes (recipe_name, pic_link, instructions_link)
values ("Rocks", NULL, "https://hrhr.dev"),
("God's Blood", "https://upload.wikimedia.org/wikipedia/commons/6/63/European_bee-eaters_%28Merops_apiaster%29_with_dragonflies.jpg", "https://en.wikipedia.org/wiki/Theophagy"),
("Caramel", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Odin%27s_last_words_to_Baldr.jpg/800px-Odin%27s_last_words_to_Baldr.jpg", "https://www.twopeasandtheirpod.com/brown-butter-salted-caramel-snickerdoodles/"),
("Really Big Steak", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Miensk%2C_Vysoki_Rynak%2C_Radzivi%C5%82._%D0%9C%D0%B5%D0%BD%D1%81%D0%BA%2C_%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D1%96_%D0%A0%D1%8B%D0%BD%D0%B0%D0%BA%2C_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%281901-10%29.jpg/1920px-Miensk%2C_Vysoki_Rynak%2C_Radzivi%C5%82._%D0%9C%D0%B5%D0%BD%D1%81%D0%BA%2C_%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D1%96_%D0%A0%D1%8B%D0%BD%D0%B0%D0%BA%2C_%D0%A0%D0%B0%D0%B4%D0%B7%D1%96%D0%B2%D1%96%D0%BB_%281901-10%29.jpg", "https://google.com"),
("The Favorite Meal of the Premier", "https://upload.wikimedia.org/wikipedia/commons/7/7b/Mienski_Teatar2.jpg", NULL);

insert into recipe_ingredient (recipe_id, food_id, amount, display_line)
values (1,1,1,"yummy yummy salt"),
values (1,2,.33,"pretty pretty quartz"),
values (1,3,.01,"and a sprinkle of diamond"),
values (3,4,.5,"a splash of milk"),
values (3,10,1,"cream for thickening"),
values (3,9,1,"sugar, rocky"),
values (2,7,3,"make it really red"),
values (2,8,1,"yeah it has steak in it too"),
values (4,8,1,"just a really big steak, nothing else"),
values (5,11,"salmon, my favorite -- stalin");

insert into user_food (food_id, expire_date, amount)
values (1, 1, '2023-01-04', 3),
values (2, 8, '2022-01-01', 1),
values (3, 11, '2022-10-25', 11);
