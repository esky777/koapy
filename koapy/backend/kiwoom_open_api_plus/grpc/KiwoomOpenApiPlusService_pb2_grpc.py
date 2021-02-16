# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from koapy.backend.kiwoom_open_api_plus.grpc import KiwoomOpenApiPlusService_pb2 as koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2


class KiwoomOpenApiPlusServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/Call',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallResponse.FromString,
                )
        self.Listen = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/Listen',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.BidirectionalListen = channel.stream_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/BidirectionalListen',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.BidirectionalListenRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.CustomListen = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/CustomListen',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.CustomCallAndListen = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/CustomCallAndListen',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallAndListenRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallAndListenResponse.FromString,
                )
        self.LoginCall = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/LoginCall',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.LoginRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.TransactionCall = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/TransactionCall',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.TransactionRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.OrderCall = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/OrderCall',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.OrderRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.RealCall = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/RealCall',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.RealRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.LoadConditionCall = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/LoadConditionCall',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.LoadConditionRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.ConditionCall = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/ConditionCall',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ConditionRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.BidirectionalRealCall = channel.stream_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/BidirectionalRealCall',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.BidirectionalRealRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.OrderListen = channel.unary_stream(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/OrderListen',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
                )
        self.SetLogLevel = channel.unary_unary(
                '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/SetLogLevel',
                request_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.SetLogLevelRequest.SerializeToString,
                response_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.SetLogLevelResponse.FromString,
                )


class KiwoomOpenApiPlusServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Listen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BidirectionalListen(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CustomListen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CustomCallAndListen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoginCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransactionCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RealCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadConditionCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConditionCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BidirectionalRealCall(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderListen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLogLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KiwoomOpenApiPlusServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallResponse.SerializeToString,
            ),
            'Listen': grpc.unary_stream_rpc_method_handler(
                    servicer.Listen,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'BidirectionalListen': grpc.stream_stream_rpc_method_handler(
                    servicer.BidirectionalListen,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.BidirectionalListenRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'CustomListen': grpc.unary_stream_rpc_method_handler(
                    servicer.CustomListen,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'CustomCallAndListen': grpc.unary_stream_rpc_method_handler(
                    servicer.CustomCallAndListen,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallAndListenRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallAndListenResponse.SerializeToString,
            ),
            'LoginCall': grpc.unary_stream_rpc_method_handler(
                    servicer.LoginCall,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.LoginRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'TransactionCall': grpc.unary_stream_rpc_method_handler(
                    servicer.TransactionCall,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.TransactionRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'OrderCall': grpc.unary_stream_rpc_method_handler(
                    servicer.OrderCall,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.OrderRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'RealCall': grpc.unary_stream_rpc_method_handler(
                    servicer.RealCall,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.RealRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'LoadConditionCall': grpc.unary_stream_rpc_method_handler(
                    servicer.LoadConditionCall,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.LoadConditionRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'ConditionCall': grpc.unary_stream_rpc_method_handler(
                    servicer.ConditionCall,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ConditionRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'BidirectionalRealCall': grpc.stream_stream_rpc_method_handler(
                    servicer.BidirectionalRealCall,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.BidirectionalRealRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'OrderListen': grpc.unary_stream_rpc_method_handler(
                    servicer.OrderListen,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.SerializeToString,
            ),
            'SetLogLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLogLevel,
                    request_deserializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.SetLogLevelRequest.FromString,
                    response_serializer=koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.SetLogLevelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KiwoomOpenApiPlusService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/Call',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Listen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/Listen',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BidirectionalListen(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/BidirectionalListen',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.BidirectionalListenRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CustomListen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/CustomListen',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CustomCallAndListen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/CustomCallAndListen',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallAndListenRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.CallAndListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoginCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/LoginCall',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.LoginRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransactionCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/TransactionCall',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.TransactionRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/OrderCall',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.OrderRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RealCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/RealCall',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.RealRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadConditionCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/LoadConditionCall',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.LoadConditionRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConditionCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/ConditionCall',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ConditionRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BidirectionalRealCall(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/BidirectionalRealCall',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.BidirectionalRealRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderListen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/OrderListen',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.ListenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLogLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/koapy.backend.kiwoom_open_api_plus.grpc.KiwoomOpenApiPlusService/SetLogLevel',
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.SetLogLevelRequest.SerializeToString,
            koapy_dot_backend_dot_kiwoom__open__api__plus_dot_grpc_dot_KiwoomOpenApiPlusService__pb2.SetLogLevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
