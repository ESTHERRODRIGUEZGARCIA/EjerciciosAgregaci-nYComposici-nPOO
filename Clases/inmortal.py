class Yin: pass 
class Yang: 
    def __del__(self): # atributo privado
        print("Yang destruido") 
 
yin = Yin()
yang = Yang()
yin.yang = yang #eliminar

print(yang) 
del(yin.yang)
del(yang) 

print("?")

#nos devuelve Yang destruido ?
# salta "yang" pues no se le hace referencia
