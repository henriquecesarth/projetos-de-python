from classes.calc_ipv4 import CalcIPv4

calc_ipv4 = CalcIPv4(ip='192.168.0.1', prefixo=12)

print(f'IP: {calc_ipv4.ip}')
print(f'Máscara: {calc_ipv4.mascara}')
print(f'Rede: {calc_ipv4.rede}')
print(f'Broadcast: {calc_ipv4.broadcast}')
print(f'Prefixo: {calc_ipv4.prefixo}')
print(f'Número de IPs da rede: {calc_ipv4.numero_ips}')

print()

calc_ipv4_2 = CalcIPv4(ip='192.168.0.1', mascara='255.255.255.63')

print(f'IP: {calc_ipv4_2.ip}')
print(f'Máscara: {calc_ipv4_2.mascara}')
print(f'Rede: {calc_ipv4_2.rede}')
print(f'Broadcast: {calc_ipv4_2.broadcast}')
print(f'Prefixo: {calc_ipv4_2.prefixo}')
print(f'Número de IPs da rede: {calc_ipv4_2.numero_ips}')

print()

calc_ipv4_3 = CalcIPv4(ip='192.168.0.1', mascara='255.255.255.63', prefixo=30)

print(f'IP: {calc_ipv4_3.ip}')
print(f'Máscara: {calc_ipv4_3.mascara}')
print(f'Rede: {calc_ipv4_3.rede}')
print(f'Broadcast: {calc_ipv4_3.broadcast}')
print(f'Prefixo: {calc_ipv4_3.prefixo}')
print(f'Número de IPs da rede: {calc_ipv4_3.numero_ips}')