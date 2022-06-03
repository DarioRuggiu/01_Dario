from fastapi import APIRouter

router_2 = APIRouter(
  prefix='/TP',
  tags=['TP']
)

@router_2.get('/')
def print_text(data_inizio,data_fine):
    return "Benvenuto nella temperatura dal %s al %s"(data_inizio,data_fine)