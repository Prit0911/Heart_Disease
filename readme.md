# Heart Disease Prediction

A machine learning project that predicts whether a person has heart disease based on health, lifestyle, and lab-test attributes, using a Random Forest classifier.

## Dataset

The project uses `heart_disease.csv`, a dataset of ~10,000 patient records with 21 columns:

| Column | Description |
|---|---|
| Age | Patient age |
| Gender | Male / Female |
| Blood Pressure | Resting blood pressure |
| Cholesterol Level | Total cholesterol |
| Exercise Habits | Low / Medium / High |
| Smoking | Yes / No |
| Family Heart Disease | Yes / No |
| Diabetes | Yes / No |
| BMI | Body mass index |
| High Blood Pressure | Yes / No |
| Low HDL Cholesterol | Yes / No |
| High LDL Cholesterol | Yes / No |
| Alcohol Consumption | Low / Medium / High |
| Stress Level | Low / Medium / High |
| Sleep Hours | Average hours of sleep |
| Sugar Consumption | Low / Medium / High |
| Triglyceride Level | Triglyceride level |
| Fasting Blood Sugar | Fasting blood sugar level |
| CRP Level | C-reactive protein level |
| Homocysteine Level | Homocysteine level |
| **Heart Disease Status** | Target — Yes / No |

## Project Structure

- `heart_disease.ipynb` — Jupyter notebook containing all data loading, preprocessing, model training, and evaluation steps.
- `heart_disease.csv` — Raw dataset (not included; place it in the project root before running).

## Workflow

1. **Load data** with pandas (`pd.read_csv`).
2. **Clean data** by dropping rows with missing values (`df.dropna()`), reducing the dataset from ~10,000 to ~7,067 rows.
3. **Split features/target**: `X` = all columns except `Heart Disease Status`; `y` = `Heart Disease Status`.
4. **Train/test split**: 70/30 split, stratified on the target, `random_state=42`.
5. **Train a model**: `RandomForestClassifier(random_state=42)`.
6. **Evaluate** using accuracy, a classification report (precision/recall/F1), and a confusion matrix.
7. **Predict on new input** via a helper function, `predict_from_input()`.

## Requirements

```
numpy
pandas
matplotlib
scikit-learn
```

Install with:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Usage

1. Place `heart_disease.csv` in the same directory as the notebook.
2. Open and run `heart_disease.ipynb` cell by cell (or `Run All`).
3. Review the printed accuracy, classification report, and confusion matrix.
4. Use `predict_from_input()` to score a new patient record.

## Known Issues / To-Do

This notebook has a few rough edges worth fixing before relying on it:

- **Categorical features are not encoded.** Columns like `Gender`, `Smoking`, `Exercise Habits`, etc. are still strings when passed to `RandomForestClassifier.fit()`, which raises `ValueError: could not convert string to float: 'Male'`. These need to be encoded first (e.g. `pd.get_dummies()` or `OneHotEncoder`/`LabelEncoder`) before training.
- **`StandardScaler` is imported but never used.** Random Forests don't strictly need scaled features, but if it's meant to be used, add the scaling step for `X_train`/`X_test`.
- **The reported accuracy (~99%) and confusion matrix predate the encoding fix** — they come from an earlier, differently-ordered run of the cells (note the non-sequential `execution_count` values in the notebook) and should be re-verified once the string-to-float issue above is resolved.
- **`predict_from_input()`'s sample input uses different feature names** (`age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal` — the classic UCI Cleveland heart-disease schema) that don't match this dataset's actual columns (`Age`, `Gender`, `Blood Pressure`, ...). This function needs to be rewritten to accept a dict keyed by the real column names in `X.columns`.

## Model

- **Algorithm**: Random Forest Classifier (`sklearn.ensemble.RandomForestClassifier`)
- **Evaluation metrics**: Accuracy, Precision, Recall, F1-score, Confusion Matrix

## License

Add a license of your choice here.

## Author : Prit Gajjar
Email: pritgajjar0911@gmail.com