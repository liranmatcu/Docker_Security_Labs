#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void main()
{
	setuid(geteuid());
	system("/bin/cat /etc/shadow");
}