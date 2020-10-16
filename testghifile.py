def GhiFile(str):
    file = open('filetk.txt', 'a', encoding ='utf-8')
    file.write(str)
    file.write('\n')
    file.close()

# GhiFile('quyetdaica')
# GhiFile('tao la quyet')
import random

name = ['quyet', 'van', 'nguyen']
sorandom = str(random.randrange(999,10000))
user ='nvq' + random.choice(name) + sorandom
print(user)

GhiFile(user)