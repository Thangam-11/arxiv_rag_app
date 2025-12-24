from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI(
    title="RAG API",
    description="Retrieval-Augmented Generation API",
    version="0.1.0"
)

# Create API v1 router
api_router = APIRouter(prefix="/api/v1")

@api_router.get("/health")
def health():
    return {"status": "ok"}

# Include the router
app.include_router(api_router)

# Also keep root health endpoint for convenience
@app.get("/health")
def root_health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "RAG API is running"}
