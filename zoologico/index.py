from mamifero import Mamifero
from ave import Ave
from repetil import Reptil

#nome = print('informe nome do cachorro')
#idade = int(print('informe idade do cachorro'))


meu_pet = Mamifero('Rex', 5, 'Ração', 0)

meu_pet.exibir_info()
meu_pet.amamentar()

minha_ave = Ave('Pirata', 2, 'Alpiste', 0.9)

minha_ave.exibir_info()
minha_ave.voar()

meu_reptil = Reptil('Mamba-negra', 4, 'carne', 'lisa')

meu_reptil.exibir_info()
meu_reptil.tomar_sol()