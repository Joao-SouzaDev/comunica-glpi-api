# Comunica GLPI API

API para comunicação com GLPI - Sistema de gerenciamento de chamados desenvolvida com FastAPI.

## Características

- **FastAPI**: Framework moderno e rápido para desenvolvimento de APIs
- **Autenticação**: Sistema de token único que não expira
- **Rotas de Chamados**: CRUD completo para gerenciamento de tickets
- **Health Check**: Monitoramento de saúde da API
- **Documentação Automática**: Swagger UI e ReDoc integrados

## Estrutura do Projeto

```
comunica-glpi-api/
├── app/
│   ├── auth/
│   │   ├── __init__.py
│   │   └── auth_handler.py        # Sistema de autenticação
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── chamados.py           # Rotas de chamados
│   │   └── health.py             # Health check
│   └── __init__.py
├── .github/
│   └── copilot-instructions.md   # Instruções para o Copilot
├── .vscode/
│   └── tasks.json                # Tarefas do VS Code
├── main.py                       # Aplicação principal
├── requirements.txt              # Dependências
├── .env.example                  # Exemplo de variáveis de ambiente
└── README.md
```

## Instalação

1. Clone o repositório:
```bash
git clone <repository-url>
cd comunica-glpi-api
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## Execução

### Desenvolvimento
```bash
python main.py
```

### Produção
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Endpoints

### Health Check
- `GET /api/v1/health` - Status básico da API
- `GET /api/v1/health/detailed` - Status detalhado da API

### Chamados (Requer Autenticação)
- `GET /api/v1/chamados` - Lista todos os chamados
- `GET /api/v1/chamados/{id}` - Obtém um chamado específico
- `POST /api/v1/chamados` - Cria um novo chamado
- `PUT /api/v1/chamados/{id}` - Atualiza um chamado
- `DELETE /api/v1/chamados/{id}` - Exclui um chamado

## Autenticação

A API utiliza autenticação por Bearer Token. Para acessar os endpoints protegidos, inclua o token no header:

```
Authorization: Bearer glpi-api-token-2025-permanent
```

## Documentação

Após iniciar a aplicação, a documentação estará disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Desenvolvimento

Este projeto está configurado para desenvolvimento no VS Code com:
- Tarefas automatizadas para execução
- Instruções personalizadas para o GitHub Copilot
- Estrutura modular para fácil manutenção

## Status

⚠️ **Em Desenvolvimento**: Este projeto contém apenas a estrutura base. As funcionalidades de integração com GLPI ainda precisam ser implementadas.

## Próximos Passos

- [ ] Implementar modelos de dados (Pydantic)
- [ ] Integração com API do GLPI
- [ ] Sistema de logging
- [ ] Testes unitários
- [ ] Validação de dados de entrada
- [ ] Documentação completa da API
