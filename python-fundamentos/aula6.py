# convesão de tipos, coercao = type convertion, typecasting, coercion
# é o ato de converter um tipo e outro

# tipos imutáveis e primitivos: str, int, float, bool

# print('1' + 1) => isso da erro, pois devido a tipagem forte o python nao consegue concatenar str + int
print('1' + '1')

print(int("1"), type(int("1")), end="\n\n")

print(1 + int("1"))
print(1 + float("1"))
print(type(1 + int("1")))
print(bool(""))
print(bool(" "))
print(str(11) + 'b')

#print(int("a") + 1) => isso da erro! nao da para suportar passar o tipo str 'a' para int