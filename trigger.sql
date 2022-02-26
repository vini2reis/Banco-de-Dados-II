CREATE OR REPLACE FUNCTION verifica_sal() RETURNS TRIGGER AS $$
	DECLARE
		menor decimal(10,2);
		maior decimal(10,2);
	BEGIN
		select min(salario) into menor from empregado;
		select max(salario) into maior from empregado;
		IF (NEW.salario < menor) THEN
			RAISE EXCEPTION 'O salario de % não pode ser menor que %', NEW.nome, menor;
		ELSIF (NEW.salario > maior) THEN
			RAISE EXCEPTION 'O salario de % não pode ser maior que %', NEW.nome, maior;
		ELSE 
			RETURN NEW;
		END IF;
		RETURN NULL;
	END;
$$ LANGUAGE "plpgsql";


CREATE TRIGGER ver_sal BEFORE INSERT ON empregado
FOR EACH ROW EXECUTE PROCEDURE verifica_sal();