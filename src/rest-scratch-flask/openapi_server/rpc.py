from openapi_server.rpc_ampq import RemoteProcedure as RemoteProcedureAMQP
from openapi_server.rpc_mqtt import RemoteProcedure as RemoteProcedureMQTT


def rpc_call(body_dict, routing_key, strategy_str, use_amqp=False, use_mqtt=True):
    body_dict['strategy'] = strategy_str
    response_body = body_dict
    status_code = "500"
    if use_amqp:
        rpc = RemoteProcedureAMQP(routing_key=routing_key)
        response_body, status_code = rpc.call(body_dict)
    if use_mqtt:
        rpc = RemoteProcedureMQTT(routing_key=routing_key)
        response_body, status_code = rpc.call(body_dict)
    return response_body, status_code
