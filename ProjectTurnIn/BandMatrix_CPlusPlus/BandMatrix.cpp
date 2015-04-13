#include "BandMatrix.h"
#include <iostream>

#define bloop

BandMatrix::BandMatrix(int size){
	mainDiagnolLength = size;
	int indices = (size + 2 * (size - 1));
	band = new double[(size + 2 * (size - 1))];
}

BandMatrix::~BandMatrix(void){
	
}

void BandMatrix::set(int row, int col, double val){
	int index = convertHelp(row,col);
#ifdef bloop
	//std::cout << "blah" << std::endl;
#endif
	if(index == -1){
	}else{
		band[index] = val;
	}
}

double BandMatrix::get(int row, int col){
	int index = convertHelp(row,col);
	if(-1){
		return 0;
	}else{
		return band[index];
	}
}

int BandMatrix::convertHelp(int row, int col){
	int val = -1;
	int shift = row - col;
	if( (mainDiagnolLength <= row) || (mainDiagnolLength <= col) ){
#ifdef bloop
	std::cout << val << std::endl;
#endif
		return -1;
	} else {
		int shift = row - col;
		int shift2 = row;
		if((shift > 1) || (shift < -1) ){
#ifdef bloop
	std::cout << val << std::endl;
#endif
			return -1;
		}
		if(-shift + row >= mainDiagnolLength){
#ifdef bloop
	std::cout << val << std::endl;
#endif
			return -1;
		}
		if(shift == -1){
			val = row;
		}else if(shift == 0){
			val = mainDiagnolLength - 1 + row;
		}else if(shift == 1){
			val = mainDiagnolLength * 2 - 2 + row;
		}
	}
#ifdef bloop
	std::cout << val << std::endl;
#endif
	return val; 
}

BandMatrix operator+(const BandMatrix &b1, const BandMatrix &b2){
	BandMatrix bm(b1.mainDiagnolLength);
	if(b1.mainDiagnolLength == b2.mainDiagnolLength){
		for(int x=0; x<(b1.mainDiagnolLength + 2 * (b1.mainDiagnolLength - 1)); x++){
			bm.band[x] = b1.band[x] + b2.band[x];
		}
	}else{
		std::cout << "You screwed up.  The matrix sizes are not the same.";
	}
	return bm;
}

void BandMatrix::printRaw(){
	for(int x=0; x<(mainDiagnolLength + 2 * (mainDiagnolLength - 1)); x++){
		std::cout << band[x] << " ";
	}
	std::cout << std::endl;
}