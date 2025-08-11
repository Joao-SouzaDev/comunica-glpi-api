# Exemplos de Uso da API

## Como testar a API

### 1. Iniciar o servidor
```bash
python main.py
```

### 2. Testar Health Check (sem autenticação)
```bash
curl http://localhost:8000/api/v1/health
```

### 3. Testar endpoints de chamados (com autenticação)

#### Listar chamados
```bash
curl -H "Authorization: Bearer glpi-api-token-2025-permanent" \
     http://localhost:8000/api/v1/chamados
```

#### Criar um chamado
```bash
curl -X POST \
     -H "Authorization: Bearer glpi-api-token-2025-permanent" \
     -H "Content-Type: application/json" \
     -d '{"titulo": "Problema no sistema", "descricao": "Descrição do problema"}' \
     http://localhost:8000/api/v1/chamados
```

#### Obter um chamado específico
```bash
curl -H "Authorization: Bearer glpi-api-token-2025-permanent" \
     http://localhost:8000/api/v1/chamados/12345
```

### 4. Acessar documentação interativa
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Configuração do Token

O token atual é: `glpi-api-token-2025-permanent`

Para alterar o token, edite o arquivo `.env` ou defina a variável de ambiente:
```bash
set API_TOKEN=seu-novo-token
```
