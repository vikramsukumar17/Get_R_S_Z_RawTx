import bitcoin
import hashlib
import shiky_Utils
import AOU_Utils
#edit tx and pute your raw tx
tx = "0100000001889844f7f301ebbd6a49f10563b39950033d9923d946570203a580c6f30c0dbd020000008a473044022015a40e5a229aa0df7611f5c960990fe9c18800e23651640841c110fe181c08df02205ac96d78880b06ce98177245adfce4f42b9569bdbbc1a346d43fb330d32f343d014104a5b91ee4d776896b73309ed7b6ae323468fb01b5b18e50d5c67670a2c6cbc11bde1f58478d2e7531425625792f721b60f02982d81ebfbbe4fd3d09e388864b79ffffffff01e994b900000000001976a914d75023c7e22517552f0d4b6e16755c05e15dc3a988ac00000000"
m = shiky_Utils.parseTxn(tx)
e = shiky_Utils.getSignableTxn(m)
z = hashlib.sha256(hashlib.sha256(e.decode('hex')).digest()).digest()
z1 = z[::-1].encode('hex_codec')
z = z.encode('hex_codec')
s = AOU_Utils.derSigToHexSig(m[1][:-2])
pub =  m[2]
sigR = s[:64]
sigS = s[-64:]
sigZ = z
print ('Signed TX is :', tx)
print ('Signature (r, s pair) is :', s)
print ('Public Key is :', pub)
print ("")
print ("#################################################################################################")
print ("")
print ('Unsigned TX is :', e)
print ('hash of message (sigZ) is USE This ONE :', z)
print ('reversed z :', z1)
print ("")
print ("#################################################################################################")
print ("##################################VALUES NEEDED ARE BELOW #######################################")
print ("#################################################################################################")
print ("")
print ('THE R VALUE is  :', sigR)
print ('THE S VALUE is  :', sigS)
print ('THE Z VALUE is  :', sigZ)
print ('THE PUBKEY is :', pub)


