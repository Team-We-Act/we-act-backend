DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS board ;

CREATE TABLE `tb_user` (
    `user_ID` INTEGER PRIMARY KEY AUTOINCREMENT,
    `user_name` TEXT NOT NULL,
    `userType` TEXT NOT NULL,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `tb_class` (
    `class_ID` INTEGER PRIMARY KEY AUTOINCREMENT,
    `class_name` TEXT ,
    `country_name` TEXT,
    `language` TEXT,
    `duration` TEXT,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
);

CREATE TABLE `tb_lecture` (
    `lectureID` INTEGER PRIMARY KEY AUTOINCREMENT,
    `classID` INTEGER NOT NULL,
    `title` TEXT not null   ,
    `description` TEXT NOT NULL,
    FOREIGN KEY (classID) REFERENCES tb_class(classID)
);

