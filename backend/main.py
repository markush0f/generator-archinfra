from fastapi import FastAPI
from app.routers.user import router as user_router
from app.routers.architecture import router as architecture_router
from app.routers.database import router as database_router
from app.routers.tag import router as tag_router
from fastapi.responses import JSONResponse
from app.routers.project import router as project_router
from app.core.database import init_db

app = FastAPI(
    title="Generator ArchInfra",
    version="1.0.0",
)

@app.get("/")
def root():
    return JSONResponse(content={"respuesta": "Ok"}, status_code=200)

init_db()

app.include_router(user_router)
app.include_router(architecture_router)
app.include_router(database_router)
app.include_router(tag_router)
app.include_router(project_router)
