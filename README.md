
---

**Live Demo:** [http://regression-forestfire-env.eba-2a4mjhih.eu-west-2.elasticbeanstalk.com](http://regression-forestfire-env.eba-2a4mjhih.eu-west-2.elasticbeanstalk.com)
## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Vineetnaik1611/Regression_forestfire.git
cd Regression_forestfire
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python application.py
```

The application will automatically open in your browser:
```
http://127.0.0.1:5000
```


## About the project

## Live Deployment

This machine learning model is deployed and running live on AWS Elastic Beanstalk:

**Live Demo:** [http://regression-forestfire-env.eba-2a4mjhih.eu-west-2.elasticbeanstalk.com](http://regression-forestfire-env.eba-2a4mjhih.eu-west-2.elasticbeanstalk.com)

### API Endpoints:
- `GET /` - Homepage
- `GET /health` - Health check
- `POST /predict` - Prediction endpoint

### Deployment Details:
- **Platform:** AWS Elastic Beanstalk
- **Region:** London (eu-west-2)
- **Instance:** t3.micro
- **Framework:** Flask
- **ML Library:** scikit-learn

This project is an **end-to-end machine learning web application** that predicts the **Fire Weather Index (FWI)** using meteorological and environmental data.  

Key steps and techniques used in this project:

- **Data Preparation:** Data cleaning, exploratory data analysis (EDA), and standardization.  
- **Feature Engineering:** Feature selection using correlation analysis.  
- **Modeling:** Applied multiple regression techniques including:
  - Ridge Regression & RidgeCV  
  - Lasso Regression & LassoCV  
  - ElasticNet & ElasticNetCV  
  - Linear Regression  
- **Model Deployment:** Pickled the best ML model and StandardScaler for scaling inputs.  
- **Web Application:** Built using **Flask**, providing a user-friendly interface to enter input data and get FWI predictions.  
- **Cloud Deployment:** Application deployed on **AWS Elastic Beanstalk**, with automated deployment using **AWS CodePipeline**.  

This project demonstrates the complete **ML workflow** from data preprocessing and model selection to deployment in a cloud environment.

