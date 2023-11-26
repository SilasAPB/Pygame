ITEMS = {
    "PISTOL":{
        "asset" : "../assets/img/pistola.png",  # Imagem do sprite da arma
        "itemType" : "STRAIGHT",  # Tipo do projétil
        "velocity" : 25,  # Velocidade do projétil
        "spray" : .2,  # % da variação de ângulo de tiro
        "size" : 8,  # Quantidade de projéteis antes de cooldown
        "cadence" : 5,  # Quantidade de Frames entre os usos do item
        "recoil" : 4,  # Velocidade do recuo da arma
        'reload': 3,  # Cooldown entre a velocidade de recarga da arma
        "soundEffect" : "Som1.wav"
        #"useParticle" : "" 
        #"hitParticle" : ""
    },
    "OUTRA_ARMA":{
        "asset" : "../assets/img/pistola.png",  # Imagem do sprite da arma
        "itemType" : "STRAIGHT",  # Tipo do projétil
        "velocity" : 30,  # Velocidade do projétil
        "spray" : .1,  # % da variação de ângulo de tiro
        "size" : 8,  # Quantidade de projéteis antes de cooldown
        "cadence" : 10,  # Quantidade de Frames entre os usos do item
        'reload': 30,  # Cooldown entre a velocidade de recarga da arma
        "recoil" : 4,  # Velocidade do recuo da arma
        "soundEffect" : "",
        "useParticle" : "",
        "hitParticle" : ""
    }
}