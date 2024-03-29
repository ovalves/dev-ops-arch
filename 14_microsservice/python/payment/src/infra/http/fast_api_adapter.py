import os
import uvicorn
from typing import Callable
from infra.http.http_server import HttpServer
from fastapi import FastAPI


class FastApiAdapter(HttpServer):
    app: None
    APP_PREFIX = os.getenv("APP_PREFIX", "")

    def __init__(self):
        self.app = FastAPI(
            root_path=f"/{self.APP_PREFIX}",
            title="Arquitetura baseada em microsserviços",
            description="Arquitetura baseada em microsserviços com Python.",
            version="v1",
        )

    @property
    def get(self):
        return self.app.get

    @property
    def post(self):
        return self.app.post

    @property
    def put(self):
        return self.app.put

    @property
    def delete(self):
        return self.app.delete

    def listen(self, port: int) -> None:
        uvicorn.run(self.app, host="0.0.0.0", port=port, debug=False, log_level="info")
