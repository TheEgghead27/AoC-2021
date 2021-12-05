#include <stdio.h>

int main(void) {
        int n[2][2];
        int m[1000][1000] = {}; // i hate myself, a lot
        int ux = 0, uy = 0;
        int a, b, x, y;
        int total = 0;

        while(scanf("%d,%d -> %d,%d", n[0], n[0]+1, n[1], n[1]+1) != EOF) {
                // this one is vertical or horizontal no diagonal yet but im scared mom
                if (n[0][0] == n[1][0]) {  // compare x
                        x = n[0][0];
                        if (n[0][1] >= n[1][1])
                                {a = n[0][1]; b = n[1][1];}
                        else
                                {a = n[1][1]; b = n[0][1];}
                        for (y = b; y <= a; y++)  // we need inclusive
                                m[x][y] += 1;
                }
                else if (n[0][1] == n[1][1]) { // compare y
                        y = n[0][1];
                        if (n[0][0] >= n[1][0])
                                {a = n[0][0]; b = n[1][0];}
                        else
                                {a = n[1][0]; b = n[0][0];}
                        for (x = b; x <= a; x++)
                                m[x][y] += 1;
                }

                if (x > ux)
                        ux = x;
                if (y > uy)
                        uy = y;
        }
        for (int i = 0; i <= ux; i++) {
#ifdef _DEBUG
                printf("\n[");
#endif
                for (int j = 0; j <= uy; j++) {
#ifdef _DEBUG
                        if (m[i][j])
                                printf("%d ", m[i][j]);
                        else
                                printf(". ");
#endif
                        if (m[i][j] > 1)
                                total++;

                }
#ifdef _DEBUG
                printf("]");
#endif
        }

        /*
        printf("Outputs:\n%d\n%d\n%d\n%d", n[0][0], n[0][1], n[1][0], n[1][1]);
        printf("\n%lu\n", sizeof(int) * 1000 * 1000);
         */
        printf("\n%d\n", total);

        return 0;
}