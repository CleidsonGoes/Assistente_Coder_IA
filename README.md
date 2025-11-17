🧠 **Assistente Coder IA**

**Criando Seu Assistente de Programação Python em Python**  

Este projeto demonstra a criação de um assistente inteligente para auxiliar no desenvolvimento de aplicações Python, utilizando Streamlit e modelos de linguagem.

**Software Necessário**

• Python 3.10 ou superior (recomendado: 3.13)

**Necessário para executar o código da aplicação.**

• Conda (Anaconda ou Miniconda) Usado para criar e gerenciar o ambiente virtual

• Navegador Web Atualizado (Chrome).

🌐 **Acesso à Internet**

A conexão é obrigatória, pois o modelo utiliza a API da Groq:

Necessário ter uma API Key válida.

A aplicação não funciona offline.

🔗 Link para criar sua chave:
https://console.groq.com/keys

🚀 **Configuração do Ambiente**

1️⃣ Crie um ambiente virtual com Conda
conda create --name assistent python=3.13

2️⃣ Ative o ambiente.

conda activate assistent  
ou  
source activate assistent  

3️⃣ **Instale o pip e as dependências do projeto**

conda install pip

pip install -r requirements.txt

▶️ **Executando a Aplicação**
No terminal, dentro da pasta do projeto, execute:

streamlit run assistent.py

A aplicação abrirá no navegador automaticamente.

💬 **Exemplos de Uso do Assistente**

Você pode fazer perguntas ao assistente, como:

Como crio um hello world em Python?

Qual a sintaxe de um loop em Python?

Como eu uso a função map em Python? Me dê um exemplo com lambda.

🧹 **Gerenciamento do Ambiente Virtual**

Desativar o ambiente virtual

conda deactivate

Remover o ambiente (opcional)

conda remove --name assistent --all
