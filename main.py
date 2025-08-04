from fastapi import FastAPI
from app.routers import formdata
import uvicorn

app = FastAPI(title="KPA Backend Assignment")

app.include_router(formdata.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
