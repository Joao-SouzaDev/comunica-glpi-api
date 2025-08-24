"""
FastAPI application for GLPI API communication
Main application entry point
"""

from fastapi import FastAPI
from app.routers import chamados, health, notificacao, user
from app.auth.auth_handler import get_api_key

# Initialize FastAPI app
app = FastAPI(
    title="Comunica GLPI API",
    description="API para comunicação com GLPI - Sistema de chamados",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["Health"])
app.include_router(chamados.router, prefix="/api/v1", tags=["Chamados"])
app.include_router(user.router, prefix="/api/v1", tags=["Usuários"])
app.include_router(notificacao.router, prefix="/api/v1", tags=["Notificação"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Comunica GLPI API - Sistema de chamados"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
