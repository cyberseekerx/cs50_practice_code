// Source - https://stackoverflow.com/a/1782327
// Posted by srikanth rongali, modified by community. See post 'Timeline' for change history
// Retrieved 2026-03-24, License - CC BY-SA 2.5

#include <stdio.h>

int main() {
    int c;
    while((c = getchar()) != EOF) { //precedence of != is greater than =, so use braces
        printf("%d\n", c);
    }
    printf("%d - at EOF\n", c);
}

