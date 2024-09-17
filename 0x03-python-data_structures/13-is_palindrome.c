#include <stddef.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *current = head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *second_half, *prev_of_slow = NULL;
    int is_pal = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_of_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        second_half = slow->next;
    }
    else
    {
        second_half = slow;
    }

    prev_of_slow->next = NULL;
    second_half = reverse_list(second_half);
    listint_t *copy_second_half = second_half;

    while (*head != NULL && second_half != NULL)
    {
        if ((*head)->n != second_half->n)
        {
            is_pal = 0;
            break;
        }
        *head = (*head)->next;
        second_half = second_half->next;
    }

    reverse_list(copy_second_half);
    return is_pal;
}
