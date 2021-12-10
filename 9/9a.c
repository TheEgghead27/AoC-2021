#include <stdio.h>
#include <string.h>

int main(void) {
	char row[101], t[2] = "!";
	short r[3][102] ={{0},{0},{0}}, j = 1;
	short rc = 0, cc = 0;
	int total;

	while (scanf("%s", row) != EOF) {
#ifdef _DEBUG
		printf("[");
#endif
		int l = strlen(row);
		for (int i = 0; i < l; i++) {
			t[0] = row[i];
			r[j][i] = atoi(t);
#ifdef _DEBUG
			printf("%d ", r[j][i]);
#endif
	}
#ifdef _DEBUG
		printf("]\n");
#endif
		rc++;
		if (l > cc)
			cc = l;
		for (int i = 1; i <= l; i++) {
			// row[j-1][i]  // central point
			if (
					r[j-1][i] < r[(j-2)%3][i] &&  // up
					r[j-1][i] < r[(j-1)%3][i-1] && // left
					r[j-1][i] < r[(j-1)%3][i+1] &&  // right
					r[j-1][i] < r[j][i]  // down
			   ) {
				total++;
				printf("%d,%d\n", j-1, i);
			}
#ifdef _DEBUG
			printf("%d %d %d %d %d\n", r[j-1][i], r[(j-2)%3][i], r[(j-1)%3][i-1], r[(j-1)%3][i+1], r[j][i]);  // down
#endif
		}
		j++;
	}

	printf("%d %d\n", rc, cc);

	return 0;
}
