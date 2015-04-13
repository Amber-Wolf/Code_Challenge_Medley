#include <stdio.h>
#include "BandMatrix.h"

int main( int argc, const char* argv[]){
	BandMatrix bm(10);
	BandMatrix bm2(10);
	bm.set(2,2,7);
	bm.printRaw();
	bm.set(2,3,9);
	bm.set(4,5,2.7);
	bm.set(6,7,3.2);
	bm.set(9,9,28);
	
	//formal tests
	bm.set(0,1,29);
	bm.set(8,9,30);
	bm.set(0,0,31);
	bm.set(9,9,32);
	bm.set(1,0,33);
	bm.set(9,8,34);
	
	bm.printRaw();
	
	bm.set(7,9,99);
	bm.set(9,7,99);
	
	//+ tests
	
	bm2.set(9,8, 34);
	(bm + bm2).printRaw();
}