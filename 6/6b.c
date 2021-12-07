#include <stdio.h>
#include <stdlib.h>


main(int argc, char *argv[]) {
	long long n[9] = {0}, q[9] = {0};
	int temp;

	while (scanf("%d,", &temp) != EOF) {
		n[temp]++;
	}

	int times = atoi(argv[1]);
	printf("doing %d\n", times);

	for (int i = 0; i < times / 7; i++) {
		q[0] = n[7];
		q[1] = n[8];
		for (int j = 0; j < 7; j++)
			q[j+2] = n[j];

		n[7] = q[7];
		n[8] = q[8];
		for (int j = 0; j < 7; j++)
			n[j] += q[j];
	}
	for (int i = 0; i < times % 7; i++) {
		q[0] = n[0];
		for (int j = 1; j < 9; j++)
			n[j-1] = n[j];
		n[8] = q[0];
		n[6] += q[0];
	}

	long long sum = 0;
	for (int i = 0; i < 9; i++)
		sum += n[i];
	printf("\n%lld\n", sum);

	return 0;
}
