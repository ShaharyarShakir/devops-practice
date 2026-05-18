import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import marimo as mo
    import seaborn as sns
    import matplotlib.pyplot as plt

    return mo, np, pd, plt, sns


@app.cell
def _(pd):
    raw = pd.read_csv(
        "https://huggingface.co/datasets/shaharyarshakir/ml-datasets/raw/main/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    )
    return (raw,)


@app.cell
def _(pd, raw):
    def _transform(df):
        df = df.copy()

        # Drop useless ID column
        df = df.drop("customerID", axis=1)

        # Fix TotalCharges — has stray spaces that make it object dtype
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

        # Binary encode yes/no and gender columns
        binary_cols = ["gender", "Partner", "Dependents", "PhoneService", "PaperlessBilling", "Churn"]
        df[binary_cols] = df[binary_cols].replace({"Yes": 1, "No": 0, "Male": 1, "Female": 0})

        # One-hot encode multi-category columns
        multi_cat_cols = [
            col for col in [
                "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup",
                "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies",
                "Contract", "PaymentMethod",
            ]
            if col in df.columns
        ]
        if multi_cat_cols:
            df = pd.get_dummies(df, columns=multi_cat_cols, drop_first=True)

        # Convert any leftover bool columns (from get_dummies) to int
        bool_cols = df.select_dtypes(include="bool").columns
        df[bool_cols] = df[bool_cols].astype(int)
        df['No_internet_service'] = (
        df['OnlineSecurity_No internet service'] |
        df['OnlineBackup_No internet service'] |
        df['DeviceProtection_No internet service'] |
        df['TechSupport_No internet service'] |
        df['StreamingTV_No internet service'] |
        df['StreamingMovies_No internet service']
    ).astype(int)

    # Drop the original redundant dummies
        drop_cols = [col for col in df.columns if 'No internet service' in col]
        df = df.drop(columns=drop_cols)

    # Handle PhoneService redundancy
        if 'MultipleLines_No phone service' in df.columns:
            df['No_phone_service'] = df['MultipleLines_No phone service'].astype(int)
            df = df.drop(columns=['MultipleLines_No phone service'])

        return df

    df = _transform(raw)
    return (df,)


@app.cell
def _(df):
    # Quick sanity check — shape and dtypes
    print(df.shape)
    return


@app.cell
def _(df):
    df.head(1)
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    # Null counts — important after TotalCharges coercion
    null_summary = df.isnull().sum()
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df, plt, sns):
    # Compute correlation matrix only for numeric columns
    corr_matrix = df.corr(numeric_only=True)

    # Focus on correlation with Churn
    churn_corr = corr_matrix[['Churn']].sort_values(by='Churn', ascending=False)

    # Plot heatmap
    plt.figure(figsize=(4, 12))
    sns.heatmap(churn_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation of Features with Churn')
    plt.show()
    return


@app.cell
def _(df, np, pd):
    # Run VIF
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    _X = df.drop(columns=['Churn'])
    bool_cols = _X.select_dtypes(include='bool').columns
    _X[bool_cols] = _X[bool_cols].astype(int)
    _X = _X.replace([np.inf, -np.inf], np.nan)
    _X = _X.dropna()

    vif_data = pd.DataFrame()
    vif_data['feature'] = _X.columns
    vif_data['VIF'] = [variance_inflation_factor(_X.values, i) for i in range(_X.shape[1])]
    vif_data = vif_data.sort_values(by='VIF', ascending=False)

    print(vif_data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Machine learning
    """)
    return


@app.cell
def _(df):
    # We have a class imbalance problem
    # Given your imbalance (27% churners), class weighting + threshold tuning is probably enough
    df['Churn'].value_counts()
    return


@app.cell
def _():
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    import lightgbm as lgb
    from sklearn.metrics import classification_report
    import time

    return RandomForestClassifier, classification_report, train_test_split


@app.cell
def _(df):
    X = df.drop(columns=['Churn'])
    y = df['Churn']
    return X, y


@app.cell
def _(X, train_test_split, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    THRESHOLD = 0.3  # lower than 0.5 to boost recall (see next to choose the right value)
    return THRESHOLD, X_test, X_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### RandomForest Classifier
    """)
    return


@app.cell
def _(
    RandomForestClassifier,
    THRESHOLD,
    X_test,
    X_train,
    classification_report,
    y_test,
    y_train,
):
    rf = RandomForestClassifier(
        n_estimators=300,
        class_weight='balanced',   # handles imbalance for you
        random_state=42,
        n_jobs=-1
    )
    rf.fit(X_train, y_train)

    proba = rf.predict_proba(X_test)[:, 1]
    y_pred = (proba >= THRESHOLD).astype(int)

    print(classification_report(y_test, y_pred, digits=3))
    return (proba,)


@app.cell
def _(proba, y_test):
    from sklearn.metrics import precision_score, recall_score, f1_score

    print("Threshold tuning for RandomForest")

    print(f"{'Thresh':<8}{'Prec_1':<8}{'Rec_1':<8}{'F1_1':<8}")
    for thresh in [0.25, 0.30, 0.35, 0.40, 0.45, 0.50]:
        preds = (proba >= thresh).astype(int)
        prec = precision_score(y_test, preds, pos_label=1)
        rec = recall_score(y_test, preds, pos_label=1)
        f1 = f1_score(y_test, preds, pos_label=1)
        print(f"{thresh:<8}{prec:<8.3f}{rec:<8.3f}{f1:<8.3f}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
