🧠 Assistente Coder IA
Criando Seu Assistente de Programação Python em Python

Este projeto demonstra a criação de um assistente inteligente para auxiliar no desenvolvimento de aplicações Python, utilizando Streamlit e modelos de linguagem.

🚀 Configuração do Ambiente

1️⃣ Crie um ambiente virtual com Conda
conda create --name assistent python=3.13

2️⃣ Ative o ambiente.

conda activate assistent

ou

source activate assistent

3️⃣ Instale o pip e as dependências do projeto

conda install pip

pip install -r requirements.txt

▶️ Executando a Aplicação
No terminal, dentro da pasta do projeto, execute:

streamlit run assistent.py


A aplicação abrirá no navegador automaticamente.

💬 Exemplos de Uso do Assistente

Você pode fazer perguntas ao assistente, como:

Como crio um hello world em Python?

Qual a sintaxe de um loop em Python?

Como eu uso a função map em Python? Me dê um exemplo com lambda.

🧹 Gerenciamento do Ambiente Virtual

Desativar o ambiente virtual

conda deactivate

Remover o ambiente (opcional)

conda remove --name assistent --all
