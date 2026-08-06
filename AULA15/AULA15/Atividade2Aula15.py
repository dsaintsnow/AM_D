"""2. Módulo random
Crie uma lista com 10 nomes.
Escolha um nome aleatoriamente da lista.
Embaralhe a ordem dos nomes na lista."""

import random
nomes = ["Débora","Pollyana","Maria","Evelyn","Joana","Lilia","Amanda","Alice","Teresa","Erika"]
print("Nome sorteado:")
print(random.choice(nomes))
random.shuffle(nomes)
print("Lista embaralhada:")
print(nomes)
