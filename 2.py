dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]


def contar_especies(pila_dinos):
    especies = [] 
    for dinosaurio in pila_dinos:
        especies.append(dinosaurio["especie"])
    especies_unicas = set(especies)  
    return len(especies_unicas)

dinos_pila = list(dinosaurios) 

def contar_descubridores_diferentes(pila_dinosaurios):
    descubridores = [] 
    for dinosaurio in pila_dinosaurios:
        descubridores.append(dinosaurio["descubridor"]) 
    descubridores_unicos = set(descubridores)
    return len(descubridores) 

dinos_pila = list(dinosaurios)  

def dinosaurios_T(pila_dinosaurios):
    dinos_T = []
    for dinosaurio in pila_dinosaurios:
        if dinosaurio["nombre"].startswith("T"):
            dinos_T.append(dinosaurio["nombre"])
    return dinos_T

dinos_pila = list(dinosaurios)

def dinos_menos_275(pila_dinosaurios):
    dinosaurios_menos_275 = []
    for dinosaurio in pila_dinosaurios:
        peso = int(dinosaurio["peso"].split()[0])
        if peso < 275:
            dinosaurios_menos_275.append((dinosaurio["nombre"], dinosaurio["peso"]))
    return dinosaurios_menos_275

def dinos_AQS(pila_dinosaurios, letras):
    return [dinosaurio for dinosaurio in pila_dinosaurios 
            if dinosaurio["nombre"].startswith(tuple(letras))]

dinosaurios_pila = list(dinosaurios)  

letras = {'A', 'Q', 'S'}

dinosaurios_seleccionados = dinos_AQS(dinosaurios_pila, letras)
dinosaurios_menos_275 = dinos_menos_275(dinos_pila)
dinos_T_mostrar = dinosaurios_T(dinos_pila)
descubridores_total = contar_descubridores_diferentes(dinos_pila)
especies_total = contar_especies(dinos_pila)
print("Cantidad de especies:", especies_total)
print("Cantidad de descubridores distintos:", descubridores_total)
print("Dinosaurios los cuales sus nombres empiezan con T:", dinos_T_mostrar)
print("Los dinosaurios que pesan menos de 275 kg son:", dinosaurios_menos_275)
for dinosaurio in dinosaurios_seleccionados:
    print(dinosaurio)
