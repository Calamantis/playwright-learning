def calculate_brutto(netto, vat_rate=0.23):
    if not isinstance(netto, (int, float)): # isinstance checks if the given attrbute belongs to the expected type
        raise TypeError(f"Cena netto musi być liczbą, a otrzymano: {type(netto).__name__}")
    if netto < 0:
        raise ValueError("Cena netto nie może być ujemna")
    return round(netto * (1 + vat_rate), 2)

# def calculate_brutto(netto, vat_rate=0.23):
#     try:
#         if netto < 0:
#             raise ValueError("Cena netto nie może być ujemna")
#         return round(netto * (1 + vat_rate), 2)
#     except TypeError:
#         raise TypeError("Błędny typ danych! Podaj liczbę.")