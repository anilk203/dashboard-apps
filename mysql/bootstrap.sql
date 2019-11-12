create database configuration_database; 
create table database_configurations(id int not null auto_increment, name varchar(100) unique, value varchar(256), primary key(id));
 