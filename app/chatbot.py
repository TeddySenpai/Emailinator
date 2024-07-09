import spacy

nlp = spacy.load("en_core_web_sm")

def get_chatbot_response(message):
    doc = nlp(message)
    intent = "default_intent"  # Spacy doesn't provide intent out of the box, customize as needed
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return intent, entities
