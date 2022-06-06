from fastapi import APIRouter

router_3 = APIRouter(
  prefix='/UM',
  tags=['UM']
)

@router_3.get('/')
def print_text():
    return "Ecco il dato della stazione %s per il periodo %s-%s"%(settings.id_stazione,settings.data_ini,settings.data_fin)
