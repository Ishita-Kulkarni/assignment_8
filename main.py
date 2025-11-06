from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from operations import calculate, DivisionByZeroError, InvalidOperationError

app = FastAPI(
    title="FastAPI Calculator",
    description="A simple calculator API built with FastAPI",
    version="1.0.0"
)

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str

class CalculationResponse(BaseModel):
    result: float
    operation: str
    num1: float
    num2: float

@app.get("/")
async def root():
    """Root endpoint returning welcome message"""
    return {
        "message": "Welcome to FastAPI Calculator!",
        "endpoints": {
            "/docs": "API documentation",
            "/calculate": "Perform calculations"
        }
    }

@app.post("/calculate", response_model=CalculationResponse)
async def calculate_endpoint(request: CalculationRequest):
    """
    Perform basic arithmetic calculations
    
    Operations supported:
    - add: Addition
    - subtract: Subtraction
    - multiply: Multiplication
    - divide: Division
    """
    try:
        result = calculate(request.num1, request.num2, request.operation)
        return CalculationResponse(
            result=result,
            operation=request.operation.lower(),
            num1=request.num1,
            num2=request.num2
        )
    except DivisionByZeroError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InvalidOperationError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
