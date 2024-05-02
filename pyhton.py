import sqlite3 as sql;
metin1="burak"

metin2="buhar"


baglan=sql.connect('sqlite.db')
imlec=baglan.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS metinler(metin TEXT)")

imlec.execute('INSERT INTO metinler (metin) VALUES(?)',(metin1,))
imlec.execute('INSERT INTO metinler(metin) VALUES(?)' ,(metin2,))
baglan.commit();
baglan.close();

def jaccard_similarity(metin1, metin2):
    # Metinleri kelimelere ayırma ve kümelerini oluşturma
    set1 = set(metin1.split())
    set2 = set(metin2.split())
    
    # Kesişim ve birleşim kümelerini bulma
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    # Jaccard benzerlik katsayısını hesaplama
    similarity = len(intersection) / len(union)
    return similarity

baglan=sql.connect('sqlite.db')
imlec=baglan.cursor()
imlec.execute('SELECT metin FROM metinler')
texts=[satir[0] for satir in imlec.fetchall()]

similarity_score = jaccard_similarity(texts[0], texts[1])
print(f"Jaccard Similarity: {similarity_score:.2f}")

with open('benzerlik_durumu.txt', 'w') as file:
    file.write(f"Jaccard Similarity: {similarity_score:.2f}")
baglan.commit();
baglan.close();