from fastapi import APIRouter

router_2 = APIRouter(
  prefix='/P',
  tags=['P']
)

@router_2.get('/')
def print_text():
    return "Ecco il dato"