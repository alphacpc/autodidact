import time
import random

date_rec = time.strftime('%d/%m/%Y', time.gmtime(random.randint(1515452400,int(time.time()))))

print(date_rec)
