import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import numpy as np
import librosa
from tensorflow.keras.models import load_model


# Cargar modelo
MODEL_PATH= "models/audio_classification.keras"
model = load_model(MODEL_PATH)


def extract_features(file):
    try:
        audio, sample_rate = librosa.load(file, res_type='kaiser_best')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=60)
        mfccs_scaled = np.mean(mfccs.T, axis=0)
        return np.expand_dims(mfccs_scaled, axis=(0, -1))

    except Exception as e:
        print(f"Error al procesar el audio: {e}")
        return None

def predict(file_path):
    features = extract_features(file_path)

    if features is None:
        return "500 Error processing"

    prediction = model.predict(features)

    print(f"Predicción cruda: {prediction}")  # 🚀 Para depuración
    print(f"Forma de la predicción: {prediction.shape}")  # 🚀 Para verificar dimensiones

    predicted_class = np.argmax(prediction, axis=-1)  # Asegurar correcto eje
    print(f"Clase predicha: {predicted_class}")  # 🚀 Depuración

    class_labels = ['Do not have', 'Have']

    return class_labels[int(predicted_class)]

print("todo salio bien parece")
