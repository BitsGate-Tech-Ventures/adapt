import os
import pandas as pd
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from scipy.sparse import vstack
import joblib

def load_updated_model(model_output_path):
    # Load the updated model
    return joblib.load(model_output_path)

def load_updated_dataset(df_output_path):
    # Load the updated dataset
    with open(df_output_path, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]
    return pd.DataFrame(data)

def preprocess_text(text, lemmatizer, stop_words):
    if isinstance(text, dict):
        text = json.dumps(text)  # Convert dict to JSON string if necessary
    tokens = word_tokenize(text)
    cleaned_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha() and token.lower() not in stop_words]
    return ' '.join(cleaned_tokens)

def vectorize_text(df, vectorizer, lemmatizer, stop_words):
    df['Processed_Description'] = df['Description'].apply(lambda text: preprocess_text(text, lemmatizer, stop_words))
    return vectorizer.fit_transform(df['Processed_Description'])

def predict_nmap_command(query, vectorizer, model, lemmatizer, stop_words):
    processed_query = preprocess_text(query, lemmatizer, stop_words)
    query_vector = vectorizer.transform([processed_query])
    predicted_command = model.predict(query_vector)
    return predicted_command[0]

def log_feedback(query, predicted_output, feedback):
    with open("feedback_log.txt", "a") as f:
        f.write(f"Query: {query}\n")
        f.write(f"Predicted Output: {predicted_output}\n")
        f.write(f"Feedback: {feedback}\n")
        f.write("="*30 + "\n")

def get_user_input(input_func, vectorizer, model, lemmatizer, stop_words):
    user_query = input_func("Please enter your query (type 'exit' to terminate): ")
    
    if user_query.lower() == 'exit':
        print("Terminating...")
        return None
    
    predicted_output = predict_nmap_command(user_query, vectorizer, model, lemmatizer, stop_words)
    print(f"Predicted Nmap command: nmap {predicted_output}")
    
    feedback = input_func("Was this output correct? Type 'yes', 'no', or 'close': ")
    
    # Log feedback
    log_feedback(user_query, predicted_output, feedback)
    
    # Update model if feedback is provided
    if feedback == 'no':
        # Add the current query to the training set
        current_query_vector = vectorizer.transform([preprocess_text(user_query, lemmatizer, stop_words)])
        global X, df
        X = vstack([X, current_query_vector])
        df = pd.concat([df, pd.DataFrame({'Command': [predicted_output], 'Description': [user_query]})], ignore_index=True)
        model.fit(X, df['Command'])
        print("Model updated based on user feedback.")
    
    return user_query

def run_interactive_mode(input_func, vectorizer, model, lemmatizer, stop_words):
    while True:
        user_query = get_user_input(input_func, vectorizer, model, lemmatizer, stop_words)
        if user_query is None:
            break
    print("Session ended.")

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    
    model_output_path = os.path.join(script_dir, "nmap_command_classifier.pkl")
    df_output_path = os.path.join(script_dir, "nmap_commands_updated.json")

    # Load the updated model and dataset
    model = load_updated_model(model_output_path)
    df = load_updated_dataset(df_output_path)

    # Preprocessing
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    global X
    X = vectorize_text(df, vectorizer, lemmatizer, stop_words)

    # Run interactive mode
    run_interactive_mode(input, vectorizer, model, lemmatizer, stop_words)

if __name__ == "__main__":
    main()
