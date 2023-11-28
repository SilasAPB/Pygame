from lista_assests import *

ITEMS = {
    "PISTOL":{
        "asset" : "Armas1",  # Imagem do sprite da arma
        "itemType" : "OBLIQUE",  # Tipo do projétil
        "velocity" : 25,  # Velocidade do projétil
        "spray" : .2,  # % da variação de ângulo de tiro
        "size" : 8,  # Quantidade de projéteis antes de cooldown
        "cadence" : 5,  # Quantidade de Frames entre os usos do item
        "recoil" : 4,  # Velocidade do recuo da arma
        'reload': 3,  # Cooldown entre a velocidade de recarga da arma
        "soundEffect" : "Som2.wav",
        "damage": 5,
        #"useParticle" : "" 
        #"hitParticle" : ""
    },
    "Arma 2":{
        "asset" : 'Armas2',  # Imagem do sprite da arma
        "itemType" : "STRAIGHT",  # Tipo do projétil
        "velocity" : 30,  # Velocidade do projétil
        "spray" : .1,  # % da variação de ângulo de tiro
        "size" : 8,  # Quantidade de projéteis antes de cooldown
        "cadence" : 10,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 4,  # Velocidade do recuo da arma
        "soundEffect" : "Som1.wav",
        "damage": 5,
        "useParticle" : "",
        "hitParticle" : ""
    },
       "Arma 3":{
        "asset" : 'Armas3',  # Imagem do sprite da arma
        "itemType" : "BOUNCE",  # Tipo do projétil
        "velocity" : 15,  # Velocidade do projétil
        "spray" : .3,  # % da variação de ângulo de tiro
        "size" : 8,  # Quantidade de projéteis antes de cooldown
        "cadence" : 15,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 4,  # Velocidade do recuo da arma
        "soundEffect" : "Som1.wav",
        "damage": 9,
        "useParticle" : "",
        "hitParticle" : ""
    },
     "Arma 4":{
        "asset" : 'Armas4',  # Imagem do sprite da arma
        "itemType" : "STRAIGHT",  # Tipo do projétil
        "velocity" : 20,  # Velocidade do projétil
        "spray" : .9,  # % da variação de ângulo de tiro
        "size" : 20,  # Quantidade de projéteis antes de cooldown
        "cadence" : 18,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 8.5,  # Velocidade do recuo da arma
        "soundEffect" : "Som1.wav",
        "damage": 10,
        "useParticle" : "",
        "hitParticle" : ""
    }, 
    "Arma 5":{
        "asset" : 'Armas5',  # Imagem do sprite da arma
        "itemType" : "OBLIQUE",  # Tipo do projétil
        "velocity" : 10,  # Velocidade do projétil
        "spray" : .9,  # % da variação de ângulo de tiro
        "size" : 15,  # Quantidade de projéteis antes de cooldown
        "cadence" : 15,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 10,  # Velocidade do recuo da arma
        "soundEffect" : "Som2.wav",
        "damage": 9,
        "useParticle" : "",
        "hitParticle" : ""
    },
     "Arma 6":{
        "asset" : "Armas6",  # Imagem do sprite da arma
        "itemType" : "BOUNCE",  # Tipo do projétil
        "velocity" : 35,  # Velocidade do projétil
        "spray" : .8,  # % da variação de ângulo de tiro
        "size" : 15,  # Quantidade de projéteis antes de cooldown
        "cadence" : 5,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 10,  # Velocidade do recuo da arma
        "soundEffect" : "Som3.wav",
        "damage": 5,
        "useParticle" : "",
        "hitParticle" : ""
    },
     "Arma 7":{
        "asset" : "Armas7",  # Imagem do sprite da arma
        "itemType" : "STRAIGHT",  # Tipo do projétil
        "velocity" : 25,  # Velocidade do projétil
        "spray" : .6,  # % da variação de ângulo de tiro
        "size" : 20,  # Quantidade de projéteis antes de cooldown
        "cadence" : 9,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 4,  # Velocidade do recuo da arma
        "soundEffect" : "Som1.wav",
        "damage": 3.2,
        "useParticle" : "",
        "hitParticle" : ""
    },
     "Arma 8":{
        "asset" : "Armas8",  # Imagem do sprite da arma
        "itemType" : "BOUNCE",  # Tipo do projétil
        "velocity" : 40,  # Velocidade do projétil
        "spray" : .8,  # % da variação de ângulo de tiro
        "size" : 20,  # Quantidade de projéteis antes de cooldown
        "cadence" : 9,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 2,  # Velocidade do recuo da arma
        "soundEffect" : "Som3.wav",
        "damage": 7.2,
        "useParticle" : "",
        "hitParticle" : ""
    },
     "Arma 9":{
        "asset" : "Armas9",  # Imagem do sprite da arma
        "itemType" : "OBLIQUE",  # Tipo do projétil
        "velocity" : 40,  # Velocidade do projétil
        "spray" : .0,  # % da variação de ângulo de tiro
        "size" : 30,  # Quantidade de projéteis antes de cooldown
        "cadence" : 25,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 20,  # Velocidade do recuo da arma
        "soundEffect" : "Som2.wav",
        "damage": 7.2,
        "useParticle" : "",
        "hitParticle" : ""
    },

}