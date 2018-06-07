import io
import typing
import pdb
import json

from azure.functions import _abc as azf_abc
from azure.functions import _edgehub as azf_edgehub

from . import meta
from .. import protos

class EdgeHubMessage(azf_edgehub.EdgeHubMessage):
    """An EdgeHub Message."""    

    def __init__(self, *, 
                 message: None):
        print('in the worker/bindings init')
        super().__init__(id=id, message=message)

class EdgeHubConverter(meta.InConverter,
                    meta.OutConverter,
                    binding='edgeHub'): 

    @classmethod
    def check_input_type_annotation(cls, pytype: type) -> bool:
        print('got here to: check_input_type_annotation')
        return issubclass(pytype, azf_edgehub.EdgeHubMessage)

    @classmethod
    def from_proto(cls, data: protos.TypedData, *,
                   pytype: typing.Optional[type],
                   trigger_metadata) -> typing.Any:
        print('got here to: from_proto')
        
        data_type = data.WhichOneof('data')
        
        if data_type == 'string':
            message = data.string.encode('utf-8')
        elif data_type == 'bytes':
            message = data.bytes
        else:
            raise NotImplementedError(
                f'unsupported queue payload type: {data_type}')

        return EdgeHubMessage(
            message=json.loads(message)
        )

    @classmethod
    def check_output_type_annotation(cls, pytype: type) -> bool:
        print('got here to: check_output_type_annotation')
        return issubclass(pytype, (str, bytes))

    @classmethod
    def to_proto(cls, obj: typing.Any, *,
                 pytype: typing.Optional[type]) -> protos.TypedData:
        print('got here to: to_proto')
        if isinstance(obj, azf_edgehub.EdgeHubMessage):
            data = azf_edgehub.EdgeHubMessage(obj)
        elif isinstance (obj, azf_edgehub.EdgeHubMessage):
            data = obj
        else:
            raise NotImplementedError

        return protos.TypedData(
            json=json.dumps(data)
        )

class EdgeHubTriggerConverter(EdgeHubConverter,
                                binding='EdgeHubTrigger', trigger=True):
        print('fired EdgeHubTrigger')
    pass