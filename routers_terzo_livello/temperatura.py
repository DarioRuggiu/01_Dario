from fastapi import APIRouter

router_3 = APIRouter(
  prefix='/TP',
  tags=['TP']
)

@router_3.get('/')
def print_text():
    return "Ecco il dato!"