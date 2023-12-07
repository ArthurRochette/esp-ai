from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def hello_world():
    return {"message": "Hello World!"}

@app.get(f"/get/{position}")
def get_position(position: int):
    # generate
    return {"position": position, "heatmappixel": []}


# python3 -m uvicorn api:app --reload