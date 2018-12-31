#!/usr/bin/python3
#fileencrypt.py
import sys
import encryptdecrypt as ENC

ARG_INFILE=1
ARG_OUTFILE=2
ARG_KEY=3
ARG_LENGTH=4

def convertFile(infile,outfile,key):
	try:
		enc_key=int(key)
	except ValueError:
		print ("Error: The key %s should be an integer value!" % (key))
	else:
		try:
			with open(infile) as f_in:
				infile_content=f_in.readlines()
		except IOError:
			print ("Unable to open %s" % (infile))
		try:
			with open(outfile,'w') as f_out:
				for line in infile_content:
					out_line = ENC.encryptText(line,enc_key)
					f_out.writelines(out_line)
		except IOError:
			print ("Unable to open %s" % (outfile))
		print ("Conversions complete: %s" % (outfile))
	finally:
		print ("Finish")

if len(sys.argv) == ARG_LENGTH:
	print ("Command: %s" %(sys.argv))
	convertFile(sys.argv[ARG_INFILE], sys.argv[ARG_OUTFILE], sys.argv[ARG_KEY])
else:
	print ("Usage: fileencrypt.py infile outfile key")

