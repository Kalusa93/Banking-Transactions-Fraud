# 🚨 Detección de Fraude en Transacciones Bancarias

Este proyecto utiliza **Python, Pandas, Seaborn y Scikit-learn** para analizar y predecir fraudes en un dataset de transacciones financieras.  
El objetivo es detectar operaciones fraudulentas mediante **análisis exploratorio de datos (EDA)** y un modelo de **Regresión Logística** con balanceo de clases.

---

## 📂 Dataset
- **Fuente**: `AIML Dataset.csv` (6.3 millones de transacciones).  
- **Características principales**:
  - `step`: unidad de tiempo de la transacción.  
  - `type`: tipo de operación (`PAYMENT`, `TRANSFER`, `CASH_OUT`, etc.).  
  - `amount`: monto de la transacción.  
  - `nameOrig` / `nameDest`: cuentas origen y destino.  
  - `oldbalanceOrg` / `newbalanceOrig`: balances de la cuenta origen antes y después de la operación.  
  - `oldbalanceDest` / `newbalanceDest`: balances de la cuenta destino antes y después.  
  - `isFraud`: etiqueta objetivo (1 = fraude, 0 = legítima).  
  - `isFlaggedFraud`: transacciones marcadas como sospechosas por el sistema.  

El dataset está **altamente desbalanceado**: solo ~0.13% de transacciones son fraudulentas.

---

## 🔎 Análisis Exploratorio (EDA)
Se realizaron los siguientes pasos:

1. **Revisión inicial**  
   - 6,362,620 transacciones  
   - 11 variables  
   - Sin valores nulos  

2. **Distribución de tipos de transacciones**  
   - Mayoría: `PAYMENT` y `CASH_OUT`.  
   - Fraudes concentrados en `TRANSFER` y `CASH_OUT`.  

3. **Fraudes en el tiempo**  
   - No hay dependencia fuerte con el tiempo (`step`).  

4. **Análisis de montos**  
   - Se aplicó escala logarítmica para visualizar la distribución.  
   - Los fraudes suelen involucrar montos más altos.  

5. **Nuevas features**  
   - `balanceDiffOrig` = diferencia en cuenta origen.  
   - `balanceDiffDest` = diferencia en cuenta destino.  

6. **Correlaciones**  
   - Se generó matriz de correlación con `heatmap`.  
   - `amount` muestra ligera relación con `isFraud`.

---

## ⚙️ Preprocesamiento
- Variables categóricas (`type`) → **OneHotEncoder**  
- Variables numéricas → **StandardScaler**  
- Eliminación de columnas irrelevantes (`nameOrig`, `nameDest`, `step`, `isFlaggedFraud`).  

Se utilizó un **ColumnTransformer** dentro de un `Pipeline` para asegurar consistencia en train/test.

---

## 🤖 Modelado
Se implementó un modelo de **Regresión Logística** con:
- `class_weight="balanced"` → manejo de clases desbalanceadas.  
- `max_iter=1000` → para asegurar convergencia.  

### Resultados:
- **Accuracy**: ~95%  
- **Recall en clase fraude**: 0.93  
- **Precision en clase fraude**: baja (~0.02) debido al desbalance extremo.  
- **Confusion Matrix**:

[[1805925, 100397], # No Fraude
[ 162, 2302]] # Fraude

Esto significa que el modelo **detecta casi todos los fraudes (alto recall)**, pero genera muchos falsos positivos.

---

## 📊 Conclusiones
- La regresión logística con balanceo es capaz de **detectar la mayoría de los fraudes**.  
- Sin embargo, la **precisión baja** indica que hay que explorar otros modelos (árboles, random forest, gradient boosting).  
- El EDA reveló que **TRANSFER y CASH_OUT** son las operaciones más críticas a monitorear.  

---

## 🚀 Próximos pasos
- Probar modelos más robustos: Random Forest, XGBoost, Gradient Boosting.  
- Usar técnicas de **undersampling / oversampling** (SMOTE) para mejorar la precisión.  
- Implementar métricas adicionales como ROC-AUC y PR-AUC.  

---

## 🛠️ Tecnologías
- Python 3.x  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

---

## ✍️ Autor
Proyecto desarrollado por **Lucas Leguizamón** como práctica de Machine Learning aplicado a detección de fraude financiero.
