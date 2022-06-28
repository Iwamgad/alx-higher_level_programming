#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node
 * @head: head
 * @number: int to add
 * Return: the address of the newNode node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newNode = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	if (!*head || (*head)->n > number)
	{
		newNode->next = *head;
		return (*head = newNode);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = newNode;
		newNode->next = current;
	}

	return (newNode);
}
