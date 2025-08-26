# Dockerfile para FastAPI GLPI API
FROM python:3.11-slim

WORKDIR /app

# Copia os arquivos do projeto
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do FastAPI
EXPOSE 3030

# Comando para iniciar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3030"]
