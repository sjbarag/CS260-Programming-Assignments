#include <stdio.h>
#include <cstdlib>
#include <iostream>
using namespace std;

#define maxlength 100 	/* from page 41 of Aho, Hopcraft, and Ullman */

/* Does not handle lists longer than 100 elements, by design.
 * the user-facing size is modulated by changing last & position.
 */
struct ArrayList	// No intentional relation to Java's ArrayList class!
{
	int list[maxlength];	// The list of all data in this ArrayList
	int last;		// The position of the last usable data element
	int position;		// The current position of the "cursor"
};

int MAKENULL(ArrayList *L);
int FIRST(ArrayList *L);
int END(ArrayList *L);
int RETREIVE(int pos, ArrayList *L);
int LOCATE(int val, ArrayList *L);
int NEXT(ArrayList *L);
int PREVIOUS(ArrayList *L);
void INSERT(int val, int pos, ArrayList *L);
void DELETE(int pos, ArrayList *L);

int MAKENULL(ArrayList *L)
{
	(*L).last = -1;	// indexing starts at zero!
	(*L).position = -1;
	return END(L);
}

int FIRST(ArrayList *L)
{
	return 0;
}

int END(ArrayList *L)
{
	return (*L).last++;
}

int RETREIVE(int pos, ArrayList *L)
{
	return (*L).list[pos];	// no error handling - other values/fringe cases are undefined.
}

int LOCATE(int val, ArrayList *L)
{
	for( int i = 0; i < END(L); i++ )
		if ( (*L).list[i] == val )
			return i;
	return END(L);
}

int NEXT(ArrayList *L)
{
	if( (*L).position == (*L).last )
		return END(L);
	else
		return (*L).position++;
}

int PREVIOUS(ArrayList *L)
{
	return (*L).position--;
}

// head insertion
void INSERT(int val, ArrayList *L)
{
	//skipping undefined cases ;)
	for( int i = (*L).last; i >= 0; i-- )
		(*L).list[i+1] = (*L).list[i];
	(*L).last++;
	(*L).list[0] = val;
}

void DELETE(int pos, ArrayList *L)
{
	(*L).last--;
	for( int i = pos; i < END(L); i++)
		(*L).list[i] = (*L).list[i+1];
}

int main()
{
	cout << "Herp derp";
}