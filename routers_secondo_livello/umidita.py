from fastapi import APIRouter

router_2 = APIRouter(
  prefix='/UM',
  tags=['UM']
)

@router_2.get('/')
def print_text(data_inizio,data_fine):
    return "Benvenuto nell'umidità dal %s al %s"(data_inizio,data_fine)

