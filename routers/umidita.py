from fastapi import APIRouter


router = APIRouter(
  prefix='/UM',
  tags=['UM']
)

@router.get('/')
def print_text():
  return {"messagge":"umidità"}