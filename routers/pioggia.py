from fastapi import APIRouter


router = APIRouter(
  prefix='/PR',
  tags=['PR']
)

@router.get('/')
def print_text():
  return {"messagge":"pioggia"}
