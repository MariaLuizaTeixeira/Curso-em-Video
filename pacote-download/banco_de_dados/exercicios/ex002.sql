/* EXERCICIO 01 */
select profissao, count(*) from gafanhotos
group by profissao;

/* EXERCICIO 02 */
select count(nascimento) from gafanhotos
where nascimento > '2005-01-01';

/* EXERCICIO 03 */
select nacionalidade, count(*) from gafanhotos
where not nacionalidade = 'Brasil'
group by nacionalidade
having count(nacionalidade) > 3
order by count(*);

/* EXERCICIO 04 */
select nome, peso, altura from gafanhotos
where peso > '100'
group by nome, peso, altura
having altura >(select avg(altura) from gafanhotos);