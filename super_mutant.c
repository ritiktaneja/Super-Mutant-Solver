#include<stdbool.h>
int solve(int a, int b, int c, bool flag1, bool flag2, bool flag3, bool flag4, bool flag5, bool flag6, bool flag7, bool flag8) {
    int s1 = (flag1) ? (b + b) : (flag2 ? (b - b) : (b * b));
    int s2 = 2 * a * c * (flag3 ? 2 : (flag4 ? 1 : -1) );
    int s3 = (flag5) ? (s1 * s2) : (flag6 ? (s1 + s2) : (s1 - s2));
    if(flag7) s3++;
    if(flag8) s3 *= -1;
    return s3;
}

// Correct F F T X F F F F