create database Projeto;

create table Atletas(
Nome varchar(255) not null,
CPF varchar(11) primary KEY,
idade int unsigned not null,
modalidade varchar (255) not null
);

create table Coompeticoes(
Nome varchar(255) primary KEY,
local varchar(255) not null,
data date not null,
premio varchar(255) not null,
constraint fk_CPF foreign key(CPF)
	references Atletas (CPF)

);