-- Banco de dados do sistema bancário
CREATE TABLE IF NOT EXISTS contas (
    id SERIAL PRIMARY KEY,
    numero_conta VARCHAR(20) UNIQUE NOT NULL,
    saldo DECIMAL(15,2) DEFAULT 0.00,
    status CHAR(1) DEFAULT 'A', -- A=Ativa, B=Bloqueada, C=Cancelada
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transacoes (
    id SERIAL PRIMARY KEY,
    conta_id INTEGER REFERENCES contas(id),
    tipo CHAR(1) NOT NULL, -- 'C'=Crédito, 'D'=Débito, 'T'=Transferência
    valor DECIMAL(15,2) NOT NULL,
    descricao VARCHAR(200),
    data_transacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status CHAR(1) DEFAULT 'P', -- 'P'=Processada, 'F'=Falha, 'R'=Rejeitada
    origem VARCHAR(50), -- 'COBOL_BATCH', 'API', 'MOBILE', 'ATM'
    suspeita BOOLEAN DEFAULT FALSE,
    score_fraude DECIMAL(5,4)
);

CREATE TABLE IF NOT EXISTS logs_processamento (
    id SERIAL PRIMARY KEY,
    arquivo_origem VARCHAR(100),
    registros_lidos INTEGER,
    registros_processados INTEGER,
    registros_falhas INTEGER,
    data_inicio TIMESTAMP,
    data_fim TIMESTAMP,
    status VARCHAR(20) -- 'SUCESSO', 'FALHA', 'EM_ANDAMENTO'
);

-- Inserir contas de teste
INSERT INTO contas (numero_conta, saldo) VALUES
('100001', 10000.00),
('100002', 5000.00),
('100003', 25000.00),
('100004', 1500.00),
('100005', 80000.00)
ON CONFLICT (numero_conta) DO NOTHING;

-- Inserir transações de teste
INSERT INTO transacoes (conta_id, tipo, valor, descricao, origem) VALUES
(1, 'C', 1000.00, 'Depósito inicial', 'API'),
(1, 'D', 500.00, 'Saque ATM', 'ATM'),
(2, 'C', 2000.00, 'Transferência recebida', 'MOBILE'),
(3, 'D', 100.00, 'Pagamento', 'WEB')
ON CONFLICT DO NOTHING;