from typing import List

from datetime import datetime

import uvicorn
from fastapi import FastAPI, Body
from starlette import status

TIME_FORMAT = "%m/%d/%Y, %H:%M:%S"

app = FastAPI()


@app.post("/programs/{client_id}", status_code=status.HTTP_201_CREATED)
async def save_programs(client_id: str, process_names: List[str] = Body(...)):
    with open(f"{client_id}_running_programs.txt", mode='a+') as file:
        current_time_string = datetime.now().strftime(TIME_FORMAT)
        file.write(f"[{current_time_string}]{','.join(process_names)}\n")


if __name__ == '__main__':
    uvicorn.run(app)
