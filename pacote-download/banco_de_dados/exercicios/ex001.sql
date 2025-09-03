/* EXERCICIO  1*/
select * from gafanhotos
where sexo = 'F';

/* EXERCICIO  2*/
select * from gafanhotos
where nascimento between '2000-1-1' and '2015-12-31';

/* EXERCICIO  3*/
select * from gafanhotos
where sexo = 'M' and profissao = 'Programador';

/* EXERCICIO  4*/
select * from gafanhotos
where sexo = 'F' and nome like 'J%';

/* EXERCICIO  5*/
select nome, nacionalidade from gafanhotos
where sexo = 'M' and nome like '%Silva' and not nacionalidade = 'Brasil' and peso < '100'; 

/* EXERCICIO  6*/
select max(altura) from gafanhotos
where sexo = 'M' and nacionalidade = 'Brasil';

/* EXERCICIO  7*/
select avg(altura) from gafanhotos;

/* EXERCICIO  8*/
select min(peso) from gafanhotos
where sexo = 'F' and not nacionalidade = 'Brasil' and nascimento between '1990-01-01' and '2000-12-30';

/* EXERCICIO  9*/
select count(altura) from gafanhotos
where altura > '1.9' and sexo = 'F';