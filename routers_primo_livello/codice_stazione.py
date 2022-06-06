from fastapi import APIRouter
from routers_secondo_livello import finestra_temporale

router = APIRouter(
  prefix='/{codice_stazione}'
)

@router.get('/')
def print_text(codice_stazione):
    return "La stazione prescelta è {codice_stazione}. Scegliere la finestra temporale di interesse."
  
router.include_router(finestra_temporale.router_2)
