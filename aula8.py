velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_radar1 = velocidade > RADAR_1
carro_multado_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and\
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_radar1 :
    print('Velocidade carro passou do radar 1 ')

if carro_multado_radar1 and velocidade_carro_radar1 :
    print('carro multado')