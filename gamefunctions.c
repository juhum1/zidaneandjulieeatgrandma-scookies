#include <stdio.h>

char* gainCoins(struct Status, int);
char* loseCoins(struct Status, int);
char* updatewave(struct Status, int);

char* gainCoins(struct Status status, int coins) {
	status.coins += coins;
	printf("You gained %d coins! Current coins: %d", coins, status.coins);
}

char* loseCoins(struct Status status, int coins) {
	status.coins -= coins;
	printf("You spent %d coins! Current coins: %d", coins, status.coins);
}

char* updatewave(struct Status status, int passed) {
	if (passed == 1) {
		status.wave++;
		gainCoins(status, status.coins);
	} else {
		;
	}
}

