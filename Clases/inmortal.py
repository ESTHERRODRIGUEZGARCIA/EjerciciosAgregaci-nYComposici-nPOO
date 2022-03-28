class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang #eliminar
 
print(yang) 
del(yin.yang)
del(yang) 

print("?") 