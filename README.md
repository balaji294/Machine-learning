# 📊 Mobile Price Prediction using Machine Learning

This machine learning project focuses on predicting or analyzing mobile phone data from Flipkart. The project involves data preprocessing, feature engineering, and applying machine learning algorithms to understand or predict outcomes from the dataset.

---

## 🗂️ Dataset

- **Source**: `Flipkart_Mobiles (1).csv`  
- **Features** include:
  - Mobile name
  - Specifications (like RAM, storage, camera)
  - Price
  - Ratings
  - Other related attributes

---

## 🧹 Preprocessing Steps

- Imported necessary Python libraries like `pandas`, `numpy`, `matplotlib`, `seaborn`
- Handled missing values and irrelevant columns
- Used `z-score` method for outlier detection
- Feature encoding where required

---

## 🤖 Machine Learning Models Used

- **Random Forest Regressor**
- **Decision Tree Regressor**

### 🧪 Evaluation Metrics
- Mean Squared Error (MSE)
- R-squared Score (R²)

---

## ✅ Results

- Models were trained using an 80/20 train-test split.
- Performance was measured using MSE and R² score.
- Random Forest performed better in most cases.

---

## 🖥️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook:
   ```bash
   jupyter notebook machine_learning_project_ac.ipynb
   ```

4. *(Optional)* If using Streamlit interface:
   ```bash
   streamlit run ml.py
   ```

---

## 📦 Requirements

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
```

---

## 📁 File Structure

```
├── machine_learning_project_ac.ipynb
├── Flipkart_Mobiles (1).csv
├── ml.py (if used for Streamlit)
├── README.md
└── requirements.txt
```
