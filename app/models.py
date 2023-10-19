from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
from datetime import date
from typing import Optional


class Pessoa(Model):
    id_pessoa = fields.IntField(pk=True, source_field="id_pessoa")
    nome = fields.CharField(100, source_field="nome")
    rg = fields.CharField(100, source_field="rg")
    cpf = fields.CharField(100, source_field="cpf")
    data_nascimento = fields.DateField(source_field="data_nascimento")
    data_admissao = fields.DateField(source_field="data_admissao")
    funcao = fields.CharField(100, null=True, source_field="funcao")

    class Meta:
        table = "pessoas"



class PessoaIn(BaseModel):
    nome: str
    rg: str
    cpf: str
    data_nascimento: date
    data_admissao: date
    funcao: Optional[str]


class PessoaOut(BaseModel):
    id_pessoa: int
    nome: str
    rg: str
    cpf: str
    data_nascimento: date
    data_admissao: date
    funcao: Optional[str]
