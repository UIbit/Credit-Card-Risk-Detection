# Data Analysis API by Samarth [![CircleCI](https://circleci.com/gh/samarth/data-analysis-api.svg?style=svg)](https://circleci.com/gh/samarth/data-analysis-api)

A comprehensive FastAPI-based Data Analysis API that provides statistical insights, data visualization endpoints, and analytical operations on datasets.

## Features

- **Data Analysis Endpoints**: Statistical summaries, correlations, distributions
- **Visualization**: Generate charts and graphs via API
- **Data Processing**: Filter, aggregate, and transform data
- **Interactive API Documentation**: Swagger UI at `/docs`
- **RESTful Architecture**: Clean, well-structured API design

## Preconditions

- Python 3.8+
- pip

## Clone the project

```
git clone https://github.com/samarth/data-analysis-api.git
cd data-analysis-api
```

## Run locally

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Run tests

```
pytest test/test.py
```

## Run with Docker

### Run server

```
docker-compose up -d --build
```

### Run tests

```
docker-compose exec app pytest test/test.py
```

## API Documentation

Interactive API documentation (Swagger UI):
```
http://127.0.0.1:8000/docs
```

Alternative documentation (ReDoc):
```
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Data Analysis
- `GET /stats/overview` - Get statistical overview of all datasets
- `GET /stats/cars` - Detailed statistics for car dataset
- `GET /analysis/correlation` - Correlation analysis between variables
- `GET /analysis/distribution/{field}` - Distribution analysis for a specific field
- `GET /analysis/trends` - Trend analysis across datasets

### Data Operations
- `GET /data/cars` - Get all car data
- `GET /data/cars/filter` - Filter cars by criteria
- `POST /data/upload` - Upload new dataset for analysis
- `GET /data/summary` - Get summary statistics

### Visualization
- `GET /visualize/chart/{chart_type}` - Generate charts (bar, pie, line, scatter)
- `GET /visualize/distribution/{field}` - Distribution visualization

## Author

**Samarth**

## License

MIT License
