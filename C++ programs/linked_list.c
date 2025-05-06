#include <stdio.h>
#include <stdlib.h>

// Define the structure for a singly linked list node
struct Node
{
    int data;
    struct Node *next;
};

// Function to create a new node
struct Node *createNode(int data)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode == NULL)
    {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to add a new node at the end of the list
void addNode(struct Node **head, int data)
{
    struct Node *newNode = createNode(data);
    if (*head == NULL)
    {
        *head = newNode;
    }
    else
    {
        struct Node *temp = *head;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

// Function to delete a node with a given value
void deleteNode(struct Node **head, int data)
{
    if (*head == NULL)
    {
        printf("List is empty!\n");
        return;
    }
    struct Node *temp = *head;
    struct Node *prev = NULL;
    while (temp != NULL && temp->data != data)
    {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL)
    {
        printf("Node with value %d not found!\n", data);
        return;
    }
    if (prev == NULL)
    {
        *head = temp->next;
    }
    else
    {
        prev->next = temp->next;
    }
    free(temp);
}

// Function to find a node with a given value
struct Node *findNode(struct Node *head, int data)
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        if (temp->data == data)
        {
            return temp;
        }
        temp = temp->next;
    }
    return NULL;
}

// Function to print the linked list
void printList(struct Node *head)
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main()
{
    struct Node *head = NULL;
    int n, value;

    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("Enter value for node %d: ", i + 1);
        scanf("%d", &value);
        addNode(&head, value);
    }

    printf("Original list: ");
    printList(head);

    printf("Enter a value to delete: ");
    scanf("%d", &value);
    deleteNode(&head, value);
    printf("List after deleting node with value %d: ", value);
    printList(head);

    printf("Enter a value to find: ");
    scanf("%d", &value);
    struct Node *foundNode = findNode(head, value);
    if (foundNode)
    {
        printf("Node with value %d found!\n", value);
    }
    else
    {
        printf("Node with value %d not found!\n", value);
    }

    return 0;
}
