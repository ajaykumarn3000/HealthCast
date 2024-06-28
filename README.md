# HealthCast - Predictive Healthcare Analytics

![healthcast_quxasp](https://github.com/ajaykumarn3000/HealthCast/assets/104309385/a51cf7f7-b54d-4bde-88df-f1bd1a2346d8)

## Overview

This repository contains the implementation of a machine learning-based system for disease diagnosis prediction. The system aims to improve the accuracy and speed of disease diagnosis by leveraging patient-reported symptoms and clinical data. By integrating advanced machine learning algorithms, the system provides healthcare professionals with a valuable decision support tool for timely intervention and improved patient care.

## Problem Statement

Current healthcare practices often struggle with timely and accurate disease diagnosis, leading to delayed treatment and suboptimal outcomes. Healthcare professionals face challenges in interpreting patient-reported symptoms and clinical data to make accurate diagnoses promptly. This results in significant implications for patient care, including prolonged suffering, increased healthcare costs, and sometimes even adverse health outcomes.

## Domain
- Domain : AI/ML

## Track
- Track : HealthCare

## Proposed Solution

Our project aims to address these challenges by developing a machine learning-based system for disease diagnosis prediction. By leveraging patient-reported symptoms and clinical data, along with advanced algorithms, we intend to enhance diagnostic accuracy and speed. The system will provide healthcare professionals with a valuable decision support tool, enabling earlier intervention and improved patient care.

## Implementation Plan

### 1. Data Collection and Preprocessing
   - Gather patient-reported symptoms and clinical data from reliable sources.
   - Preprocess the data to handle missing values, normalize features, and ensure data quality.

### 2. Machine Learning Model Development
   - Develop machine learning models trained on the collected data to predict diseases and probabiltiy of having diabetics based on symptoms and clinical data.
   - Experiment with various algorithms such as decision trees, Support vector machines, Logistic regression  to find the most effective approach.

### 3. Frontend Development
   - Develop a user-friendly frontend application using React.
   - Design an intuitive interface for users to input symptoms and receive disease predictions.

### 4. Backend Development
   - Implement a FastAPI REST API to handle requests from the frontend and communicate with the machine learning models.
   - Ensure scalability, security, and efficient handling of requests.

### 5. Integration and Testing
   - Integrate the frontend and backend components to form a cohesive system.
   - Conduct rigorous testing to validate the accuracy and reliability of disease predictions.
   - Perform user acceptance testing to ensure usability and user satisfaction.

### 6. Deployment and Maintenance
   - Deploy the system to production environment, ensuring high availability and scalability.
   - Monitor system performance and conduct regular maintenance to address any issues or updates.

## Demo
https://github.com/VishalRMahajan/HealthCast/assets/111660265/75210605-feb5-4c40-867d-580cb2fb65d4

If the video above isn't loading or playing, you can watch it here on [Youtube](https://youtu.be/acmxltnAErg?si=yUbxNqOOj8n1LpIH)


## Features

- **Machine Learning Models**: Utilizes machine learning models trained on patient-reported symptoms and clinical data to predict diseases accurately.
  
- **Integration with Healthcare Infrastructure**: The system is designed to seamlessly integrate into existing healthcare infrastructure, providing healthcare professionals with a valuable decision support tool.
  
- **Enhanced Diagnostic Accuracy and Speed**: By leveraging advanced algorithms, the system enhances diagnostic accuracy and speed, enabling earlier intervention and improved patient care.

## Project Structure

The project is organized into the following directories:

1. **`frontend`**: This directory contains a React application responsible for the user interface. It provides an intuitive interface for users to input symptoms and receive disease predictions.
2. **`backend`**: This directory contains the backend implementation of the system. It consists of a FastAPI REST API responsible for handling requests from the frontend and communicating with the machine learning models for disease prediction.
3. **`Machine Learning`**:  This directory contains the dataset used for training, the trained machine learning model extracted from Jupyter notebook, and the Jupyter notebook itself where the data was processed and the model was trained.

## Usage/Installations

1. **Frontend**:
   - Navigate to the `frontend` directory.
   - Install dependencies using `npm install`.
   - Start the development server using `npm start`.

2. **Backend**:
   - Remain in the root directory.
   - Install dependencies using `pip install -r requirements.txt`.
   - Start the FastAPI server using `uvicorn backend.main:app --reload`.
  
## Tech Stack
- Frontend
     - ReactJs
     - Tailwind CSS
       
- Backend
     - FastAPI
     - PostgreSQL
       
- Machine Learning
     - Scikit Learn
     - Jupyter

- VCS
   - Github
   - Git

- API Testing/Docs
   - Postman

## Contributors

- [Ajaykumar Nadar](https://github.com/ajaykumarn3000): Frontend Developer
- [Kevin Nadar](https://github.com/KXN2004): Backend Developer
- [Vishal Mahajan](https://github.com/VishalRMahajan): Machine Learning Engineer

## License

This project is licensed under the [MIT License](LICENSE.txt).
