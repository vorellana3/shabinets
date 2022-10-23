drop database if exists shabinets;
create database if not exists shabinets;
use shabinets;

create table food (
    food_name varchar(100) not null,
    units varchar(100) not null,
    primary key (food_name)
);

create table recipes (
	id INT not null AUTO_INCREMENT,
    recipe_name VARCHAR(1024) not null,
    pic_link VARCHAR(1024),
    instructions_link VARCHAR(1024),
    preference INT not null,
    primary key (id)
);

create table recipe_ingredient (
    id INT not null AUTO_INCREMENT,
	food_name VARCHAR(100) not null,
    recipe_id INT not null,
    amount FLOAT,
    display_line VARCHAR(1024) not null,
    primary key (id)
);

create table user_food (
	id INT not null AUTO_INCREMENT,
    food_name varchar(100) not null,
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

insert into recipe_ingredient (recipe_id, food_name, amount, display_line)
values (1,"salt",1,"yummy yummy salt"),
(1,"quartz",.33,"pretty pretty quartz"),
(1,"diamond",.01,"and a sprinkle of diamond"),
(3,"milk",.5,"a splash of milk"),
(3,"cream",1,"cream for thickening"),
(3,"sugar",1,"sugar, rocky"),
(2,"food color",3,"make it really red"),
(2,"steak",NULL,"yeah it has steak in it too"),
(4,"steak",NULL,"just a really big steak, nothing else"),
(5,"lox",1,"salmon, my favorite -- stalin");

insert into user_food (food_name, expire_date, amount)
values ("salt", '2023-01-04', 3),
("steak", '2022-01-01', 1),
("lox"'2022-10-25', 11);
