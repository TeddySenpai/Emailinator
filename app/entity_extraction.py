import spacy

# Load the Spacy model
nlp = spacy.load("en_core_web_sm")

# Define a function to process text and extract entities
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
if __name__ == "__main__":
    text = "Apple is looking at buying U.K. startup for $1 billion"
    entities = extract_entities(text)
    print(entities)  # Output: [('Apple', 'ORG'), ('U.K.', 'GPE'), ('$1 billion', 'MONEY')]
