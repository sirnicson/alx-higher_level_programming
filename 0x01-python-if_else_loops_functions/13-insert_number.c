#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the list.
 * @number: The number to insert.
 * 
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node, *current, *prev;

    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    new_node->n = number;
    current = *head;
    prev = NULL;

    while (current && current->n < number) {
        prev = current;
        current = current->next;
    }

    if (prev)
        prev->next = new_node;
    else
        *head = new_node;

    new_node->next = current;

    return (new_node);
}
