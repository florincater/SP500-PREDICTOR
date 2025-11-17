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
