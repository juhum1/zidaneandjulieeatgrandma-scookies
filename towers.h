#ifndef TOWERS_H
#define TOWERS_H

struct Tower {
        int currentHealth;
        int maxHealth;
        int damage;
	int range; // in y-direction
	//int attackSpeed;
};

void attack (struct Tower* towers, struct Enemy enemy);

#endif
