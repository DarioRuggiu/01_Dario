from fastapi import APIRouter


router = APIRouter(
  prefix='/TP',
  tags=['TP']
)

@router.get('/')
def print_text():
  return {"messagge":"temperatura"}