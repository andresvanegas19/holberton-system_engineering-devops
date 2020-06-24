#include <stdio.h>
#include <sys/types.h>

/**
 * infinite_while - is an infinite a while
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - make the process
 *
 * Return: Always 0.
 */
int main(void)
{
	int counter = 0;
	pid_t pId;

	for (; counter < 5; counter++)
	{
		pId = fork();
		if (pId > 0)
			printf("Zombie process created, PID: %d\n", pId);
		else
			return;
	}
	infinite_while();

	return (0);
}
