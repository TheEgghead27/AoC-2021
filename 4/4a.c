#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int[5][5];
} board;

int main(void) {
        int n = 0, *arr;
        int a;
        while (scanf("%d", &a) != EOF) {
                n++;
                arr = realloc(arr, sizeof(int) * n);
                if (arr == NULL) {
                        fprintf(stderr, "Failed to allocated memory for arr!\n")
                        exit(1);
                }
                arr[n-1] = a;

        }
        printf();

        return 0;
}