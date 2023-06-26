# importing spaCy
import spacy 
nlp = spacy.load('en_core_web_sm')

# storing garden path sentences in a list
garden_path_sentences = [
    'Southern European people like Italians like dishes like pasta',
    'When Fred eats food gets thrown',
    'Mary gave the child a Band-Aid',
    'That Jill is never here hurts',
    'The cotton clothing is made of grows in Mississippi'
]

# tokenising each sentence
tokenised_sentences = []
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    tokenised_sentences.append([(token, token.orth_, token.orth) for token in doc])
    print(tokenised_sentences)

# running named entity recognition on each sentence
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    print([(entity.text, entity.label_, entity.label) for entity in doc.ents])

# checking what the entities mean
entity_labels = ['GPE','PERSON','ORG','NORP','FAC']
for entity in entity_labels:
    print(f'{entity}: {spacy.explain(entity)}')

# GPE means countries, cities, states and it makes sense as Mississippi is a state.
# PERSON means people including fictional, makes sense as Mary is a person.
# NORP means nationalities or religious or political groups, makes sense as Italian is a nationality.