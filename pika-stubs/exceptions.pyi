from typing import Sequence

from .adapters import blocking_connection


class AMQPError(Exception):
    ...


class AMQPConnectionError(AMQPError):
    ...


class ConnectionOpenAborted(AMQPConnectionError):
    ...


class StreamLostError(AMQPConnectionError):
    ...


class IncompatibleProtocolError(AMQPConnectionError):
    ...


class AuthenticationError(AMQPConnectionError):
    ...


class ProbableAuthenticationError(AMQPConnectionError):
    ...


class ProbableAccessDeniedError(AMQPConnectionError):
    ...


class NoFreeChannels(AMQPConnectionError):
    ...


class ConnectionWrongStateError(AMQPConnectionError):
    ...


class ConnectionClosed(AMQPConnectionError):

    def __init__(self, reply_code: int, reply_text: str) -> None: ...

    @property
    def reply_code(self) -> int: ...

    @property
    def reply_text(self) -> str: ...


class ConnectionClosedByBroker(ConnectionClosed):
    ...


class ConnectionClosedByClient(ConnectionClosed):
    ...


class ConnectionBlockedTimeout(AMQPConnectionError):
    ...


class AMQPHeartbeatTimeout(AMQPConnectionError):
    ...


class AMQPChannelError(AMQPError):
    ...


class ChannelWrongStateError(AMQPChannelError):
    ...


class ChannelClosed(AMQPChannelError):

    def __init__(self, reply_code: int, reply_text: str) -> None: ...

    @property
    def reply_code(self) -> int: ...

    @property
    def reply_text(self) -> str: ...


class ChannelClosedByBroker(ChannelClosed):
    ...


class ChannelClosedByClient(ChannelClosed):
    ...


class DuplicateConsumerTag(AMQPChannelError):
    ...


class ConsumerCancelled(AMQPChannelError):
    ...


class UnroutableError(AMQPChannelError):

    messages: Sequence[blocking_connection.ReturnedMessage]

    def __init__(
        self,
        messages: Sequence[blocking_connection.ReturnedMessage],
    ) -> None: ...


class NackError(AMQPChannelError):

    messages: Sequence[blocking_connection.ReturnedMessage]

    def __init__(
        self,
        messages: Sequence[blocking_connection.ReturnedMessage],
    ) -> None: ...


class InvalidChannelNumber(AMQPError):
    ...


class ProtocolSyntaxError(AMQPError):
    ...


class UnexpectedFrameError(ProtocolSyntaxError):
    ...


class ProtocolVersionMismatch(ProtocolSyntaxError):
    ...


class BodyTooLongError(ProtocolSyntaxError):
    ...


class InvalidFrameError(ProtocolSyntaxError):
    ...


class InvalidFieldTypeException(ProtocolSyntaxError):
    ...


class UnsupportedAMQPFieldException(ProtocolSyntaxError):
    ...


class MethodNotImplemented(AMQPError):
    ...


class ChannelError(Exception):
    ...


class ReentrancyError(Exception):
    ...


class ShortStringTooLong(AMQPError):
    ...


class DuplicateGetOkCallback(ChannelError):
    ...
