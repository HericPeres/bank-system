import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Bancário",
    page_icon="🏦",
    layout="wide"
)

# Título
st.title("🏦 Sistema Bancário - Dashboard")
st.markdown("---")

# Colunas para métricas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Contas Ativas", "125", "+3")
with col2:
    st.metric("Transações Hoje", "1,234", "+12%")
with col3:
    st.metric("Saldo Total", "R$ 2.5M", "+5.2%")
with col4:
    st.metric("Fraudes Detectadas", "2", "-1")

st.markdown("---")

# Gráficos
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Transações por Tipo")
    
    # Dados de exemplo
    dados_tipo = pd.DataFrame({
        'Tipo': ['Crédito', 'Débito', 'Transferência'],
        'Quantidade': [450, 320, 230]
    })
    
    fig = px.bar(dados_tipo, x='Tipo', y='Quantidade', color='Tipo')
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.subheader("📈 Volume por Hora")
    
    # Dados de exemplo
    horas = [f"{h:02d}:00" for h in range(8, 18)]
    volume = [120, 180, 220, 300, 450, 520, 480, 350, 280, 200]
    
    dados_hora = pd.DataFrame({'Hora': horas, 'Volume': volume})
    fig = px.line(dados_hora, x='Hora', y='Volume', markers=True)
    st.plotly_chart(fig, use_container_width=True)

# Seção de integração COBOL
st.markdown("---")
st.subheader("🔗 Integração COBOL")

col_status, col_actions = st.columns([2, 1])

with col_status:
    st.write("**Status do Processamento Batch:**")
    
    status_data = {
        'Arquivo': ['transacoes.dat', 'saldos.dat', 'clientes.dat'],
        'Status': ['✅ Processado', '🔄 Em processamento', '⏳ Pendente'],
        'Registros': [1250, 500, 0],
        'Última execução': ['10:30', 'Em andamento', '-']
    }
    
    df_status = pd.DataFrame(status_data)
    st.dataframe(df_status, use_container_width=True)

with col_actions:
    st.write("**Ações:**")
    
    if st.button("Executar Batch COBOL", type="primary"):
        st.success("Processamento batch iniciado!")
    
    if st.button("Verificar Arquivos"):
        st.info("Verificação concluída")
    
    if st.button("Limpar Logs"):
        st.warning("Logs limpos")

# Rodapé
st.markdown("---")
st.caption("Sistema Bancário Híbrido COBOL + Python | v1.0.0")