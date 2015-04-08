import wikipedia
import sys

def useCommandLineInput():
	while True:
		print("\nwhat would you like to search?")
		toSearch = raw_input("enter here: ")
		if (toSearch == "q"):
			break
		try:
			print wikipedia.summary(toSearch, sentences = 2)
		except wikipedia.exceptions.DisambiguationError:
			print "there was an error!"

def useFileIO():
	print "\n\twhat file should be read from?"
	inFile = raw_input("\tenter here: ")
	if (inFile == 'q'):
		quit()
	
	try:
		toSearch = open(inFile, 'r')
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		quit()

	print "\n\twhat file should be written to?"
	outFile = raw_input("\tenter here: ")
	if (outFile == 'q'):
		quit()
	
	try:
		toWrite = open(outFile, 'w')
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		quit()

	sys.stdout.write( "Processing" )
	sys.stdout.flush();

	for line in toSearch:
		line = line[:-1]
		toWrite.write("\n" + line + ":\n\t")
		try:
			toWrite.write( wikipedia.summary(line, sentences = 2).encode('utf8'))
		except wikipedia.exceptions.DisambiguationError:
			toWrite.write( "Multiple results" )
		except wikipedia.exceptions.PageError:
			toWrite.write( "No results found" )
		toWrite.write("\n")
		sys.stdout.write('.')
		sys.stdout.flush();
	
	print "Done!"

	toSearch.close()
	toWrite.close()


def main():
	print "\n\tHow would you like to use this program?"
	print "\t (1) Command Line Input/Standard Output" 
	print "\t (2) File Input/Output"
	print "\t (enter q at anytime to quit)"
	while True:
		answer = raw_input("\n\tenter here: ")
		if (answer == '1'):
			useCommandLineInput()
			quit()
		elif (answer == '2'):
			useFileIO()
			quit()
		elif (answer == 'q'):
			quit()
		else:
			print "\n\tYour input was not understood."
			print "\tPlease try again."


main()