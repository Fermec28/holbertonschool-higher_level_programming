#include "lists.h"
/**
 * insert_node - insert node
 * @head: reference head of list
 * @number: number to evaluate
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if(*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{
		listint_t *aux = *head;

		while (aux->next)
		{
			if (aux->next->n > number && aux->n < number)
			{
				new_node->next = aux->next;
				aux->next = new_node;
				return (new_node);
			}
			if (aux->n == number)
			{
				new_node->next = aux->next;
				aux->next = new_node;
				return (new_node);
			}
			aux = aux->next;
		}
		new_node->next = aux->next;
		aux->next = new_node;
		return (new_node);
	}
}
