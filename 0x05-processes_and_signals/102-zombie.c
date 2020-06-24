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
 * process - is a simple function
 * @counter: is the times a process is created
 */
void process(int counter)
{
	pid_t pId;

	for (;counter > 0; counter--)
	{
		pId = fork();
		if (pId > 0)
			printf("Zombie process created, PID: %d\n", pId);
		else
			return;
	}
	infinite_while();
}

/**
 * main - make the process
 *
 * Return: Always 0.
 */
int main(void)
{
	int time_create = 5;

	process(time_create);

	return (0);
}
