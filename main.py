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




@app.route('/processjson', methods=['POST'])
def processjson():
        
    data = request.get_json()

    entities = data['NCTnumber']
    
    trail_info = trial_scrape(entities)
   
    return jsonify({'Trial Details': trail_info})

if __name__ == '__main__':
    app.run(debug=True)