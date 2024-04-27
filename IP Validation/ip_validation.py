def is_valid_IP(ip):
    octets = ip.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False
    
    for octet in octets:
        # Check if octet is a valid integer
        if not octet.isdigit():
            return False
        
        # Check if octet is within range [0, 255] and doesn't have leading zeros
        if not (0 <= int(octet) <= 255) or (len(octet) > 1 and octet[0] == '0'):
            return False
    
    return True