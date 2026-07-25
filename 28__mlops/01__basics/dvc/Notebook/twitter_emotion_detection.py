import marimo

__generated_with = "0.23.13"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    import re
    import nltk
    import string
    from nltk.corpus import stopwords
    from nltk.stem import SnowballStemmer, WordNetLemmatizer
    from sklearn.feature_extraction.text import CountVectorizer
    import xgboost as xgb
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_score, recall_score, roc_auc_score

    return (
        CountVectorizer,
        WordNetLemmatizer,
        accuracy_score,
        nltk,
        np,
        pd,
        precision_score,
        re,
        recall_score,
        roc_auc_score,
        stopwords,
        train_test_split,
        xgb,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Ingestion
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('https://raw.githubusercontent.com/entbappy/Branching-tutorial/refs/heads/master/tweet_emotions.csv')

    df.head()
    return (df,)


@app.cell
def _(df):
    # delete tweet id
    df.drop(columns=['tweet_id'],inplace=True)
    df
    return


@app.cell
def _(df):
    final_df = df[df['sentiment'].isin(['happiness','sadness'])]
    return (final_df,)


@app.cell
def _(final_df):
    final_df.sample(5)
    return


@app.cell
def _(final_df):
    final_df.shape
    return


@app.cell
def _(final_df):
    final_df['sentiment'].replace({'happiness':1, 'sadness':0},inplace=True)
    return


@app.cell
def _(final_df):
    final_df.head()
    return


@app.cell
def _(final_df, train_test_split):
    train_data, test_data = train_test_split(final_df, test_size=0.2, random_state=42)
    return test_data, train_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Preprocessing
    """)
    return


@app.cell
def _(WordNetLemmatizer, nltk, np, re, stopwords):
    nltk.download('wordnet')
    nltk.download('stopwords')

    def lemmatization(text):
        lemmatizer= WordNetLemmatizer()

        text = text.split()

        text=[lemmatizer.lemmatize(y) for y in text]

        return " " .join(text)

    def remove_stop_words(text):
        stop_words = set(stopwords.words("english"))
        Text=[i for i in str(text).split() if i not in stop_words]
        return " ".join(Text)

    def removing_numbers(text):
        text=''.join([i for i in text if not i.isdigit()])
        return text

    def lower_case(text):

        text = text.split()

        text=[y.lower() for y in text]

        return " " .join(text)

    def removing_punctuations(text):
        ## Remove punctuations
        text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,،-./:;<=>؟?@[\]^_`{|}~"""), ' ', text)
        text = text.replace('؛',"", )

        ## remove extra whitespace
        text = re.sub('\s+', ' ', text)
        text =  " ".join(text.split())
        return text.strip()

    def removing_urls(text):
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        return url_pattern.sub(r'', text)

    def remove_small_sentences(df):
        for i in range(len(df)):
            if len(df.text.iloc[i].split()) < 3:
                df.text.iloc[i] = np.nan

    def normalize_text(df):
        df.content=df.content.apply(lambda content : lower_case(content))
        df.content=df.content.apply(lambda content : remove_stop_words(content))
        df.content=df.content.apply(lambda content : removing_numbers(content))
        df.content=df.content.apply(lambda content : removing_punctuations(content))
        df.content=df.content.apply(lambda content : removing_urls(content))
        df.content=df.content.apply(lambda content : lemmatization(content))
        return df

    def normalized_sentence(sentence):
        sentence= lower_case(sentence)
        sentence= remove_stop_words(sentence)
        sentence= removing_numbers(sentence)
        sentence= removing_punctuations(sentence)
        sentence= removing_urls(sentence)
        sentence= lemmatization(sentence)
        return sentence

    return normalize_text, normalized_sentence


@app.cell
def _(normalized_sentence):
    normalized_sentence("That's it? It's done already? This is one")
    return


@app.cell
def _(normalize_text, test_data, train_data):
    train_data_1 = normalize_text(train_data)
    test_data_1 = normalize_text(test_data)
    return test_data_1, train_data_1


@app.cell
def _(train_data_1):
    train_data_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### feature engineering
    """)
    return


@app.cell
def _(test_data_1, train_data_1):
    X_train = train_data_1['content'].values
    y_train = train_data_1['sentiment'].values
    X_test = test_data_1['content'].values
    y_test = test_data_1['sentiment'].values
    return X_test, X_train, y_test, y_train


@app.cell
def _(CountVectorizer, X_test, X_train):
    # Apply Bag of Words (CountVectorizer)
    vectorizer = CountVectorizer()

    # Fit the vectorizer on the training data and transform it
    X_train_bow = vectorizer.fit_transform(X_train)

    # Transform the test data using the same vectorizer
    X_test_bow = vectorizer.transform(X_test)
    return X_test_bow, X_train_bow


@app.cell
def _(X_train_bow, pd, y_train):
    train_df = pd.DataFrame(X_train_bow.toarray())

    train_df['label'] = y_train
    train_df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Model building
    """)
    return


@app.cell
def _(
    X_test_bow,
    X_train_bow,
    accuracy_score,
    classification_report,
    xgb,
    y_test,
    y_train,
):
    # Define and train the XGBoost model
    xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    xgb_model.fit(X_train_bow, y_train)
    _y_pred = xgb_model.predict(X_test_bow)
    # Make predictions
    accuracy = accuracy_score(y_test, _y_pred)
    classification_rep = classification_report(y_test, _y_pred)
    # Evaluate the model
    print('Accuracy:', accuracy)
    print('Classification Report:\n', classification_rep)
    return (xgb_model,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Model evaluation
    """)
    return


@app.cell
def _(
    X_test_bow,
    precision_score,
    recall_score,
    roc_auc_score,
    xgb_model,
    y_test,
):
    # Make predictions
    _y_pred = xgb_model.predict(X_test_bow)
    y_pred_proba = xgb_model.predict_proba(X_test_bow)[:, 1]
    precision = precision_score(y_test, _y_pred)
    # Calculate evaluation metrics
    recall = recall_score(y_test, _y_pred)
    auc = roc_auc_score(y_test, y_pred_proba)
    return auc, precision, recall


@app.cell
def _(auc, precision, recall):
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"AUC: {auc}")
    return


if __name__ == "__main__":
    app.run()
