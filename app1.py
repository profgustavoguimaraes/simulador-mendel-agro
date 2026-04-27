import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da Página
st.set_page_config(page_title="Simulador Mendel: Agronomia", layout="wide")

st.title("🌱 Simulador da 1ª Lei de Mendel")
st.markdown("""
Esta ferramenta simula o cruzamento de dois indivíduos heterozigotos **(Aa x Aa)**.
Ideal para observar a convergência estatística da segregação fenotípica.
""")

# Barra Lateral para Parâmetros
st.sidebar.header("Configurações do Experimento")
n_plantas = st.sidebar.slider("Número de plantas na lavoura (F2):", 10, 5000, 100)

# Simulação
parental = ['A', 'a']
contagem = {"AA": 0, "Aa": 0, "aa": 0}

for _ in range(n_plantas):
    g1, g2 = random.choice(parental), random.choice(parental)
    genotipo = "".join(sorted([g1, g2]))
    contagem[genotipo] += 1

# Processamento de Dados
df = pd.DataFrame({
    'Genótipo': contagem.keys(),
    'Quantidade': contagem.values()
})

dom = contagem["AA"] + contagem["Aa"]
rec = contagem["aa"]
proporcao = dom / rec if rec > 0 else 0

# Exibição de Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Fenótipo Dominante", dom)
col2.metric("Fenótipo Recessivo", rec)
col3.metric("Proporção Real", f"{proporcao:.2f} : 1")

# Gráficos
fig, ax = plt.subplots()
colors = ['#2ca02c', '#d62728']
ax.bar(['Dominante', 'Recessivo'], [dom, rec], color=colors)
ax.set_ylabel('Número de Plantas')
st.pyplot(fig)

st.write(f"**Tabela Genotípica:**", df)