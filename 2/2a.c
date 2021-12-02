#include <stdio.h>

int main(void) {
	int a;
	char arg[10];
	int x = 0, y = 0;
	int stat;

	while (scanf("%s %d", arg, &a) != EOF) {
		switch (arg[0]) {
			case 'f':
				x += a;
				break;
			case 'd':
				y += a;
				break;
			case 'u':
				y -= a;
				break;
		}
	}
	printf("%d\n", x * y);
	return 0;
}
