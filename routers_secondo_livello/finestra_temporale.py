from fastapi import APIRouter
from routers_terzo_livello import pioggia,temperatura,umidita
from datetime import datetime

router_2 = APIRouter(
  prefix='/{finestra_temporale}'
)

@router_2.get('/')
def print_text(finestra_temporale:str):
    data_ini = datetime.strptime(finestra_temporale[:12],'%Y%m%d%H%M')
    data_fin = datetime.strptime(finestra_temporale[12:],'%Y%m%d%H%M')
    return "Verranno selezionati i dati a partire dal %s fino al %s. Scegliere la tipologia di dato meteo associato alla stazione."%(data_ini,data_fin)

router_2.include_router(pioggia.router_3)
router_2.include_router(temperatura.router_3)
router_2.include_router(umidita.router_3)