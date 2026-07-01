from fastapi import FastAPI

app = FastAPI(
    title="Fintech Core API",
    description="API para la gestión de billeteras y transacciones",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Fintech Core API",
        "docs_url": "/docs"
    }
