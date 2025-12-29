import warnings
warnings.filterwarnings("ignore")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Sistema Bancário API", version="1.0.0")

# Modelos de dados
class Conta(BaseModel):
    id: int
    numero_conta: str
    saldo: float
    status: str
    
    class Config:
        from_attributes = True

class Transacao(BaseModel):
    conta_id: int
    tipo: str
    valor: float
    descricao: Optional[str] = None
    
    class Config:
        from_attributes = True

# Dados em memória (temporário)
contas_db = [
    {"id": 1, "numero_conta": "100001", "saldo": 10000.00, "status": "A"},
    {"id": 2, "numero_conta": "100002", "saldo": 5000.00, "status": "A"},
]

transacoes_db = []

@app.get("/")
def read_root():
    return {"message": "Sistema Bancário API", "status": "online"}

@app.get("/contas", response_model=List[Conta])
def listar_contas():
    return contas_db

@app.get("/contas/{conta_id}")
def buscar_conta(conta_id: int):
    for conta in contas_db:
        if conta["id"] == conta_id:
            return conta
    raise HTTPException(status_code=404, detail="Conta não encontrada")

@app.post("/transacoes")
def criar_transacao(transacao: Transacao):
    # Aqui integraríamos com COBOL depois
    nova_transacao = {
        "id": len(transacoes_db) + 1,
        **transacao.dict(),
        "status": "processada"
    }
    transacoes_db.append(nova_transacao)
    
    # Usando a variável para remover warning
    print(f"Transações totais: {len(transacoes_db)}")
    
    return {"message": "Transação registrada", "transacao": transacao}

@app.get("/status")
def status_sistema():
    return {
        "api": "online",
        "contas_registradas": len(contas_db),
        "transacoes": len(transacoes_db),
        "integracao_cobol": "pendente"
    }

if __name__ == "__main__":
    print("=== INICIANDO SISTEMA BANCÁRIO ===")
    print("API disponível em: http://localhost:8000")
    print("Documentação: http://localhost:8000/docs")
    print("Pressione Ctrl+C para parar")
    uvicorn.run(app, host="0.0.0.0", port=8000)