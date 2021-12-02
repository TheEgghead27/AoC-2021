#include <stdio.h>

int main(void) {
	int a;
	char arg[10];
	int x = 0, y = 0, aim = 0;
	int stat;

	while (scanf("%s %d", arg, &a) != EOF) {
		switch (arg[0]) {
			case 'f':
				x += a;
				y += (a * aim);
				break;
			case 'd':
				aim += a;
				break;
			case 'u':
				aim -= a;
				break;
		}
	}
	printf("%d\n", x * y);
	return 0;
}
