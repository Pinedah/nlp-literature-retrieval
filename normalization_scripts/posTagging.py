#Importamos la biblioteca spacy
import spacy
from spacy import displacy
#conda install -c conda-forge spacy-model-es_core_news_sm
#python -m spacy download es_core_news_sm

# ~ cadena = "Juan pisó fuertemente unos papeles importantes"
# ~ cadena = "Compré un dulce en la tienda a $8.5 pesos"
# ~ cadena = "Los perros ladraron la otra noche a unos coches rojos que pasaron por la calle."
# ~ cadena = "Juan estaba corriendo por el pasillo de la escuela superior de cómputo."
cadena = "Juan estaba corriendo por el pasillo de la ESCOM. El estaba feliz."
# ~ cadena = "Juan estaba corriendo por el pasillo de Microsoft."
# ~ cadena = "Juan estaba corriendo rápidamente por el pasillo amarillo de escuela superior de cómputo."



#Se carga el corpus para el tagger en español
nlp = spacy.load("es_core_news_sm")
#Se realiza el análisis de la cadena
doc = nlp(cadena)


for token in doc:
    # ~ print(tokebn.text, token.pos_, token.lemma_)
    print(token.text, token.pos_, token.dep_, token.lemma_)
    # ~ print(token.text, token.pos_, token.dep_, token.lemma_, spacy.explain(token.tag_), spacy.explain(token.dep_))
# ~ displacy.serve(doc, style="dep")    

print ("Entidades:")
for entity in doc.ents:
    print(entity.text, entity.label_)
