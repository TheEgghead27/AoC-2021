#include <stdio.h>

int main(void) {
	int n = 0;
	char input[20];
	scanf("%s", input);
	while (input[n] != '\0')
		n++;  // count string length
	int a[n]; // loop breaks at null, = strlen
	do {
		for (int i = 0; i < n; i++) {
			if (input[i] == '1')
				
	} while (scanf("%s", input) != EOF);
	return 0;
}
