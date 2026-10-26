atzimes = [8, 4, 7, 10, 6, 9, 5]

skaits = len(atzimes)
vidējais = sum(atzimes) / skaits
lielākais = max(atzimes)
septiņi_vai_lielāki = sum(1 for a in atzimes if a >= 7)

print(f"Skaits: {skaits}, Vidējais: {vidējais}, Lielākais: {lielākais}, >=7: {septiņi_vai_lielāki}")
