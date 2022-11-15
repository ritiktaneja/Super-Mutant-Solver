// File1 : reference_solution.c File2 : super_mutant.c
#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<string.h>

void klee_assume();

void klee_make_symbolic();

int solve1(int a, int b, int c) {
    int s1 = b * b;
    int s2 = 4 * a * c;
    int s3 = s1 - s2;
    return s3;
}


#include<stdbool.h>
int solve2(int a, int b, int c, bool flag1, bool flag2, bool flag3, bool flag4, bool flag5, bool flag6, bool flag7, bool flag8) {
    int s1 = (flag1) ? (b + b) : (flag2 ? (b - b) : (b * b));
    int s2 = 2 * a * c * (flag3 ? 2 : (flag4 ? 1 : -1) );
    int s3 = (flag5) ? (s1 * s2) : (flag6 ? (s1 + s2) : (s1 - s2));
    if(flag7) s3++;
    if(flag8) s3 *= -1;
    return s3;
}

// Correct F F T X F F F F


int main()
{
	int a;
	klee_make_symbolic(&a,sizeof(a),"a");
	 klee_assume(a > 0); 
	klee_assume(a < 65536); 
	int b;
	klee_make_symbolic(&b,sizeof(b),"b");
	 klee_assume(b > 0); 
	klee_assume(b < 65536); 
	int c;
	klee_make_symbolic(&c,sizeof(c),"c");
	 klee_assume(c > 0); 
	klee_assume(c < 65536); 
	int return_value_1 = solve1(a,b,c);
	int return_value_2 = solve2(a,b,c, false, false, false, false, true, true, true, true);

	assert(return_value_1 == return_value_2); 

	return 0; 
 }