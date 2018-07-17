from pymagnitude import Magnitude
vectors = Magnitude('GoogleNews-vectors-negative300.magnitude')
print("cat" in vectors, "rabbit" in vectors)
print(vectors.similarity("uberx", "uberxl"))
print(vectors.most_similar(positive=["cow", "pork"], negative="pig"))