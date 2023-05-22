
import spacy

nlp = spacy.load('en_core_web_sm')

# creating a list of garden-path sentences
gardenpathSentences = ["The old man the boat.", "The complex houses married and single soldiers and their families."]

# Add more sentences to the list
add_new_sentence1 = "Mary gave the child a Band-Aid."
gardenpathSentences.append(add_new_sentence1)

add_new_sentence2 = "That Jill is never here hurts."
gardenpathSentences.append(add_new_sentence2)

add_new_sentence3 = "The cotton clothing is made of grows in Mississippi."
gardenpathSentences.append(add_new_sentence3)

# Loop over the sentences, tokenize each sentence on the list and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(doc.text.split())

    for token in doc:
        print(token.text,token.orth, token.orth_, token.pos_, token.dep_, token.ent_type_)

        for ent in doc.ents:
            print(ent.label, ent.label_)


# Get an explanation of an entity and print it
entity_LOC = spacy.explain("LOC")
print(f"LOC:{entity_LOC}")

# Get an explanation of another entity and print it
entity_ORG = spacy.explain("ORG")
print(f"ORG:{entity_ORG}")


 # Examples of entities and their explanations

#  "LOC": Non-GPE locations, mountain ranges, bodies of water, etc.
#  "ORG": Companies, agencies, institutions, etc.

# The entities make sense in terms of the words associated with them:
# The location "Mississippi" is correctly identified as a "LOC" entity, and 
# the proper noun "Mary" is identified as a person or organization with the "ORG" entity.