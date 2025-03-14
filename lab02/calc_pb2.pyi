from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MsgCliente(_message.Message):
    __slots__ = ("operacao", "n1", "n2")
    OPERACAO_FIELD_NUMBER: _ClassVar[int]
    N1_FIELD_NUMBER: _ClassVar[int]
    N2_FIELD_NUMBER: _ClassVar[int]
    operacao: int
    n1: float
    n2: float
    def __init__(self, operacao: _Optional[int] = ..., n1: _Optional[float] = ..., n2: _Optional[float] = ...) -> None: ...

class MsgServidor(_message.Message):
    __slots__ = ("mensagem", "resposta")
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    RESPOSTA_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    resposta: float
    def __init__(self, mensagem: _Optional[str] = ..., resposta: _Optional[float] = ...) -> None: ...
