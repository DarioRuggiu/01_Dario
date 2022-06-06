from fastapi import APIRouter

router_3 = APIRouter(
  prefix='/P',
  tags=['P']
)

@router_3.get('/')
def print_text():
    return "Ecco il dato della stazione"