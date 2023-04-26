#                     0       1         2        3         4
nevek:list[str] = ['Géza', 'Emőke', 'András', 'Petra', 'Zoltán']
magassagok:list[int] = []

for i in range(len(nevek)):
    m:int = int(input(f'{nevek[i]} magassága: '))
    magassagok.append(m)

m_osszeg:int = sum(magassagok)
m_atlag:float = m_osszeg / len(magassagok)

print(f'az emberek átlagmagassága: {round(m_atlag, 2)} cm')

# nevek.sort()
# print(f'nevek névsorban: {nevek}')

for i in range(0, len(nevek) - 1):
    for j in range(i, len(nevek)):
        if magassagok[i] > magassagok[j]:
            sm:int = magassagok[i]
            magassagok[i] = magassagok[j]
            magassagok[j] = sm
            sn:str = nevek[i]
            nevek[i] = nevek[j]
            nevek[j] = sn

for i in range(len(nevek)):
    print(f'{nevek[i]}: {magassagok[i]} cm')

max_index:int = 0
for i in range(len(magassagok)):
    if magassagok[i] > magassagok[max_index]:
        max_index = i

# print(f'A legmagasabb {nevek[max_index]}, ő {magassagok[max_index]} cm magas')

magas_indexek:list[int] = []
for i in range(len(magassagok)):
    if magassagok[i] == magassagok[max_index]:
        magas_indexek.append(i)

print(f'a legnagyobb magasság {magassagok[max_index]} cm')
print('ők mind ilyen magasak:')
for i in magas_indexek:
    print(f'\t-{nevek[i]}')

legnagyobb_elem:int = max(magassagok)
maxi:int = magassagok.index(legnagyobb_elem)
legnagyobb_ertekhez_tartozo_nev:str = nevek[maxi]

print(f'a legmagasabb: {nevek[magassagok.index(max(magassagok))]}')
print(f'ő {max(magassagok)} cm magas')