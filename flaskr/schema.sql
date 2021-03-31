DROP TABLE IF EXISTS tb_user;
DROP TABLE IF EXISTS tb_class;
DROP TABLE IF EXISTS tb_lecture;


CREATE TABLE tb_user (
    user_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    userType TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `tb_class` (
    `class_ID` INTEGER PRIMARY KEY AUTOINCREMENT,
    `user_ID` INTEGER,
    `class_name` TEXT ,
    `country_name` TEXT,
    `language` TEXT,
    `duration` TEXT,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
     constraint fk_teaches FOREIGN KEY (user_ID) REFERENCES tb_user(user_ID)
     ON DELETE NO ACTION,
       constraint fk_takes FOREIGN KEY (user_ID) REFERENCES tb_user(user_ID)
     ON DELETE NO ACTION
);

CREATE TABLE `tb_lecture` (
    `lecture_ID` INTEGER PRIMARY KEY AUTOINCREMENT,
    `class_ID` INTEGER NOT NULL,
    `title` TEXT not null   ,
    `file` BLOB, 
    `contents` TEXT,
    `description` TEXT NOT NULL,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
    FOREIGN KEY (class_ID) REFERENCES tb_class(class_ID) ON DELETE NO ACTION
);