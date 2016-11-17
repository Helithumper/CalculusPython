import parser
from math import *
import argparse
import sys
import time

def main(fx, a, b, n):

	#Define the function
	#print("FUNCTION: ", fx);
	functioncode = parser.expr(fx).compile();
	#print("A: ",a);
	#print("B: ",b);
	#print("N: ",n);

	#Get Ends (y0 and yn)
	x = a;
	ares = eval(functioncode);
	x = b;
	bres = eval(functioncode);
	sumends = (float)(ares + bres);
	#print(sumends);



	#find the common height of all the rhombuses
	difference = (float)(b-a)/n
	#print(difference);


	#find the sum of double the side length of each rhombus
	suminterior = 0;
	incrementor = a+difference;
	currentItem = 0;
	while incrementor < b:
		x=incrementor;
		suminterior = suminterior + (2*eval(functioncode));
		#print("SUMINTERIOR",suminterior)
		#print("INCREMENTOR", incrementor)
		incrementor = incrementor + difference;
		currentItem = currentItem+1;
		printProgress(currentItem, args.n, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

	print();
	print("RESULT:",(difference/2)*(sumends+suminterior))


# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '|' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()






#Handle Argument Parsing
argparser = argparse.ArgumentParser(description='Compute Rhombus Integrals!')
argparser.add_argument("function", help = "function to compute", type=str)
argparser.add_argument("a", help = "initial a value", type=int);
argparser.add_argument("b", help = "initial b value", type=int);
argparser.add_argument("n", help = "number of rhombuses to split the range into", type=int);

args = argparser.parse_args();






# Initial call to print 0% progress
printProgress(0, args.n, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
intitialTime = time.time()
main(args.function,args.a,args.b,args.n);
timeelapsed = time.time() - intitialTime
print("TIME ELAPSED: ", timeelapsed);
