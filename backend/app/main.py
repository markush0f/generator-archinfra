from fastapi import FastAPI
from app.routers.user import router as user_router
from app.routers.architecture import router as architecture_router

app = FastAPI(
    title="Generator ArchInfra",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "API funcionando !!"}


app.include_router(user_router)
app.include_router(architecture_router)
