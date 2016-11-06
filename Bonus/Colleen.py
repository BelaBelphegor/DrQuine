def nothing():
	pass

def main():
	# THIS IS COMMENT
	s = "def nothing():{:s}pass{:s}def main():{:s}# THIS IS COMMENT{:s}s = {:s}print(s.format((chr(10) + chr(9)), (chr(10) + chr(10)), (chr(10) + chr(9)), (chr(10) + chr(9)), (chr(34) + s + chr(34) + chr(10) + chr(9)), (chr(10) + chr(10)), chr(10))){:s}main(){:s}# THIS IS SECOND COMMENT"
	print(s.format((chr(10) + chr(9)), (chr(10) + chr(10)), (chr(10) + chr(9)), (chr(10) + chr(9)), (chr(34) + s + chr(34) + chr(10) + chr(9)), (chr(10) + chr(10)), chr(10)))

main()
# THIS IS SECOND COMMENT
