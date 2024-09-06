# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from urltoimage import urltoimage_pb2 as urltoimage_dot_urltoimage__pb2


class UrltoimageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Convert = channel.unary_unary(
                '/liburltoimage.Urltoimage/Convert',
                request_serializer=urltoimage_dot_urltoimage__pb2.Request.SerializeToString,
                response_deserializer=urltoimage_dot_urltoimage__pb2.Response.FromString,
                )


class UrltoimageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Convert(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UrltoimageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Convert': grpc.unary_unary_rpc_method_handler(
                    servicer.Convert,
                    request_deserializer=urltoimage_dot_urltoimage__pb2.Request.FromString,
                    response_serializer=urltoimage_dot_urltoimage__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'liburltoimage.Urltoimage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Urltoimage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Convert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/liburltoimage.Urltoimage/Convert',
            urltoimage_dot_urltoimage__pb2.Request.SerializeToString,
            urltoimage_dot_urltoimage__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
