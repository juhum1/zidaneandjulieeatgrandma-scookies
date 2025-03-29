#ifndef ENEMIES_H
#define ENEMIES_H

struct Enemy {
     	char name[100];
	int currentHealth;
        int maxHealth;
        float xPosition;
        float yPosition;
	int damage;
};

int overlap (struct Enemy enemy, struct Status status, struct Tower* towers);
void attack (struct Enemy enemy, struct Status status, struct Tower* towers);

#endif
