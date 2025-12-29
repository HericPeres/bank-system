       IDENTIFICATION DIVISION.
       PROGRAM-ID. BATCH-PROCESS.
       AUTHOR. MAINFRAME-TEAM.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT ARQ-TRANSACOES
               ASSIGN TO '/shared_data/transacoes.dat'
               ORGANIZATION IS LINE SEQUENTIAL.
               
           SELECT ARQ-SALDOS
               ASSIGN TO '/shared_data/saldos.dat'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       
       FD ARQ-TRANSACOES.
       01 REG-TRANSACAO.
           05 RT-CONTA      PIC 9(10).
           05 RT-TIPO       PIC X(1).
           05 RT-VALOR      PIC 9(9)V99.
           05 RT-DATA       PIC X(10).
           
       FD ARQ-SALDOS.
       01 REG-SALDO.
           05 RS-CONTA      PIC 9(10).
           05 RS-SALDO      PIC S9(9)V99.
           05 RS-STATUS     PIC X(1).

       WORKING-STORAGE SECTION.
       77 WS-EOF            PIC X(1) VALUE 'N'.
       77 WS-CONTADOR       PIC 9(5) VALUE 0.
       
       PROCEDURE DIVISION.
       
       MAIN-PROCEDURE.
           DISPLAY 'INICIANDO PROCESSAMENTO BATCH'.
           PERFORM ABRE-ARQUIVOS.
           PERFORM PROCESSAR-TRANSACOES.
           PERFORM FECHA-ARQUIVOS.
           DISPLAY 'PROCESSAMENTO CONCLUIDO'.
           DISPLAY 'TOTAL REGISTROS: ' WS-CONTADOR.
           STOP RUN.
           
       ABRE-ARQUIVOS.
           OPEN INPUT ARQ-TRANSACOES.
           OPEN OUTPUT ARQ-SALDOS.
           
       PROCESSAR-TRANSACOES.
           PERFORM UNTIL WS-EOF = 'S'
               READ ARQ-TRANSACOES
                   AT END MOVE 'S' TO WS-EOF
                   NOT AT END PERFORM PROCESSAR-REGISTRO
               END-READ
           END-PERFORM.
           
       PROCESSAR-REGISTRO.
           ADD 1 TO WS-CONTADOR.
           MOVE RT-CONTA TO RS-CONTA.
           MOVE 1000.00 TO RS-SALDO.  -- Valor exemplo
           MOVE 'A' TO RS-STATUS.
           WRITE REG-SALDO.
           
       FECHA-ARQUIVOS.
           CLOSE ARQ-TRANSACOES.
           CLOSE ARQ-SALDOS.