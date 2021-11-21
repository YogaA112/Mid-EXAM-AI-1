#include <stdio.h>
#include <stdlib.h>
void main()
{
	int fd = open("/root/phpserver72_1.4.12-xdebug.tar", 0);
	char buf[2] = {0};
	int ret = 0;
	do {
		ret = read(fd, buf, 1);
	}while (ret);
}
