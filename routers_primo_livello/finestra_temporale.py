from fastapi import APIRouter
from routers_secondo_livello import pioggia,temperatura,umidita

router = APIRouter(
  prefix='/{finestra_temporale}'
)

@router.get('/')
def print_text(finestra_temporale:str):
    data_inizio=finestra_temporale[0:11]
    data_fine=finestra_temporale[12:]
    return data_inizio,data_fine,"Puoi scegliere fra precipitazione, temperatura e umidità"
  
router.include_router(pioggia.router_2)
router.include_router(temperatura.router_2)
router.include_router(umidita.router_2)