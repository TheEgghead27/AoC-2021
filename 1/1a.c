#include <stdio.h>

int main(void) {
	int total = 0;
	int x, y;
	scanf("%d", &x);
	while (scanf("%d", &y) != EOF) {
		if (y > x)
			total++;
		x = y;
	}
	printf("%d\n", total);
	return 0;
}
