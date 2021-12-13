
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

params = [{
    'model': 'first 31.7',
    'loa': 9.61,
    'beam': 3.23,
    'draft': 1.85,
    'displacement': 3750,
    'sup': 52,
    'age': 2022 - 1999,
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
    'abattibile': True,
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
    'abattibile': True,
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
    'abattibile': True,
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
    'abattibile': True,
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
    'abattibile': True,
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
    'abattibile': True,
    'age': 2022 - 2002,
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
            'abattibile': True,
            'spi': True
        }

    #- (2022 - boat['boat']['year']) / 10.

    # Velocita' massima teorica in nodi
    vmaxtor = 1.35 * math.sqrt(params['loa'] * 3.28084)
    vmaxt = vmaxtor

    if not params['abattibile']:
        vmaxt = vmaxt - 0.5

    if params['spi']:
        vmaxt *= 0.68
    else:
        vmaxt *= 0.53

    # Potenza complessiva barca
    # Maggior valore => maggior velocita'
    # Bisogna includere anche il draft, dato che maggiore il pescaggio, maggiore la stabilita'
    dispt = (params['displacement']) 

    # Dal calcolo togliamo 1/10 peso * draft, dato che maggiore il pescaggio, maggiore la stabilita'
    sup = params['sup']
    pow = sup / (dispt) * params['loa']

    # Fattore di forma
    # Maggior fattore => maggior velocita'
    #ff =  1 / (params['beam'] / params['loa']) #* params['draft']

    vmax2 = vmaxt * pow #* ff
    vmax = vmaxt + vmax2

    
    # v = s/t
    # t = s/v

    # Tempo per fare un miglio in secondi (e' il GPH orc)
    tod = 1 / vmax * 60. * 60.
    tod += 0.9 * (params['age'])

    # Calcola il time on time
    tot = (1/ tod * 60 * 60) / 7.

    # print ('Model: ', params['model'], 'VMAXT: ', vmaxt, 'VMAX: ', vmax, 'VMAX2: ', vmax2, 'FF: ', ff, 'Power: ', pow, 'TOD: ', tod)
    print (params['model'], ',', "{:.2f}".format(vmaxtor), ',', "{:.2f}".format(vmaxt), ',', "{:.2f}".format(vmax), ',', "{:.2f}".format(vmax2), ',', "{:.2f}".format(ff), ',', "{:.2f}".format(pow), ',', "{:.2f}".format(tod), ',', "{:.4f}".format(tot))

    #print (params)
    #print ()

print('model, vmaxt, vmaxtcor, vmax, vmax2, ff, power, tod, tot')
for x in params:
    ratingOfBoat(params=x)


# data = utils.dataToList(utils.loadData())
# for y in ['first 31.7', 'comet 33', 'jod 35']:
#     for x in [utils.findBoatModel(data, y, n = 1)]:
#         ratingOfBoat(x)
