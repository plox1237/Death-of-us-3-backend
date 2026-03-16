# ===============================
# 1. Importar librerías
# ===============================
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ===============================
# 2. Cargar el dataset
# ===============================
df = pd.read_csv("src/modules/prediction/data/Diabetes_prediction.csv")

print("Primeras filas:")
print(df.head())

print("\nColumnas:")
print(df.columns)

# ===============================
# 3. Separar variables
# ===============================
# Suponiendo que la columna objetivo se llama 'Outcome'
# (Si se llama diferente, cambia el nombre aquí)

X = df.drop("Diagnosis", axis=1)  # Variables predictoras
y = df["Diagnosis"]               # Variable objetivo

# ===============================
# 4. Dividir datos en entrenamiento y prueba
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# 5. Escalar datos (opcional pero recomendable)
# ===============================
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ===============================
# 6. Crear y entrenar modelo
# ===============================
model = model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)
model.fit(X_train, y_train)

# ===============================
# 7. Evaluar modelo
# ===============================
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nMatriz de confusión:\n", confusion_matrix(y_test, y_pred))
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred))

joblib.dump(model, "modelo_diabetes.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Modelo entrenado y guardado correctamente.")