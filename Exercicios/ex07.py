# Estudando código! Tópico Datetime/time

import datetime
# Datetime = pacote
print(datetime.datetime.now().strftime('Data: %d/%m/%Y Horário: %H:%M'))
# %d : day
# %m : month
# %Y : year
# %H : hour
# %M : minutes


import time
print(time.strftime("%d/%m/%Y %H:%M"))