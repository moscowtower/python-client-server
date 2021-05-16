import json


def pack(response_dict):
    """produces message to send via tcp"""
    str_msg = json.dumps(response_dict)
    return str_msg.encode("utf-8")


def unpack(byte_str):
    """unpacks received message"""
    str_decoded = byte_str.decode('utf-8')
    return json.loads(str_decoded)


def status_200():
    msg = {
        "response": 200,
        "alert": "OK"
    }
    return pack(msg)


def status_402():
    msg = {
        "response": 402,
        "error": "Wrong credentials"
    }
    return pack(msg)


def status_409():
    msg = {
        "response": 409,
        "alert": "Conflict"
    }
    return pack(msg)