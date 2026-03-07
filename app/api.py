from fastapi import FastAPI #importing class
from routers import metrics,aws,health,logs
app = FastAPI(
    title= "DevOps Monitoring API",
    description = "DevOps Monitoring API: This is ana internal api utilities",
    version = "1.1.0",
    doc_url="/docs",
    redoc_url="/redoc"
)

@app.get("/") 
def hello():
    """
    This is a Hello Api ,Just for testing
    """
    return {"message":"Hello Dosto This is devops utilities api"}

app.include_router(metrics.router)
app.include_router(aws.router)
app.include_router(logs.router)
app.include_router(health.router)