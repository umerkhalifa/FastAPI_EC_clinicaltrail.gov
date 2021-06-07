from utils import trial_scrape
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class clinical_trial(BaseModel):
    NCT_number: str


@app.post('/')
def return_rx(trial: clinical_trial):
    print(trial.NCT_number)
    result= trial_scrape(trial.NCT_number)
    return result


if __name__ == '__main__':
    uvicorn.run(app)

