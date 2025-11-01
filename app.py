from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response, JSONResponse
from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline
import asyncio
from concurrent.futures import ThreadPoolExecutor

text:str = "What is Text Summarization?"

app = FastAPI()

# Thread pool for running blocking operations
executor = ThreadPoolExecutor(max_workers=2)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        # Return immediate response that training has started
        def run_training():
            os.system("python main.py")
        
        # Run training in background
        loop = asyncio.get_event_loop()
        loop.run_in_executor(executor, run_training)
        
        return JSONResponse(
            content={"message": "Training started in background. Check logs for progress."},
            status_code=200
        )

    except Exception as e:
        return JSONResponse(
            content={"error": f"Error Occurred! {str(e)}"},
            status_code=500
        )
    

@app.post("/predict")
async def predict_route(text: str):
    try:
        def run_prediction(input_text):
            obj = PredictionPipeline()
            return obj.predict(input_text)
        
        # Run prediction in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(executor, run_prediction, text)
        
        return JSONResponse(
            content={"prediction": result},
            status_code=200
        )
    except Exception as e:
        return JSONResponse(
            content={"error": f"Error: {str(e)}"},
            status_code=500
        )
    

if __name__=="__main__":
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8080,
        timeout_keep_alive=300  # Increase timeout to 5 minutes
    )