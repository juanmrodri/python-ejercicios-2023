import re

texto = "The Spartans faced the Persian Empire in the Battle of Thermopylae in 480 BCE.\nA small Spartan-led Greek force defended a narrow mountain pass against a much larger Persian army.\nThey fought bravely but were ultimately defeated.\nThis battle is famous for its Spartan valor and sacrifice."

print(texto)

text2 = "777777789hola a caca hoca 1 culo hoja 7 sorete hoka hoia 8 hoya hora howa hoa"

print("ho.*a")
print(re.split("ho.*a",text2))

print("\nho.?a") # este
print(re.split("ho.?a",text2))

print("\nho.+a")
print(re.findall("ho.+a",text2))

print("\n[0-9]+") # este
print(re.findall("[0-9]+",text2))