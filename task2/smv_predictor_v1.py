import joblib
from ai_model import SimpleAIModel

# Train and save model artifact
model = SimpleAIModel()
joblib.dump(model, "smv_predictor_v1.joblib")

print("✅ Model trained and saved as smv_predictor_v1.joblib")
