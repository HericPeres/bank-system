import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CobolFileHandler(FileSystemEventHandler):
    """Monitora novos arquivos gerados pelo COBOL"""
    
    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"Novo arquivo detectado: {event.src_path}")
            
            # Aguardar o arquivo ser completamente escrito
            time.sleep(0.5)
            
            # Processar arquivo baseado no tipo
            if 'saldos' in event.src_path:
                self.processar_saldos(event.src_path)
            elif 'transacoes' in event.src_path:
                self.processar_transacoes(event.src_path)
    
    def processar_saldos(self, filepath):
        """Processa arquivo de saldos do COBOL"""
        try:
            with open(filepath, 'r') as f:
                conteudo = f.read()
            
            logger.info(f"Processando saldos: {len(conteudo)} bytes")
            # Aqui você adicionaria a lógica para salvar no banco
            
            # Simulação
            linhas = conteudo.strip().split('\n')
            for i, linha in enumerate(linhas):
                if linha.strip():
                    logger.info(f"Linha {i+1}: {linha[:50]}...")
            
            logger.info(f"Arquivo {filepath} processado com sucesso")
            
        except Exception as e:
            logger.error(f"Erro ao processar {filepath}: {e}")
    
    def processar_transacoes(self, filepath):
        """Processa arquivo de transações do COBOL"""
        logger.info(f"Iniciando processamento de transações: {filepath}")
        # Similar ao processar_saldos, mas para transações

def iniciar_monitoramento(diretorio='/shared_data'):
    """Inicia o monitoramento de arquivos"""
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        logger.info(f"Diretório criado: {diretorio}")
    
    event_handler = CobolFileHandler()
    observer = Observer()
    observer.schedule(event_handler, diretorio, recursive=False)
    
    logger.info(f"Iniciando monitoramento do diretório: {diretorio}")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    iniciar_monitoramento()