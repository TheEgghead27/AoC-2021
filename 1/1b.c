#include <stdio.h>

int main(void) {
	int total = 0, n;
	int a = 0, b = 0, c = 0;
	int d = 0, e = 2, f = 1;
	int at = 0, bt = 0, ct = 0;
	while (scanf("%d", &n) != EOF) {
		a += n;
		b += n;
		c += n;

		d++;
		e++;
		f++;
		if (d > 2) {
			at = a;
			if (at > ct) {
                                printf("%d (a) more than %d (c)\n", at, ct);
                                total++;
                        }
			a = 0;
			d = 0;
		}
		if (e > 2) {
			bt = b;
			if (bt > at) {
                                printf("%d (b) more than %d (a)\n", bt, at);
                                total++;
                        }
			b = 0;
			e = 0;
		}
		if (f > 2) {
			ct = c;
			if (ct > bt) {
                                printf("%d (c) more than %d (b) \n", ct, bt);
                                total++;
                        }
			c = 0;
			f = 0;
		}
	}
	total -= 3; // assuming no negative values at the start, we have extra comparison when isn't ready
	printf("%d\n", total);
	return 0;
}
