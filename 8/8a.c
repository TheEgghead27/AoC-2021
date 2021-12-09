#include <stdio.h>
#include <string.h>

int main(void) {
	char n[8];
	int total = 0, i = 0;
	while (scanf("%s", n) != EOF) {
		if (i > 10) {
		switch (strlen(n)) {
			case 2:
			case 3:
			case 4:
			case 7:
				total++;
				printf("%s taken\n", n);
				break;
			default:
				printf("failed %s\n", n);
		}
		}
		else
			printf("discarded %s\n", n);
		i++;
		if (i > 14)
			i = 0;
		
	}
	printf("%d", total);
	return 0;
}
