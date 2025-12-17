from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from starlette.responses import Response
from typing import Optional, List
import pandas as pd
import numpy as np

from app.db.models import UserAnswer, DataFilter
from app.api import api

app = FastAPI(
    title="Data Analysis API",
    description="A comprehensive data analysis API by Samarth",
    version="1.0.0",
    contact={
        "name": "Samarth",
        "email": "samarth@example.com"
    }
)


@app.get("/")
def root():
    return {
        "message": "Data Analysis API by Samarth",
        "version": "1.0.0",
        "endpoints": {
            "documentation": "/docs",
            "stats": "/stats/overview",
            "analysis": "/analysis/correlation",
            "visualization": "/visualize/chart/bar"
        }
    }


# Data Analysis Endpoints
@app.get("/stats/overview")
def get_statistical_overview():
    """Get comprehensive statistical overview of all datasets"""
    return api.get_statistical_overview()


@app.get("/stats/cars")
def get_cars_statistics():
    """Get detailed statistics for car dataset"""
    return api.get_cars_statistics()


@app.get("/analysis/correlation")
def get_correlation_analysis():
    """Perform correlation analysis between numerical variables"""
    return api.get_correlation_analysis()


@app.get("/analysis/distribution/{field}")
def get_distribution_analysis(field: str):
    """Get distribution analysis for a specific field"""
    try:
        return api.get_distribution_analysis(field)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/analysis/trends")
def get_trend_analysis():
    """Analyze trends across datasets"""
    return api.get_trend_analysis()


# Data Operations
@app.get("/data/cars")
def get_all_cars():
    """Get all car data"""
    return api.read_cars()


@app.get("/data/cars/filter")
def filter_cars(
    fuel: Optional[str] = None,
    price: Optional[str] = None,
    category: Optional[str] = None
):
    """Filter cars by fuel type, price range, or category"""
    return api.filter_cars(fuel=fuel, price=price, category=category)


@app.get("/data/summary")
def get_data_summary():
    """Get summary statistics for all datasets"""
    return api.get_data_summary()


# Original endpoints (maintained for compatibility)
@app.get("/user")
def read_user():
    return api.read_user()


@app.get("/question/{position}", status_code=200)
def read_questions(position: int, response: Response):
    question = api.read_questions(position)
    if not question:
        raise HTTPException(status_code=400, detail="Error")
    return question


@app.get("/alternatives/{question_id}")
def read_alternatives(question_id: int):
    return api.read_alternatives(question_id)


@app.post("/answer", status_code=201)
def create_answer(payload: UserAnswer):
    payload = payload.dict()
    return api.create_answer(payload)


@app.get("/result/{user_id}")
def read_result(user_id: int):
    return api.read_result(user_id)
