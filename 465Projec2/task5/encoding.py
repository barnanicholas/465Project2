import codecs


hexlify = codecs.getencoder('hex')
print(hexlify(b"sudo reboot\n")[0])