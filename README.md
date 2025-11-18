# 🌱 Crop Prediction System

A Streamlit-based web application for predicting suitable crops based on soil nutrients and environmental conditions using Machine Learning models.

## 📋 Features

- **Interactive UI**: Clean, user-friendly interface with purple gradient theme
- **Multiple ML Models**: Choose between Random Forest and Logistic Regression
- **Real-time Predictions**: Instant crop recommendations based on input parameters
- **Input Validation**: Built-in validation for all soil and environmental factors
- **Responsive Design**: Works seamlessly on different screen sizes

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **Python**: Core programming language
- **Scikit-learn**: Machine learning models
- **Pydantic**: Data validation (FactorsData model)

## 📦 Installation

1. **Clone the repository**
```bash
git clone <https://github.com/AhmedSho3ib/Crop-Recommendation>
cd <project-directory>
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📝 Requirements

Create a `requirements.txt` file with the following dependencies:

```
pydantic==2.0.0
fastapi==0.115.6
uvicorn==0.34.0
scikit-learn==1.3.2
python-dotenv==1.0.1
matplotlib==3.10.0
seaborn==0.13.2
streamlit==1.28.0
```

## 🚀 Usage
### 🌐 Online Demo (Recommended):
The application is deployed and ready to use online:

**👉 [Launch Crop Prediction App](https://crop-recommendation1.streamlit.app/)**

Simply click the link above to start making predictions immediately - no installation required!

### 💻 Local Development:

1. **Run the Streamlit app**
```bash
streamlit run streamlit-app.py
```

2. **Access the application**
   - Open your browser and navigate to `http://localhost:8501`
   - The app will automatically open in your default browser

3. **Make predictions**
   - Select your preferred ML model (Random Forest or Logistic Regression)
   - Enter soil and environmental parameters:
     - Nitrogen (N)
     - Phosphorus (P)
     - Potassium (K)
     - Temperature (°C)
     - Humidity (%)
     - pH Level
     - Rainfall (mm)
   - Click "Get Prediction" to see results

## 📊 Input Parameters

| Parameter | Description | Range/Constraint |
|-----------|-------------|------------------|
| **Nitrogen (N)** | Nitrogen content in soil | ≥ 0 |
| **Phosphorus (P)** | Phosphorus content in soil | ≥ 0 |
| **Potassium (K)** | Potassium content in soil | ≥ 0 |
| **Temperature** | Environmental temperature | 8-50°C |
| **Humidity** | Atmospheric moisture level | 0-100% |
| **pH** | Soil acidity/alkalinity | 0-14 |
| **Rainfall** | Annual or seasonal rainfall | ≥ 0 mm |

## 🗂️ Project Structure

```
project/
│   .env
│   .env.example
│   main.py
│   requirements.txt
│   streamlit-app.py
│
├───.vscode
│       settings.json
│
├───datasets
│       Crop_recommendation.csv
│
├───models
│       encoder_preprocessor.pkl
│       logistic_regression_model.pkl
│       random_forest_model.pkl
│       scaler_preprocessor.pkl
│
├───notebooks
│       metadata.txt
│       notebook.ipynb
│
├───utils
│   │   config.py
│   │   FactorsData.py
│   │   inference.py
│   │   __init__.py
│   │
│   └───__pycache__
│           config.cpython-313.pyc
│           FactorsData.cpython-313.pyc
│           inference.cpython-313.pyc
│           __init__.cpython-313.pyc
│
└───__pycache__
        main.cpython-313.pyc
```

## 🤖 Models

The application supports two prediction models:

1. **Random Forest** 🌲
   - Ensemble learning method
   - High accuracy for complex patterns
   - Default selection

2. **Logistic Regression** 📈
   - Linear classification model
   - Fast and interpretable
   - Good for simpler patterns

## 🔧 Configuration

The application loads pre-trained models and preprocessors from `utils/config.py`:

- `random_forest_model`: Random Forest classifier
- `logistic_regression_model`: Logistic Regression classifier
- `scaler_preprocessor`: Feature scaling transformer
- `encoder_preprocessor`: Label encoding transformer

## 🎨 UI Features

- **Clean Modern Design**: Minimalist interface with intuitive layout
- **Interactive Model Selection**: Toggle buttons with visual highlighting for selected model
- **Two-Column Input Form**: Organized layout for efficient data entry
- **Real-time Validation**: Instant feedback on input constraints and ranges
- **Helpful Tooltips**: Descriptive hints for each input field
- **Loading Indicators**: Visual spinner during model prediction
- **Error Handling**: Clear, user-friendly error messages
- **Success Feedback**: Confirmation messages and JSON result display
- **Responsive Design**: Adapts to different screen sizes seamlessly

## 👥 Contributors

- **[Ahmed Shoaib]** - [@AhmedSho3ib](https://github.com/AhmedSho3ib)
- **[Abdeltawab Mahmoud]** - [@Abdomahmoud7](https://github.com/Abdomahmoud7)
