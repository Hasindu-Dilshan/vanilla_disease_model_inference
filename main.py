from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    a = 'sdf'
    return {"message": "hello"}
