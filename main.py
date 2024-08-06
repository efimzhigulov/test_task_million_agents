import uvicorn
from fastapi import FastAPI
from app.api.routes import router
from app.core import config

app = FastAPI(title=config.PROJECT_NAME,
              debug=config.DEBUG)


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)