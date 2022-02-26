CREATE TABLE PageRevision(name varchar, 
	date date,
	author varchar,
	texto text);

CREATE TABLE PageAudit(name varchar,
	data date,
	dif_len int);

CREATE OR REPLACE FUNCTION editawiki() RETURNS trigger as $$
	DECLARE
		i int;
		j int;
	BEGIN
		i = length(old.texto);
		j = length(NEW.texto);
		insert into PageAudit values (current_user, now(), (j-i));
		return NEW;
	END $$
LANGUAGE 'plpgsql';

CREATE TRIGGER edita BEFORE UPDATE ON PageRevision
FOR EACH ROW EXECUTE PROCEDURE editawiki();

insert into PageRevision values('BD', '15/03/2019', 'Vini', 'Muito dificil');
update pagerevision set texto = 'nao é nao';