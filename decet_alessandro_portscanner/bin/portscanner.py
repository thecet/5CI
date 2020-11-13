import argparse, nmap, logging, sys

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', \
                    filename="..//log//portscanner.log")

def scan(ip, port):
    nm = nmap.PortScanner() # instantiate nmap.PortScanner object
    ports = nm.scan(f'{ip} {port}') # scan host 127.0.0.1, ports from 22 to 443
    nm.command_line()

    with open(f'..//output//{ip}.xml', 'w') as f:
        f.write(nm.get_nmap_last_output())


def check_ip(ip):
    a = [x for x in ip.split('.') if int(x) >= 0 and int(x) < 255 ]

    if len(a) != 4:
        logging.error("Indirizzo non valido")
        return False
    
    return True



if __name__ == "__main__":


    if len(sys.argv) != 1:
        parser = argparse.ArgumentParser(description="Questo script permetti di eseguire uno scan degli indirizzi IP dati in input.")
        parser.add_argument("ip", type=str, help="IP dell'host / Primo IP dell'intervallo")
        parser.add_argument("second_ip", type=str, nargs='?',default=0, help="Ultimo IP dell'intervallo")
        parser.add_argument("port", type=str, help="Porte da scannerizzare.")
        args = parser.parse_args()
        
        if (args.second_ip == 0 and check_ip(args.ip)):
            print('1')
            scan(args.ip, args.port)
        else:
            if check_ip(args.ip) and check_ip(args.second_ip):
                ip = args.ip.split('.')
                second_ip = args.second_ip.split('.')
                for i in range(int(ip[3]), int(second_ip[3])+1):
                    print(f'{ip[0]}.{ip[1]}.{ip[2]}.{i}', args.port)
                    scan(f'{ip[0]}.{ip[1]}.{ip[2]}.{i}', args.port)

    else:   
        try:             
            for socket in open('./ip.txt', 'r'):
                socket = socket.split(',')
                if(check_ip(socket[0])):
                    scan(socket[0], socket[1])
        except:
            logging.error("file non trovato")
        

