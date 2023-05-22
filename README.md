### Natural Language Processing

Follow these steps:

● Read the introduction about garden path sentences and study a few of the examples on Wikipedia.

● Create a new Python file called garden.py.

● Find at least 2 garden path sentences from the web or think up your own.

● Store the sentences you have identified or created in a list called gardenpathSentences

● Add the following sentences to your list:

Mary gave the child a Band-Aid.
That Jill is never here hurts.
The cotton clothing is made of grows in Mississippi.

● Tokenise each sentence in the list and perform named entity recognition.

Examine how spaCy has categorised each sentence. Then, use spacy.explain to look up and print the meaning of entities that you don’t
understand. For example: print(spacy.explain("FAC"))
