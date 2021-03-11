CREATE TABLE `User` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`handle` VARCHAR(255) NOT NULL UNIQUE,
	`email` VARCHAR(255) NOT NULL UNIQUE,
	`password` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Question` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`uid` INT NOT NULL,
	`title` TEXT NOT NULL,
	`body` TEXT NOT NULL,
	`dop` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Tag` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`tag` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `QuesTag` (
	`qid` INT NOT NULL,
	`tid` INT NOT NULL
);

CREATE TABLE `Answer` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`uid` INT NOT NULL,
	`answer` TEXT NOT NULL,
	`votes` INT NOT NULL,
	`doa` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `QuesAns` (
	`qid` INT NOT NULL,
	`aid` INT NOT NULL
);

CREATE TABLE `AnsVote` (
	`uid` INT NOT NULL,
	`aid` INT NOT NULL,
	`status` INT NOT NULL
);

ALTER TABLE `Question` ADD CONSTRAINT `Question_fk0` FOREIGN KEY (`uid`) REFERENCES `User`(`id`);

ALTER TABLE `Answer` ADD CONSTRAINT `Answer_fk0` FOREIGN KEY (`uid`) REFERENCES `User`(`id`);

ALTER TABLE `QuesTag` ADD CONSTRAINT `QuesTag_fk0` FOREIGN KEY (`qid`) REFERENCES `Question`(`id`);

ALTER TABLE `QuesTag` ADD CONSTRAINT `QuesTag_fk1` FOREIGN KEY (`tid`) REFERENCES `Tag`(`id`);

ALTER TABLE `QuesAns` ADD CONSTRAINT `QuesAns_fk0` FOREIGN KEY (`qid`) REFERENCES `Question`(`id`);

ALTER TABLE `QuesAns` ADD CONSTRAINT `QuesAns_fk1` FOREIGN KEY (`aid`) REFERENCES `Answer`(`id`);

ALTER TABLE `AnsVote` ADD CONSTRAINT `AnsVote_fk0` FOREIGN KEY (`uid`) REFERENCES `User`(`id`);

ALTER TABLE `AnsVote` ADD CONSTRAINT `AnsVote_fk1` FOREIGN KEY (`aid`) REFERENCES `Answer`(`id`);

