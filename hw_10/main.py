import joblib
import uvicorn

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()



with open("gb_fitted.pkl", 'rb') as file:
    model = joblib.load(file)

with open('l.pkl', 'rb') as file:
        l = joblib.load(file)



class ModelRequestData(BaseModel):
    total_square: int
    rooms: int
    floor: int
    city: str


class Result(BaseModel):
    result: float

@app.get("/")
def index():
    return {"UI": "http://127.0.0.1:8000/docs"}

@app.get("/health")
def health():
    return JSONResponse(content={"message": "It's alive!"}, status_code=200)

@app.post("/predict_post", response_model=Result)
def preprocess_data(data: ModelRequestData):
    input_data = data.model_dump()
    input_data['city']=l.index(input_data['city'])
    input_df = pd.DataFrame(input_data, index=[0])
    result = model.predict(input_df)[0]
    return Result(result=result)

@app.get("/predict_get")
def predict_get(sqare: int):
    d = {'total_square': sqare, 'rooms': 2, 'floor': 7, 'city': l.index('пос.подсобного хозяйства "Воскресенское"')}
    df = pd.DataFrame(d, index=[0])
    result = model.predict(df)[0]
    return result



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8008)

