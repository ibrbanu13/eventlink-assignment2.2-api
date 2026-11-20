from fastapi import FastAPI

app = FastAPI(title="EventLink API", version="v1")

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Routers will be registered here in later commits