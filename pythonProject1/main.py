# ["a b c", "z b", "x y", "z" ] sort by num of words

letras: list[str] = ["a b c", "z b", "x y", "z" ]
print(sorted(letras))

print(sorted(letras, key=lambda l: len(l.split())))

# [89, 91, 23, 34, 15, 98, 71, 99, 101]
# sort by units and order by the smaller  unit number
# 71, 91, 101, 23, 34, 15, 98, 89, 99

numeros: list[int] = [89, 91, 23, 34, 15, 98, 71, 99, 101]
print(numeros)

print(sorted(numeros, key=lambda n: (n % 10, n)))

#(n % 10, n) it orders first by units then checks the tens to provide order chronologic

#sort even first then odd

print(sorted([89, 91, 23, 34, 15, 98, 71, 99, 101], key=lambda n: (n % 2, n)))