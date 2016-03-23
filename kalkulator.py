def dodawanie (a, b):
	return a+b
def get_info():
	return "To jest kalk Wiki"

try:	
	a = int(input("podaj pierwsza liczbe"))
	b = int(input("podaj druga liczbe"))
print(dodawanie(a, b))
except ValueError as ve:
	print("wprowadzono bledne dane, koncze dzialanie")
input()
	


