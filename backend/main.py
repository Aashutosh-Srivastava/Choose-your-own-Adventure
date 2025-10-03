from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.config import settings
from backend.routers import story,job

from backend.db.database import Base, engine, create_Tables
# create tables
Base.metadata.create_all(bind=engine)

create_Tables(engine)



app = FastAPI(
    title="Choose your own AI Adventure",
    description="An AI adventure game where you can choose your own path",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router,prefix=settings.API_PREFIX)
app.include_router(job.router,prefix=settings.API_PREFIX)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
