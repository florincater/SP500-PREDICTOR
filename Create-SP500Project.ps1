# Create project structure
$projectRoot = "sp500-predictor"
mkdir $projectRoot, "$projectRoot\.github\workflows", "$projectRoot\model" -Force

# Create files with content
Set-Content -Path "$projectRoot\app.py" -Value @"
import gradio as gr
from model.model import SP500Predictor

# Initialize predictor
predictor = SP500Predictor()

def predict_sp500():
    \"\"\"Make S&P 500 prediction\"\"\"
    try:
        predictor.load_model()
        return "S&P 500 Prediction: Model loaded successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📈 S&P 500 Predictor")
    btn = gr.Button("🔮 Predict", variant="primary")
    output = gr.Textbox(label="Prediction Result")
    btn.click(fn=predict_sp500, outputs=output)

if __name__ == "__main__":
    demo.launch()
"@

Set-Content -Path "$projectRoot\requirements.txt" -Value @"
gradio>=4.0.0
pandas>=1.5.0
numpy>=1.21.0
scikit-learn>=1.2.0
yfinance>=0.2.0
plotly>=5.0.0
pickle-mixin>=1.0.0
"@

Set-Content -Path "$projectRoot\Dockerfile" -Value @"
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7860
CMD ["python", "app.py"]
"@

Set-Content -Path "$projectRoot\README.md" -Value @"
# S&P 500 Prediction Model

A machine learning model that predicts next-day S&P 500 closing prices.

## Features
- Real-time S&P 500 predictions
- Gradio web interface
- Automated Hugging Face deployment
"@

Set-Content -Path "$projectRoot\model\model.py" -Value @"
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle

class SP500Predictor:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        
    def train_model(self):
        \"\"\"Train the prediction model\"\"\"
        print("Training model...")
        # Add your training logic here
        return "Model training completed"
        
    def load_model(self):
        \"\"\"Load trained model\"\"\"
        try:
            # Simulate model loading
            return "Model loaded successfully - Ready for predictions!"
        except Exception as e:
            return f"Model loading failed: {str(e)}"
"@

Set-Content -Path "$projectRoot\.github\workflows\deploy.yml" -Value @"
name: Deploy to Hugging Face
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Deploy to HF
        env:
          HF_TOKEN: `${{ secrets.HF_TOKEN }}
        run: echo "Ready for Hugging Face deployment!"
"@

# Create empty weights file
New-Item -Path "$projectRoot\model\weights.pkl" -ItemType File

# Display success message and structure
Write-Host "✅ S&P 500 Predictor project created successfully!" -ForegroundColor Green
Write-Host "📁 Project location: $(Get-Location)\$projectRoot" -ForegroundColor Yellow
Write-Host "`n📂 Project Structure:" -ForegroundColor Cyan
tree $projectRoot /f
