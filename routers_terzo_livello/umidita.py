from fastapi import APIRouter, Request

router_3 = APIRouter(
  prefix='/UM',
  tags=['UM']
)

@router_3.get('/')
def print_text(request: Request):
    print(request.path_params)
    return "Ecco il dato della stazione %s per il periodo %s-%s"
