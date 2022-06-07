#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * palindrome_rec - iterates of over a linked list 
 * @head: head is the list
 * @tail: iterates to the end of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int palindrome_rec(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);

	if (palindrome_rec(head, tail->next) == 1 && (*head)->n == tail->n)
	{
		(*head) = (*head)->next;
		return (1);
	} else 
	{
		return (0);
	}
}

/**
 * is_palindrome - Linked list palindrome
 *
 * @head: head of the linked list
 *
 * Description: checks if a linked list is a palindrom
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	if ((*head)->next == NULL)
		return (1);

	return (palindrome_rec(head, *head));
}
