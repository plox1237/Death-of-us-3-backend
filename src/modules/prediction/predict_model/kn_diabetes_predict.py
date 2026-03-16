# ===============================
# 1. Librerías
# ===============================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ===============================
# 2. Cargar datos
# ===============================
df = pd.read_csv("src/modules/prediction/data/Diabetes_prediction_balanced.csv")

# Limpiar posibles espacios en nombres de columnas
df.columns = df.columns.str.strip()

# ===============================
# 3. Separar variables
# ===============================
X = df.iloc[:, :-1]  # Todas menos la última
y = df.iloc[:, -1]   # Última columna como target

# ===============================
# 4. Dividir dataset
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# 5. Escalar (MUY IMPORTANTE en KNN)
# ===============================
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ===============================
# 6. Crear modelo KNN
# ===============================
model = KNeighborsClassifier(n_neighbors=5)  # k = 5 vecinos
model.fit(X_train, y_train)

# ===============================
# 7. Evaluar
# ===============================
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))
print("Reporte:\n", classification_report(y_test, y_pred))