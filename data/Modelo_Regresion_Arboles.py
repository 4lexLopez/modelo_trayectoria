import pandas as pd


# Cargar el archivo CSV (reemplaza 'ruta/a/tu/archivo.csv' con la ubicación real de tu archivo)
data = pd.read_csv('resultado_comparacion_completa.csv')

# Ver las primeras filas para inspeccionar los datos
print(data.head())

# Crear la variable dependiente 'abandono' basada en la columna 'trayectoria'
data['abandono'] = data['mensaje_trayectoria'].apply(lambda x: 0 if x == 'TRAYECTORIA' else 1)

# Convertir la columna 'mensMensaje_Comparacionaje' en una variable categórica:
# 'igual' -> 0 (no cambió de colegio), 'diferente' -> 1 (cambió de colegio)
data['mensaje'] = data['Mensaje_Comparacion'].apply(lambda x: 0 if x == 'IGUAL' else 1)

# Verificamos cómo quedaron las columnas
print(data[['Mensaje_Comparacion', 'mensaje_trayectoria', 'abandono']].head())

# Variables independientes: grados de los años (2019-2024)
X = data[['Grado_2019', 'Grado_2020', 'Grado_2021', 'Grado_2022', 'Grado_2023', 'Grado_2024', 'mensaje']]  # Años de los grados y mensaje
y = data['abandono']  # Variable dependiente: abandono (1 si abandonó, 0 si completó)

# Dividir los datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ver cómo quedaron los conjuntos de entrenamiento y prueba
print(f"Datos de entrenamiento: {X_train.shape[0]}")
print(f"Datos de prueba: {X_test.shape[0]}")


# Regresión Logística:
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Crear el modelo de regresión logística
modelo_logistico = LogisticRegression(max_iter=1000)  # Ajuste de max_iter por si el modelo no converge rápido
modelo_logistico.fit(X_train, y_train)

# Predicciones en el conjunto de prueba
y_pred_logistico = modelo_logistico.predict(X_test)

# Evaluar el modelo
print("Precisión Regresión Logística:", accuracy_score(y_test, y_pred_logistico))
print(classification_report(y_test, y_pred_logistico))

from sklearn.tree import DecisionTreeClassifier


# Crear el modelo de árbol de decisión
modelo_arbol = DecisionTreeClassifier(random_state=42)
modelo_arbol.fit(X_train, y_train)

# Predicciones en el conjunto de prueba
y_pred_arbol = modelo_arbol.predict(X_test)

# Evaluar el modelo
print("Precisión Árbol de Decisión:", accuracy_score(y_test, y_pred_arbol))
print(classification_report(y_test, y_pred_arbol))

#Visualización del Árbol de Decisión (Opcional):

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Graficar el árbol de decisión
plt.figure(figsize=(12, 8))
plot_tree(modelo_arbol, filled=True, feature_names=X.columns, class_names=['No abandono', 'Abandono'], rounded=True)
plt.show()