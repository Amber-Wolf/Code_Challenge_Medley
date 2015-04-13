#pragma once
class BandMatrix
{
public:
	BandMatrix(int size);
	~BandMatrix(void);
	void set(int row, int col, double val);
	double get(int row, int col);
	
	friend BandMatrix operator+(const BandMatrix &c1, const BandMatrix &c2);
	void printRaw();

private:
	int convertHelp(int row, int col);
	double * band;
	int mainDiagnolLength;
};

