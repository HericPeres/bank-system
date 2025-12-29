# 🏦 Sistema Bancário Híbrido (COBOL + Python)

Este projeto foi desenvolvido para simular um ambiente bancário real, onde sistemas
legados escritos em COBOL convivem com APIs modernas em Python. A ideia é reproduzir
um cenário próximo ao encontrado em grandes instituições financeiras, integrando
processamento batch, API REST, machine learning e visualização de dados.

---

## 🚀 Tecnologias Utilizadas

- COBOL (GnuCOBOL) – Processamento batch de transações
- Python 3.11+ – API, automações e machine learning
- FastAPI – API REST
- Streamlit – Dashboard interativo
- PostgreSQL – Banco de dados
- Scikit-learn – Detecção de fraudes
- Docker / Docker Compose – Containerização (opcional)

---

## 🎯 Objetivo do Projeto

- Simular a integração entre sistemas legados e tecnologias modernas  
- Processar transações bancárias em batch (COBOL)  
- Disponibilizar dados por meio de uma API REST  
- Implementar detecção de fraudes com machine learning  
- Exibir métricas e informações em tempo real em um dashboard  

---

## 📁 Estrutura do Projeto

```
sistema-banco/
├── cobol/
│   ├── src/
│   │   ├── CBL0001.cob
│   │   └── JCL/
│   ├── data/
│   └── scripts/
├── python/
│   ├── api/
│   │   └── main.py
│   ├── dashboard/
│   │   └── app.py
│   ├── detecção_de_fraude/
│   │   └── train_model.py
│   ├── loader/
│   │   └── file_monitor.py
│   ├── tests/
│   ├── utils/
│   └── requirements.txt
├── database/
│   └── init.sql
├── docker/
│   ├── cobol/
│   │   └── Dockerfile
│   └── python/
│       └── Dockerfile
├── docs/
└── docker-compose.yml
```

---

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.11 ou superior  
- Pip  
- Git (opcional)  
- PostgreSQL (caso não utilize Docker)  

### Clonar o "repositório"

```bash
git clone https://github.com/seu-usuario/bank-system.git
cd bank-system
Criar e ativar ambiente virtual (recomendado)
python -m venv .venv


Windows:

.venv\Scripts\activate


Linux / Mac:

source .venv/bin/activate

Instalar dependências
cd python
pip install -r requirements.txt

🚀 Como Executar
Executar sem Docker (desenvolvimento)

API FastAPI:

cd python
python api/main.py


Acesse:

http://localhost:8000

Docs: http://localhost:8000/docs

Dashboard Streamlit:

cd python
streamlit run dashboard/app.py


Acesse:

http://localhost:8501

Modelo de detecção de fraudes:

cd python
python fraud_detection/train_model.py


Monitor de arquivos:

cd python
python loader/file_monitor.py

Executar com Docker
docker-compose up --build


Em segundo plano:

docker-compose up -d


Parar os containers:

docker-compose down

📊 Endpoints da API

GET / – Status da API

GET /contas – Lista todas as contas

GET /contas/{id} – Retorna uma conta específica

POST /transacoes – Cria uma nova transação

GET /status – Status geral do sistema

Exemplos:

curl http://localhost:8000
curl http://localhost:8000/contas
curl http://localhost:8000/status

⚙️ Funcionalidades

Processamento COBOL:

Processamento batch de transações

Geração de arquivos

Simulação de integração com sistemas legados

API REST:

FastAPI com documentação automática

Validação de dados com Pydantic

Endpoints para contas e transações

Dashboard:

Métricas bancárias

Gráficos de transações

Status do processamento COBOL

Detecção de Fraudes:

Modelo de machine learning

Score de risco por transação

Base para análise em tempo real

🔧 Configuração Avançada

Banco de Dados PostgreSQL (sem Docker):

createdb bankdb
psql -d bankdb -f database/init.sql


Variáveis de ambiente (python/.env):

DATABASE_URL=postgresql://bankuser:bankpass@localhost:5432/bankdb
SECRET_KEY=sua-chave-secreta
DEBUG=True


COBOL (GnuCOBOL):

Instalação via WSL:

wsl --install
sudo apt-get install gnucobol


Compilação:

cd cobol
cobc -x -o bin/programa src/CBL0001.cob

🧪 Testes
cd python
python -m pytest tests/

📈 Monitoramento

Logs da API:

docker-compose logs -f api


Acessos:

Dashboard: http://localhost:8501

Health Check: http://localhost:8000/status

📦 Dependências Principais
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pandas==2.1.3
numpy==1.24.3
scikit-learn==1.3.2
streamlit==1.29.0
python-dotenv==1.0.0
watchdog==3.0.0

👨‍💻 Autor

Heric Rodrigues Peres
Email: hericperes9@gmail.com

GitHub: https://github.com/HericPeres
