from fastapi import FastAPI
from ultralytics import YOLO

app = FastAPI()

# Load YOLO model
model = YOLO('best.pt')


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "hello"}
