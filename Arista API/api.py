
#!/usr/bin/python 
import jsonrpclib 
from jsonrpclib import Server 
switch = Server( "https://fabrice:fabrice@172.16.201.2/command-api" ) 
response = switch.runCmds( 1, [ "show hostname" ] ) 
print "Hello, my name is: ", response[0][ "hostname" ] 
response = switch.runCmds( 1, [ "show version" ] ) 
print "My MAC address is: ", response[0][ "systemMacAddress" ] 
print "My version is: ", response[0][ "version" ]
print "architecture:", response[0] ["architecture"]

