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
		sleep(1);
	return (0);
}

/**
 * process - is a simple function
 * @counter: is the times a process is created
 */
void process(int counter)
{
	pid_t pId;

	while (counter >= 0)
	{
		pId = fork();
		if (pId < 1)
			return;
		printf("Zombie process created, PID: %d\n", pId);
		counter -= 1;
	}

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
	infinite_while();

	return (0);
}
