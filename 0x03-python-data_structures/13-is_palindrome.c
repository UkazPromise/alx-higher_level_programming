#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to head of list
 * Return: pointer to the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
    return (*head);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head;
	listint_t *prev = NULL, *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast)
	{
		second_half = slow->next;
	}
	else
	{
		second_half = slow;
		prev->next = NULL;
	}

	listint_t *current = *head, *next = NULL;
	prev = NULL;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;

	while (second_half && *head)
	{
		if (second_half->n != (*head)->n)
			return (0);
		second_half = second_half->next;
		*head = (*head)->next;
	}
	return (1);
}
