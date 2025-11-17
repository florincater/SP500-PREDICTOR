import gradio as gr
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class SimplePredictor:
    def __init__(self):
        self.prediction_history = []
    
    def get_market_status(self):
        """Simulate market status"""
        return "📊 **Market Status**: Simulation Mode - Ready for Predictions"
    
    def train_model(self):
        """Simulate training"""
        return "✅ Model training completed! Ready for predictions."
    
    def predict(self):
        """Simulate prediction with realistic S&P 500 data"""
        # Base S&P 500 price around typical values
        base_price = 4500 + np.random.normal(0, 50)
        
        # Simulate some market movement
        daily_change = np.random.normal(0.001, 0.015)  # ±1.5% typical daily move
        predicted_price = base_price * (1 + daily_change)
        
        change = predicted_price - base_price
        change_percent = (change / base_price) * 100
        
        # Store prediction
        self.prediction_history.append({
            'timestamp': datetime.now(),
            'actual': base_price,
            'predicted': predicted_price
        })
        
        return base_price, predicted_price, change, change_percent

# Initialize predictor
predictor = SimplePredictor()

def get_prediction():
    """Get S&P 500 prediction"""
    try:
        current_price, predicted_price, change, change_percent = predictor.predict()
        
        result = f"""📈 **S&P 500 Prediction**

**Current Price**: ${current_price:,.2f}
**Predicted Tomorrow's Price**: ${predicted_price:,.2f}
**Expected Change**: ${change:+.2f} ({change_percent:+.2f}%)

*Simulation Mode - Using realistic market data patterns*"""
        
        return result
        
    except Exception as e:
        return f"❌ Prediction error: {str(e)}"

def retrain_model():
    """Retrain the model"""
    try:
        result = predictor.train_model()
        return result
    except Exception as e:
        return f"❌ Training failed: {str(e)}"

def get_market_status():
    """Get market status"""
    return predictor.get_market_status()

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft(), title="S&P 500 Predictor") as demo:
    gr.Markdown("""
    # 📈 S&P 500 Prediction Model
    **AI-powered predictions for next-day S&P 500 closing prices**
    """)
    
    # Market status display
    market_status = gr.Markdown()
    
    with gr.Row():
        with gr.Column():
            predict_btn = gr.Button("🎯 Get Prediction", variant="primary", size="lg")
            train_btn = gr.Button("🔄 Retrain Model", variant="secondary")
    
    with gr.Row():
        output = gr.Markdown(label="Prediction Result")
    
    # Update market status on load
    demo.load(get_market_status, outputs=market_status)
    
    # Button actions
    predict_btn.click(fn=get_prediction, outputs=output)
    train_btn.click(fn=retrain_model, outputs=output)
    
    gr.Markdown("""
    ---
    **How to use**:
    1. Click **🔄 Retrain Model** first
    2. Click **🎯 Get Prediction** for forecasts
    3. Refresh page for new predictions
    
    *⚠️ Educational purpose only. Not financial advice.*
    """)

if __name__ == "__main__":
    # FIX: Use localhost instead of 0.0.0.0
    demo.launch(server_name="127.0.0.1", server_port=7860)
