README.md - Sistema Bancário Híbrido COBOL + Python
markdown
# 🏦 Sistema Bancário Híbrido COBOL + Python

Um sistema bancário completo que integra processamento batch em COBOL com APIs modernas em Python, incluindo detecção de fraudes com machine learning e dashboard em tempo real.

## 🚀 Tecnologias Utilizadas

- **COBOL** (GnuCOBOL) - Processamento batch de transações
- **Python 3.11+** - API, ML e Dashboard
- **FastAPI** - API REST moderna
- **Streamlit** - Dashboard interativo
- **PostgreSQL** - Banco de dados
- **Scikit-learn** - Detecção de fraudes
- **Docker** - Containerização (opcional)

## 📁 Estrutura do Projeto
bank-system/
├── cobol/ # Código COBOL
| |
│ ├── src/ # Programas COBOL
│ │ ├── CBL0001.cob # Programa principal
| | |
│ │ └── JCL/ # Scripts de controle
| |
│ ├── data/ # Arquivos de dados
| |
│ └── scripts/ # Scripts de execução
|
├── python/ # Código Python
| |
│ ├── api/ # API FastAPI
| | |
│ │ └── main.py # API principal
| |
│ ├── dashboard/ # Dashboard Streamlit
| | |
│ │ └── app.py # Dashboard principal
| |
│ ├── fraud_detection/ # ML para detecção de fraudes
| |
│ ├── loader/ # Integração COBOL-Python
| |
│ ├── tests/ # Testes
| |
│ ├── utils/ # Utilitários
| |
│ └── requirements.txt # Dependências Python
|
├── database/ # Scripts do banco de dados
|
├── docker/ # Configurações Docker
|
├── docs/ # Documentação
|
└── docker-compose.yml # Orquestração de containers

text

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.11 ou superior
- Pip (gerenciador de pacotes Python)
- Git (opcional)

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/bank-system.git
cd bank-system
2. Configurar ambiente virtual (recomendado)
bash
# Criar ambiente virtual
python -m venv .venv

# Ativar no Windows:
.venv\Scripts\activate

# Ativar no Linux/Mac:
source .venv/bin/activate
3. Instalar dependências Python
bash
cd python
pip install -r requirements.txt
🚀 Como Executar
Opção 1: Executar sem Docker (Recomendado para desenvolvimento)
A. Executar a API FastAPI
bash
# Na pasta bank-system\python
cd python
python api/main.py
Acesse: http://localhost:8000
Documentação: http://localhost:8000/docs

B. Executar o Dashboard Streamlit
bash
# Em outro terminal, na pasta bank-system\python
cd python
streamlit run dashboard/app.py
Acesse: http://localhost:8501

C. Testar o modelo de Machine Learning
bash
cd python
python fraud_detection/train_model.py
D. Executar o monitor de arquivos
bash
cd python
python loader/file_monitor.py
Opção 2: Executar com Docker (Recomendado para produção)
bash
# Construir e iniciar todos os containers
docker-compose up --build

# Ou em segundo plano
docker-compose up -d

# Parar todos os containers
docker-compose down
📊 Endpoints da API
Rotas principais:
GET / - Status da API

GET /contas - Listar todas as contas

GET /contas/{id} - Buscar conta específica

POST /transacoes - Criar nova transação

GET /status - Status do sistema

Exemplos de uso:
bash
# Status da API
curl http://localhost:8000

# Listar contas
curl http://localhost:8000/contas

# Status do sistema
curl http://localhost:8000/status
🎯 Funcionalidades
1. Processamento COBOL
Processamento batch de transações

Geração de arquivos de saída

Integração com sistemas legados

2. API REST Moderna
Documentação automática (Swagger/OpenAPI)

Validação de dados com Pydantic

Rotas para contas e transações

3. Dashboard em Tempo Real
Métricas bancárias

Gráficos de transações

Status da integração COBOL

4. Detecção de Fraudês
Modelo de machine learning

Análise em tempo real

Score de risco por transação

🔧 Configuração Avançada
Banco de Dados PostgreSQL
bash
# Criar manualmente (se não usar Docker)
createdb bankdb
psql -d bankdb -f database/init.sql
Variáveis de Ambiente
Crie um arquivo python/.env:

env
DATABASE_URL=postgresql://bankuser:bankpass@localhost:5432/bankdb
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
Configuração do COBOL
bash
# Instalar GnuCOBOL no Windows (via WSL)
wsl --install
# No WSL: sudo apt-get install gnucobol

# Compilar programa COBOL
cd cobol
cobc -x -o bin/programa src/CBL0001.cob
🧪 Testes
bash
# Executar testes (em desenvolvimento)
cd python
python -m pytest tests/
📈 Monitoramento
Logs da API
bash
# Ver logs em tempo real
docker-compose logs -f api

# Logs específicos
docker-compose logs api --tail=100
Métricas
Dashboard: http://localhost:8501

Documentação API: http://localhost:8000/docs

Health Check: http://localhost:8000/status

🤝 Contribuição
Fork o projeto

Crie uma branch (git checkout -b feature/nova-funcionalidade)

Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')

Push para a branch (git push origin feature/nova-funcionalidade)

Abra um Pull Request

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🆘 Suporte
Problemas Comuns
"ModuleNotFoundError: No module named 'fastapi'"

bash
pip install fastapi uvicorn pydantic
"streamlit: command not found"

bash
pip install streamlit
Porta já em uso

Mude a porta no arquivo api/main.py (linha port=8000)

Erro de banco de dados

bash
# Verificar se PostgreSQL está rodando
# Criar banco manualmente se necessário
Contato
Issues: GitHub Issues

Email: seu-email@exemplo.com

Desenvolvido com ❤️ para integração de sistemas legados com tecnologias modernas.

text

## **PARA USAR:**

1. **Copie todo este texto**
2. **Crie/Abra o arquivo** `README.md` na pasta principal `bank-system`
3. **Cole o conteúdo**
4. **Salve** (Ctrl+S)

## **BÔNUS: Criar também um `requirements.txt` completo:**

Crie/Atualize `python/requirements.txt` com:

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pandas==2.1.3
numpy==1.24.3
scikit-learn==1.3.2
streamlit==1.29.0
python-multipart==0.0.6
pydantic==2.5.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0
watchdog==3.0.0

---
**Desenvolvido por:** Heric Rodrigues Peres  
**Contato:** hericperes9@gmail.com  
**GitHub:** [@HericPeres](https://github.com/seu-usuario)
