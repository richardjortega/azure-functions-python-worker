import datetime
import json
import typing

from . import _abc


class EdgeHubMessage(_abc.EdgeHubMessage):
    """A EdgeHub message object.

    :param bytes message:
        Bytes specifying the message body
    """

    def __init__(self, *,
                 message: typing.Optional[typing.Union[str, bytes]]=None) -> None:
        self.__message = b''

        print("in the functions/_edgehub")

        if message is not None:
            self.__set_message(message)

    def __set_message(self, body):
        if isinstance(message, str):
            message = message.encode('utf-8')

        if not isinstance(message, (bytes, bytearray)):
            raise TypeError(
                f'reponse is expected to be either of '
                f'str, bytes, or bytearray, got {type(message).__name__}')

        self.__message = bytes(message)

    def get_message(self) -> bytes:
        """Return message content as bytes."""
        return self.__message

    def get_json(self) -> typing.Any:
        """Decode and return message content as a JSON object.

        :return:
            Decoded JSON data.

        :raises ValueError:
            when the body of the message does not contain valid JSON data.
        """
        return json.loads(self.__message)