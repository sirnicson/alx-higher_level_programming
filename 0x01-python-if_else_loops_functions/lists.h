#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Node of a singly linked list.
 * @n: Integer.
 * @next: Pointer to the next node.
 */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
