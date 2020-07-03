USE bd_endereco;
CREATE TABLE ENDERECO(
	cep VARCHAR(8) NOT NULL,
    logradouro VARCHAR(45) NOT NULL,
    bairro VARCHAR(45) NOT NULL,
    numero INT NOT NULL,
    cidade VARCHAR(45) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    complemento VARCHAR(45),
    descricao VARCHAR(100),
    PRIMARY KEY (cep)
);
SHOW tables;