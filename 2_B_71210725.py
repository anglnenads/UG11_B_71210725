def check_data_type(D1, D2):
    if (type(D1).__name__.lower()==D2.lower()):
        print("Jawaban Anda benar")
        return True
   
    print("Jawaban Anda salah, seharusnya adalah : ", type(D1).__name__.lower())
    return False

print(check_data_type("Kevin","STr")) 
print(check_data_type("Kevin","str")) 
print(check_data_type(12345,"str")) 
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))  