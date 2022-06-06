from fastapi import APIRouter
from routers_terzo_livello import pioggia,temperatura,umidita
from datetime import datetime

router_2 = APIRouter(
  prefix='/{finestra_temporale}'
)

@router_2.get('/')
def print_text(finestra_temporale:str):
    data_ini = datetime.strptime(finestra_temporale[:11],'%Y%M%d%h%M')
    data_fin = datetime.strptime(finestra_temporale[12:],'%Y%M%d%h%M')
    return "Verranno selezionati i dati a partire da {data_ini} fino a {data_fin}. Scegliere la tipologia di dato meteo associato alla stazione."

router_2.include_router(pioggia.router_3)
router_2.include_router(temperatura.router_3)
router_2.include_router(umidita.router_3)