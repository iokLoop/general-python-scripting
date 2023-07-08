def simple_vlan_check(ip):
    ip_address = ip.split('.')  # Split IPs into octets
    octet_1 = int(ip_address[0])
    octet_2 = int(ip_address[1])
    octet_3 = int(ip_address[2])
    octet_4 = int(ip_address[3])

    #for 192.168.0.0/23   512 IPs   (192.168.0.1 - 192.168.1.254)
    if octet_1 == 192 and octet_2 == 168 and 0 <= octet_3 <= 1 and 1 <= octet_4 <= 254:
        return "VLAN 1"
    #for 192.168.2.0/26   64 IPs    (192.168.2.1 - 192.168.2.62)
    elif octet_1 == 192 and octet_2 == 168 and octet_3 == 2 and 1 <= octet_4 <= 62:
        return "VLAN 2"
    #for 192.168.2.64/27  32 IPs    (192.168.2.65 - 192.168.2.95)
    elif octet_1 == 192 and octet_2 == 168 and octet_3 == 2 and 65 <= octet_4 <= 95:
        return "VLAN 3"
    #for 192.168.2.96/22  1,024 IPs (192.168.2.97 - 192.168.6.95)
    elif octet_1 == 192 and octet_2 == 168 and octet_3 == 2 and 97 <= octet_4 <= 254:
        return "VLAN 4"
    elif octet_1 == 192 and octet_2 == 168 and 3 <= octet_3 <= 5 and 0 <= octet_4 <= 254:
        return "VLAN 4"
    elif octet_1 == 192 and octet_2 == 168 and octet_3 == 6 and 0 <= octet_4 <= 95:
        return "VLAN 4"
    else:
        return "Unknown VLAN"

ip_addresses = [
    '192.168.1.30',
    '192.168.10.98',
    '192.168.5.10',
    '192.168.2.20',
    '192.168.2.70',
    '192.168.1.12',
    '192.168.0.100',
    '192.168.7.50',
    '192.168.6.0'
]

for ip in ip_addresses:
    vlan = simple_vlan_check(ip)
    print(f"The IP address {ip} belongs to {vlan}")

