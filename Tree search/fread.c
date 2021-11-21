#include <stdio.h>
#include <stdlib.h>
void main()
{
	FILE *pf = fopen("/root/phpserver72_1.4.12-xdebug.tar", "r");
	char buf[2] = {0};
	int ret = 0;
	do {
		ret = fread(buf, 1, 1, pf);
	}while (ret);
}
