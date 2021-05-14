#include <stdio.h>

void int main()
{
	setuid(geteuid());
	system("/bin/cat /etc/shadow")
}