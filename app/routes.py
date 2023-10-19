from fastapi import APIRouter, HTTPException, Depends
from .models import Pessoa, PessoaIn, PessoaOut

router = APIRouter()


@router.post("/pessoas/", response_model=PessoaOut)
async def create_pessoa(pessoa: PessoaIn):
    return await Pessoa.create(**pessoa.dict())


@router.get("/pessoas/", response_model=list[PessoaOut])
async def get_pessoas():
    return await Pessoa.all()


@router.put("/pessoas/{id_pessoa}", response_model=PessoaOut)
async def update_pessoa(id_pessoa: int, pessoa: PessoaIn):
    await Pessoa.filter(id_pessoa=id_pessoa).update(**pessoa.dict(by_alias=True))
    return await Pessoa.get(id_pessoa=id_pessoa)


@router.delete("/pessoas/{id_pessoa}", response_model=PessoaOut)
async def delete_pessoa(id_pessoa: int):
    deleted_count = await Pessoa.filter(id_pessoa=id_pessoa).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Pessoa {id_pessoa} not found")
