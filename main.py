from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.config import settings
from core.database import Base
from core.database import engine
from core.routers import auth, product, shop

router_list = [auth.router, product.router, shop.router]
origins = [
    "http://127.0.0.1:1234",
    "http://localhost:1234",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    [app.include_router(router) for router in router_list]
    configure_static(app)
    create_tables()
    return app


app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)