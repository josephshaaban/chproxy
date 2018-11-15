#!/usr/bin/python3

import os
import sys
import getopt
import subprocess

__version__ = 0.1

# host = '207.144.111.230'
# port = 8080


def main(argv):

    help_msg = 'chproxy -m <none|manual|auto> -p <http|https|ftp|socks> -H <proxy_host> -P <proxy_port>'
    modes = ['none', 'manual', 'auto']
    mode = 'none'
    protocols = ['http', 'https', 'ftp', 'socks']
    protocol = protocols[0]
    all_protocols = False
    host = ''
    port = ''

    try:
        opts, args = getopt.getopt(argv, "hm:p:H:P:", ["help", "mode=", "protocol=", "host=", "port=", "all-protocols"])

    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_msg)
            sys.exit()
        elif opt in ("-m", "--mode"):
            if arg in modes:
                mode = arg
            else:
                print(help_msg)
                sys.exit(2)
        elif opt in ("-p", "--protocol"):
            if arg in protocols:
                protocol = arg
        elif opt in ("-H", "--host"):
            host = arg
        elif opt in ("-P", "--port"):
            port = arg
        elif opt == "all-protocols":
            all_protocols = True

    if os.name == 'posix':
        subprocess.run('gsettings set org.gnome.system.proxy mode {}'.format(mode).split(' '))
        if mode == 'none':
            print('No proxy mode enabled.')
            sys.exit()
        elif mode == 'auto':
            print('Auto mode is not supported in this chproxy version v.{}.'.format(__version__))
        elif mode == 'manual':
            if all_protocols:
                for protocol in protocols:
                    subprocess.run('gsettings set org.gnome.system.proxy.{} host {}'.format(protocol, host).split(' '))
                    subprocess.run('gsettings set org.gnome.system.proxy.{} port {}'.format(protocol, port).split(' '))
            else:
                subprocess.run('gsettings set org.gnome.system.proxy.{} host {}'.format(protocol, host).split(' '))
                subprocess.run('gsettings set org.gnome.system.proxy.{} port {}'.format(protocol, port).split(' '))
    else:
        print('No OS except linux is supported in this chproxy version v.{}.'.format(__version__))


if __name__ == "__main__":
    main(sys.argv[1:])