#ifndef GAMEFUNCIONS_H
#define GAMEFUNCIONS_H

struct Status {
        int currentHealth;
        int maxHealth;
        int coins;
        int wave;
};

char* gainCoins(struct Status, int);
char* loseCoins(struct Status, int);
char* updatewave(struct Status, char[50]);

#endif
