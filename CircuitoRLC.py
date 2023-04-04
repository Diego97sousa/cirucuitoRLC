#!/usr/bin/env python
# coding: utf-8

# In[4]:


freq = float (input('Digite o valor da frequencia de sinal em Hz: \n'))

resi = float (input('Digite a resistência do resistor: \n'))

capa = float (input('Digite a capacitancia do Capacitor em farads: \n'))

bobi = float (input('Digite a indutancia da Bobina em henrys: \n'))

corr =  tens / resi


xc = 1/ (6.28 * freq * capa)

xl = 6.28 * freq * bobi

# Para saber a tesão.
tens_efetiva = capa - bobi

# Caculo da impedancia
impe = (resi ** 2 + tens_efetiva ** 2) ** (1/2)

print('---------------------------------------------------------------------')
print('RELATÓRIO DE CIRCUITO')

print('Frquência: ', freq,'Hz')

print('A resistência do resistor é: ' ,resi,'ohms')

print('A reatância do capacitor é:' ,round(xc,2) ,'ohms')

print('A reatância da Bobina é: ',round(xl,2) ,'ohms')

print('O valor da impendancia é: ', round(impe,2),'ohms')

print('---------------------------------------------------------------------')


# In[ ]:




