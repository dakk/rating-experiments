
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
# - elica fissa / abattibile
# - age
# - peso
# - lunghezza
# - larghezza
# - sup velica
# - pescaggio

# La velocita' massima teorica di un corpo immerso in assetto dislocante e' 1.35 * sqrt(L)

    
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
            'abattibile': True,
            'spi': True
        }

    #- (2022 - boat['boat']['year']) / 10.

    # Velocita' massima teorica in nodi
    vmaxt = 1.35 * math.sqrt(params['loa'] * 3.28084)

    # Da VMAX togliamo 0.8 nodi se a pala fissa
    vmax = vmaxt

    # Potenza complessiva barca
    # Maggior valore => maggior velocita'
    # Bisogna includere anche il draft, dato che maggiore il pescaggio, maggiore la stabilita'
    dispt = (params['displacement'] / 1000.) 

    # Dal calcolo togliamo 1/10 peso * draft, dato che maggiore il pescaggio, maggiore la stabilita'
    # dispt -= dispt / 10. * params['draft']
    # dispt -= dispt * 1. / params['draft']

    sup = params['sup']

    pow = sup / dispt

    # Fattore di forma
    # Maggior fattore => maggior velocita'
    ff =  params['beam'] / params['loa']
    #* params['draft']

    sfact = 0
    # sfact = - 1 / (pow) * ff
    # print(pow, pow, ff, sfact)
    # sfact = pow / 100. * ff
    #print(pow, vmax * (pow / 100.) / params['draft'])
    vmax2 = vmax * (pow / 100.) / params['draft'] 
    # vmax += vmax * ff 

    #print(ff)
    vmax = vmax + vmax2
    
    if not params['abattibile']:
        vmax = vmax - 0.5

    if params['spi']:
        vmax *= 0.85
    else:
        vmax *= 0.7
    # v = s/t
    # t = s/v

    # Tempo per fare un miglio in secondi (e' il GPH orc)
    tod = 1 / vmax * 60. * 60.

    print ('Model: ', params['model'], 'VMAXT: ', vmaxt, 'VMAX: ', vmax, 'VMAX2: ', vmax2, 'FF: ', ff, 'Power: ', pow, 'TOD: ', tod)
    #print (params)
    #print ()


params = [{
    'model': 'first 31.7',
    'loa': 9.61,
    'beam': 3.23,
    'draft': 1.85,
    'displacement': 3750,
    'sup': 53,
    'age': 0,
    'abattibile': True,
    'rating': 0,
    'spi': False
}, {
    'model': 'comet 333',
    'loa': 10.3,
    'beam': 3.35,
    'draft': 1.95,
    'displacement': 5100,
    'sup': 52,
    'abattibile': True,
    'age': 0,
    'rating': 0,
    'spi': False
}, {
    'model': 'jod35',
    'loa': 10.60,
    'beam': 3.5,
    'draft': 1.95,
    'displacement': 3500,
    'sup': 66,
    'abattibile': True,
    'age': 0,
    'rating': 0,
    'spi': False
}, {
    'model': 'x99',
    'loa': 9.8,
    'beam': 3,
    'draft': 1.79,
    'displacement': 3200,
    'sup': 52.2,
    'abattibile': True,
    'age': 0,
    'rating': 0,
    'spi': False
}, {
    'model': 'comet33 (2004)',
    'loa': 9.96,
    'beam': 3.29,
    'draft': 1.95,
    'displacement': 4700,
    'sup': 56.9,
    'abattibile': True,
    'age': 0,
    'rating': 0,
    'spi': False
}, {
    'model': 'comet 1050',
    'loa': 10.10,
    'beam': 3.278,
    'draft': 1.80,
    'displacement': 5003,
    'sup': 58.87,
    'abattibile': True,
    'age': 0,
    'rating': 0,
    'spi': False
}, {
    'model': 'sunfast3200',
    'loa': 9.7,
    'beam': 3.4,
    'draft': 1.95,
    'displacement': 3600,
    'sup': 59,
    'abattibile': True,
    'age': 0,
    'rating': 0,
    'spi': False
}]

for x in params:
    ratingOfBoat(params=x)


# data = utils.dataToList(utils.loadData())
# for y in ['first 31.7', 'comet 33', 'jod 35']:
#     for x in [utils.findBoatModel(data, y, n = 1)]:
#         ratingOfBoat(x)
