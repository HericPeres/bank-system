"""
Treinamento de modelo para detecção de fraudes
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def gerar_dados_teste():
    """Gera dados de teste para treinamento"""
    np.random.seed(42)
    
    n_amostras = 1000
    
    dados = {
        'valor': np.random.exponential(500, n_amostras),
        'hora': np.random.randint(0, 24, n_amostras),
        'dia_semana': np.random.randint(0, 7, n_amostras),
        'localizacao': np.random.randint(0, 5, n_amostras),
        'dispositivo': np.random.randint(0, 3, n_amostras),
        'historico_suspeito': np.random.binomial(1, 0.1, n_amostras),
    }
    
    df = pd.DataFrame(dados)
    
    # Criar variável alvo (fraude)
    # Regras simples para simular fraudes
    df['fraude'] = (
        ((df['valor'] > 2000) & (df['hora'] < 5)) |
        ((df['historico_suspeito'] == 1) & (df['valor'] > 1000)) |
        ((df['localizacao'] == 4) & (df['dispositivo'] == 2))
    ).astype(int)
    
    logger.info(f"Dados gerados: {len(df)} registros")
    logger.info(f"Fraudes: {df['fraude'].sum()} ({df['fraude'].mean()*100:.1f}%)")
    
    return df

def treinar_modelo():
    """Treina o modelo de detecção de fraudes"""
    logger.info("Iniciando treinamento do modelo...")
    
    # Gerar dados
    df = gerar_dados_teste()
    
    # Separar features e target
    features = ['valor', 'hora', 'dia_semana', 'localizacao', 
                'dispositivo', 'historico_suspeito']
    X = df[features]
    y = df['fraude']
    
    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    logger.info(f"Treino: {len(X_train)}, Teste: {len(X_test)}")
    
    # Treinar modelo
    modelo = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        class_weight='balanced'
    )
    
    modelo.fit(X_train, y_train)
    
    # Avaliar
    y_pred = modelo.predict(X_test)
    report = classification_report(y_test, y_pred)
    
    logger.info("Relatório de classificação:")
    logger.info(f"\n{report}")
    
    # Salvar modelo
    with open('modelo_fraude.pkl', 'wb') as f:
        pickle.dump(modelo, f)
    
    # Salvar features usadas
    with open('features.pkl', 'wb') as f:
        pickle.dump(features, f)
    
    logger.info("Modelo treinado e salvo como 'modelo_fraude.pkl'")
    
    # Retornar métricas
    return {
        'acuracia_treinamento': modelo.score(X_train, y_train),
        'acuracia_teste': modelo.score(X_test, y_test),
        'features': features,
        'amostras_treino': len(X_train),
        'amostras_teste': len(X_test)
    }

if __name__ == "__main__":
    resultado = treinar_modelo()
    print("\n" + "="*50)
    print("RESUMO DO TREINAMENTO:")
    print(f"Acurácia (treino): {resultado['acuracia_treinamento']:.3f}")
    print(f"Acurácia (teste): {resultado['acuracia_teste']:.3f}")
    print(f"Features usadas: {resultado['features']}")
    print("="*50)