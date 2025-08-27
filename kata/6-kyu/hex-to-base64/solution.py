import base64
def hex_to_base64(hex: str) -> str:
    bytes_data = bytes.fromhex(hex)
    base64_bytes = base64.b64encode(bytes_data)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string