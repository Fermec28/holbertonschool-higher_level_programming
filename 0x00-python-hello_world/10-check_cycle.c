#include "lists.h"
/**
 * check_cycle - finds loops inside lists
 * @list: address pointer head
 * Return: 0 no loop, 1 loop
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *rabbit;

	if (list)
	{
		turtle = list;
		rabbit = list->next;
		while (turtle && rabbit && rabbit->next)
		{
			if (turtle == rabbit)
				return (1);
			turtle = turtle->next;
			rabbit = rabbit->next->next;
		}
	}
	return (0);
}
