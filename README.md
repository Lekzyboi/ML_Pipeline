
# ML Pipeline Project

A robust, modular, and production-ready machine learning pipeline that automates data ingestion, validation, transformation, training, evaluation, and deployment. This project integrates **MLflow** for experiment tracking and **DagsHub** for version control and artifact management.

---

## Key Features

- Modular pipeline with clearly defined stages
- **MLflow** integration for tracking experiments, metrics, and parameters
- **DagsHub** support for remote artifact storage and Git-based tracking
- YAML-based configuration for reproducibility
- Schema validation and data quality checks
- Model evaluation with automatic comparison and promotion logic
- Packaged with Docker for scalable deployment
- Flask web interface for real-time predictions and triggering training

---

## Project Structure

```
ML_Pipeline/
├── main.py                      # Executes the full training pipeline
├── app.py                       # Flask web app for UI interaction
├── Dockerfile                   # Docker build setup
├── params.yaml                  # Configurations for the pipeline
├── schema.yaml                  # Expected input schema
├── model.pkl                    # Output: trained model artifact
├── src/mlproject/
│   ├── components/              # Core logic for pipeline stages
│   ├── pipelines/               # Entry points for each pipeline stage
│   ├── config/                  # YAML loader and configuration manager
│   ├── entity/                  # Configuration data classes
│   ├── constants/               # Paths and constants
```

---

## Pipeline Stages

### 1. Data Ingestion
- Downloads or loads dataset
- Saves raw data into artifact directory

### 2. Data Validation
- Validates input data schema (`schema.yaml`)
- Logs results to console and MLflow

### 3. Data Transformation
- Converts raw data into train-ready format
- Saves processed datasets

### 4. Model Training
- Trains a supervised ML model
- Logs metrics and parameters to MLflow
- Stores final model as `model.pkl`

### 5. Model Evaluation
- Compares with existing model
- If better, logs and promotes it
- Tracks all metrics via MLflow and artifacts via DagsHub

---

## Web App Interface

Flask endpoints:

- `/` — Homepage
- `/train` — Triggers full pipeline
- `/predict` — Accepts 11 features via HTML form and returns prediction

### Features Required for Prediction:

- fixed_acidity, volatile_acidity, citric_acid, residual_sugar
- chlorides, free_sulfur_dioxide, total_sulfur_dioxide
- density, pH, sulphates, alcohol

---

## MLflow + DagsHub Integration

- Logs experiments to `mlruns/` directory or remote DagsHub tracking URI
- Tracks:
  - Hyperparameters
  - Metrics (accuracy, loss, etc.)
  - Artifacts (models, plots, etc.)
- Version control handled via Git/DVC and DagsHub

To set MLflow tracking URI:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/<user>/<repo>.mlflow
```

---

## Docker Setup

```bash
docker build -t ml-pipeline .
docker run -p 5000:5000 ml-pipeline
```

---

## 🛠️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run training

```bash
python main.py
```

### 3. Start web app

```bash
python app.py
```

---

## Config Files

- `params.yaml` — model parameters, data paths
- `schema.yaml` — defines required schema for validation
- `config/config.yaml` — supports remote paths and artifact storage

