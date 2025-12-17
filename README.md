🏦 Bank Retirement Classification.    

Production-Ready Machine Learning Package.

This repository contains a production-ready machine learning package for bank retirement classification.
The project demonstrates how a classical applied ML problem in the banking / finance domain can be implemented as a maintainable, testable, and distributable Python package, following software engineering and MLOps-oriented best practices.

Key focus areas:
* clean and modular project structure
* reproducible and deterministic training
* automated testing
* static code analysis
* packaging and distribution workflow

📌 Project Goals
* Build an end-to-end ML pipeline for bank retirement classification
* Ensure reproducibility and deterministic model training
* Emphasize interpretability and stability, important in financial applications
* Apply software engineering practices to ML:
    * testing
    * linting
    * type checking
    * packaging
* Provide a clear example of an ML → package → build workflow in a banking context

📊 Dataset
* Domain: Banking / Finance
* Task: Binary classification
* Target: Client retirement / exit indicator
* Features: demographic and financial attributes
The dataset is intentionally included in the repository because:
* it is small and lightweight
* it is publicly available
* it enables full reproducibility of training and tests

🧠 Modeling Approach
The project focuses on classical and interpretable machine learning models, which are commonly required in banking and financial domains.
Implemented concepts include:
* feature engineering
* structured preprocessing pipeline
* deterministic training
* validation and evaluation logic
* stored trained artifacts for inference
Training, prediction, and validation logic are clearly separated to support maintainability and extensibility.


📁 Project Structure
```
bank-retirement-classification/
├── __init__.py
├── bank_classification_model
│   ├── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   └── core.py
│   ├── config.yml
│   ├── datasets
│   │   ├── __init__.py
│   │   └── Bank_Customer_retirement_TP.csv
│   ├── pipeline.py
│   ├── predict.py
│   ├── processing
│   │   ├── __init__.py
│   │   ├── data_manager.py
│   │   └── validation.py
│   ├── train_pipeline.py
│   ├── trained_models
│   │   └── __init__.py
│   └── VERSION
├── MANIFEST.in
├── mypy.ini
├── pyproject.toml
├── requirements
│   ├── requirements.txt
│   ├── test_requirements.txt
│   └── typing_requirements.txt
├── setup.py
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── conftest.cpython-311-pytest-7.4.4.pyc
│   │   ├── test_features.cpython-311-pytest-7.4.4.pyc
│   │   └── test_prediction.cpython-311-pytest-7.4.4.pyc
│   ├── conftest.py
│   ├── test_features.py
│   └── test_prediction.py
└── tox.ini
```


✅ Automated Workflow (tox)

This project uses tox to standardize all workflows.

Run full test suite and code checks
```
tox
```
This executes:
* model training
* unit tests (pytest)
* code quality checks (flake8, isort, black, mypy)

Train model only
```
tox -e train
```

Run package tests only
```
tox -e test_package
```


🧪 Testing
Unit tests validate:
* feature engineering logic
* prediction pipeline behavior
* consistency of model outputs
Tests are deterministic and reproducible. Model training is executed as part of the test environment.


📦 Build Package

After tests pass, build distributable artifacts:
```
python3 -m build
```

This creates:
* .whl (wheel)
* .tar.gz (source distribution) Artifacts are placed in the dist/ directory.


🧠 Why This Structure Matters
This repository demonstrates:
* separation of concerns (data / features / training / inference)
* testable and maintainable ML code
* reproducible experiments
* readiness for CI/CD integration
* transition from research-oriented ML to a production-ready package

📌 Intended Audience
* ML Engineers
* Data Scientists working with financial data
* Teams interested in production ML and MLOps foundations
* Recruiters reviewing real-world ML engineering work

🚧 Project Status
The package is stable and fully functional.
Possible future extensions:
* advanced model explainability (SHAP)
* probability calibration
* deployment examples (API / batch inference)
