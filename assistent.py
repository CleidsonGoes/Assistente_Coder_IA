""" Estudo 01 - AI Coder - Criando um Assistente de Programação Python,
    em Python """

# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plaforma Groq e acessar o LLM
from groq import Groq

# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="AI Coder",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define um prompt de sistema que descreve as regras e comportamento do
# assistente de IA

CUSTOM_PROMPT = """
Você é o "Coder", um assistente de IA especialista em programação, com
foco principal em Python. Sua missão é ajudar desenvolvedores iniciantes com
dúvidas de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas a
    programação, algoritmos, estruturas de dados, bibliotecas e frameworks.
    Se o usuário perguntar sobre outro assunto, responda educadamente que
    seu foco é exclusivamente em auxiliar com código.

2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte
    maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o
    tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python
    com a sintaxe correta. O código deve ser bem comentado para explicar as
    partes importantes.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes
    o que cada parte do código faz, explicando a lógica e as funções
    utilizadas.
    * **Documentação de Referência**: Ao final, inclua uma seção chamada
    "📚 Documentação de Referência" com um link direto e relevante para a
    documentação oficial da Linguagem Python (docs.python.org) ou da
    biblioteca em questão.
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões
    desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:

    # Define o título da barra lateral
    st.title("AI Coder")

    # Mostra um texto explicativo sobre o assistente
    st.markdown("Um assistente de IA focado em programação Python para ajudar "
                "iniciantes.")

    # Campo para inserir a chave de API da Groq
    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação "
                "com linguagem Python. IA pode cometer erros. Sempre "
                "verifique as respostas.")

    # Adiciona Links das redes sociais
    st.markdown("---")
    st.markdown("Acesse minhas redes sociais.")

    st.markdown("LinkedIn: https://www.linkedin.com/in/cleidson-jorge-s-goes/")
    st.markdown("Github: https://github.com/CleidsonGoes")
    st.markdown("Portfólio: https://portfolio-blue-delta-62.vercel.app/")

    st.link_button("✉️E-mail para suporte de uso",
                   "mailto:jorgegoes4@gmail.com")

# Título principal do app
st.title("Assistente IA Coder")

# Subtítulo adicional
st.title("Assistente Pessoal de Programação Python 🐍")

# Texto auxiliar abaixo do título
st.caption("Faça sua pergunta sobre a Linguagem Python e obtenha código, "
           "explicações e referências.")
