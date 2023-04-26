import hashlib

def passwd_check(passwd):
    SpecialSym=["!", "@", "#","$", "%", "^", "&","*"]
    return_val=True
 
    if len(passwd) <  8:
        print("Votre mot de passe doit contenir au moins 8 caractères")
        return_val=False
    if not any(char.isdigit() for char in passwd):
        print("Votre mot de passe doit contenir au moins un chiffre")
        return_val=False
    if not any(char.isupper() for char in passwd):
        print("Votre mot  passe doit contenir au moins une lettre majuscule")
        return_val=False
    if not any(char.islower() for char in passwd):
        print("Votre mot de passe doit contenir au moins une lettre minuscule")
        return_val=False
    if not any(char in SpecialSym for char in passwd):
        print("Votre mot de passe doit contenir un caractère spécial(!, @, #, $, %, ^, &, *)")
        return_val=False
    if return_val:
        print("le password est : " + passwd)
        
        password_bytes = passwd.encode('utf-8')
        hash_obj = hashlib.sha256(password_bytes)
        return("hachage hexadecimal : " +  hash_obj.hexdigest())
        
    return return_val
    

passwd = input('entrez votre mot de passe : ')
print(passwd_check(passwd))



























"""""
def passe_word():
    
        passe_word = input("Veuillez entrer votre mot de passe:")

        if len(passe_word) < 8:
            print("Votre mot de passe doit contenir au moins 8 caractères")
    
        elif  passe_word.islower():
            # print("Votre mot  passe doit contenir au moins une lettre minuscule")
            if not passe_word.isupper():
                print("Votre mot de passe doit contenir au moins une lettre majuscule")
        
            elif not passe_word .isdigit():
                print("Votre motde passe doit contenir au moins un chiffre")
        
            elif not passe_word in ("!", "@", "#","$", "%", "^", "&","*"):
                print("Votre mot de passe doit contenir un caractère spécial(!, @, #, $, %, ^, &, *)")
        else:
            print("votre mot de passe est valable")
            break
            
    
        
passe_word()



with open('data.json') as mon_fichier:
    data = json.load()

print(data)












# """
# ######
# def demander_passe_word():
#     passe_word_valide = False
    
#     while not passe_word_valide:
#         passe_word = input("Veuillez entrer votre mot de passe:")

#         if len(passe_word) < 8:
#             print("Votre mot de passe doit contenir au moins 8 caractères")
            
#         for char in passe_word:
#             if char.islower():
#                 char = True
        
#             if char .isupper():
#                 char = True
        
#             if char. isdigit():
#                  = True
        
#             if char in ["!", "@", "#","$", "%", "^", "&","*"]:
#                 caractère_special = True
        
#         if not miniscule:
#             print(" Votre mot de passe doit contenir au moins une lettre miniscule")
            
#         if not majuscule:
#             print("Votre mot de passe doit contenir au moins une lettre majuscule")
            
#         if not chiffre:
#             print("Votre mot de passe doit contenir au moins un chiffre")
            
#         if not caractère_special:
#             print("Votre mot de passe doit au moins contenir un caractère spécial (!, @, #, $, %, ^, &, *)")
            
#             passe_word_valide = len(passe_word) >= 8 and majuscule and miniscule and chiffre and caractère_special
        
#         if passe_word_valid:
#             print("Votre mot de passe est valide")
#             return passe_word
#         else: 
#             print("Votre mot de passe n'est pas valide, veuillez en choisir un autre")

# if __name__ == " main__ ":
#     demander_passe_word()
#    ##########     """

 
