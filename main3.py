
import utils
import random
import math

# TOD: time on distance: tempo impiegato per un miglio
# TOT: corrispettivo corretto del tempo sul tempo
# TCOM = TOT * T
# All of this data is presented on the rating certificate, and the General Performance 
# Handicap [GPH] rating is expressed as a time, in seconds, that the yacht will take to complete a 
# mile across a defined range of wind speeds and across a defined range of angles to true wind.


# Parametri:
# - elica fissa / foldable
# - age
# - peso
# - lunghezza
# - larghezza
# - sup velica
# - pescaggio

# La velocita' massima teorica di un corpo immerso in assetto dislocante e' 1.35 * sqrt(L)

params = [{
    'model': 'first 31.7',
    'loa': 9.61,
    'beam': 3.23,
    'draft': 1.85,
    'displacement': 3750,
    'sup': 52,
    'age': 2022 - 2004,
    'foldable': True,
    'rating': 0,
    'spi': False
}, {
    'model': 'comet 12',
    'loa': 12,
    'beam': 3.90,
    'draft': 2.05,
    'displacement': 7500,
    'sup': 96,
    'foldable': True,
    'age': 2022 - 1985,
    'rating': 0,
    'spi': False
    
    },{
    'model': 'attalia 32',
    'loa': 9.70,
    'beam': 3.20,
    'draft': 1.75,
    'displacement': 3400,
    'sup': 51.6,
    'foldable': True,
    'age': 2022 - 1988,
    'rating': 0,
    'spi': False
    
    },{
    'model': 'comet 333',
    'loa': 10.3,
    'beam': 3.35,
    'draft': 1.95,
    'displacement': 5100,
    'sup': 52,
    'foldable': True,
    'age': 2022 - 1987,
    'rating': 0,
    'spi': False
}, {
    'model': 'jod35',
    'loa': 10.60,
    'beam': 3.5,
    'draft': 1.95,
    'displacement': 3500,
    'sup': 66,
    'foldable': True,
    'age': 2022 - 1993,
    'rating': 0,
    'spi': False
}, {
    'model': 'x99',
    'loa': 9.96,
    'beam': 3,
    'draft': 1.79,
    'displacement': 3200,
    'sup': 63,
    'foldable': True,
    'age': 2022 - 1995,
    'rating': 0,
    'spi': True
}, {
    'model': 'comet33 (2004)',
    'loa': 9.96,
    'beam': 3.29,
    'draft': 1.95,
    'displacement': 4700,
    'sup': 56.9,
    'foldable': True,
    'age': 2022 - 2004,
    'rating': 0,
    'spi': True
}, {
    'model': 'comet 1050',
    'loa': 10.10,
    'beam': 3.278,
    'draft': 1.80,
    'displacement': 5003,
    'sup': 58.87,
    'foldable': True,
    'age': 2022 - 1983,
    'rating': 0,
    'spi': True
}, {
    'model': 'sunfast3200',
    'loa': 10.1,
    'beam': 3.4,
    'draft': 1.95,
    'displacement': 3600,
    'sup': 59,
    'foldable': True,
    'age': 2022 - 2007,
    'rating': 0,
    'spi': True
}, {
    'model': 'first 40.7',
    'loa': 11.93,
    'beam': 3.75,
    'draft': 2.40,
    'displacement': 7100,
    'sup': 85,
    'foldable': True,
    'age': 2022 - 2002,
    'rating': 0,
    'spi': True
}, {
    'model': 'polaris 33',
    'loa': 10.13,
    'beam': 3.38,
    'draft': 1.82,
    'displacement': 4300,
    'sup': 63.44,
    'foldable': True,
    'age': 2022 - 1979,
    'rating': 0,
    'spi': True
}]

    
def ratingOfBoat(boat = None, params = None):
    if boat != None and params == None:
        params = {        
            'model': boat['boat']['type'],
            'loa': boat['boat']['sizes']['loa'],
            'beam': boat['boat']['sizes']['beam'],
            'draft': boat['boat']['sizes']['draft'],
            'displacement': boat['boat']['sizes']['displacement'],
            'sup': boat['boat']['sizes']['genoa'] + boat['boat']['sizes']['main'],
            'age': 2022 - boat['boat']['year'],
            'rating': boat['rating'],
            'foldable': True,
            'spi': True
        }


    # Velocita' massima teorica in nodi
    vmaxt = 1.35 * math.sqrt(params['loa'] * 3.28084)

    # Abbuoniamo 0.5 di velocita' nel caso di elica fissa
    if not params['foldable']:
        vmaxt = vmaxt - 0.5

    # Moltiplichiamo per un coefficiente di correzione che ci permette di stare in linea
    # coi valori ORC: a seconda che si usi o meno vele asimettriche, si usa un coefficiente
    # diverso.
    if params['spi']:
        vmaxt *= 0.68
    else:
        vmaxt *= 0.53

    # Potenza complessiva barca
    pow = params['sup'] / (params['displacement']) * params['loa']

    # Calcoliamo la vmax in relazione alla potenza
    vmax = vmaxt + vmaxt * pow 

    # Tempo per fare un miglio in secondi (e' il GPH orc)
    tod = 1 / vmax * 60. * 60.

    # Abbuoniamo 0.9 secondi per miglio per anno di eta
    tod += 0.9 * (params['age'])

    # Calcola il time on time partendo dal tod
    tot = (1 / tod * 60 * 60) / 7.

    print (params['model'], ',', "{:.2f}".format(vmaxt), ',', "{:.2f}".format(vmax), ',', "{:.2f}".format(pow), ',', "{:.2f}".format(tod), ',', "{:.4f}".format(tot))


print('model, vmaxt, vmax, power, tod, tot')
for x in params:
    ratingOfBoat(params=x)


# data = utils.dataToList(utils.loadData())
# for y in ['first 31.7', 'comet 33', 'jod 35', 'farr 40', 'sunfast 3200', 'comet 333', 'comet 1050', 'x99', 'first 40.7']:
#     for x in utils.findBoatModel(data, y, n=6):
#         ratingOfBoat(boat=x)
