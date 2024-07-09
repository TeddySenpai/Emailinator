import spacy

nlp = spacy.load("en_core_web_sm")

def generate_response(message):
    doc = nlp(message)
    entities = [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    return entities
