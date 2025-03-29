#include <stdio.h>
#include "gamefunctions.h"
#include "towers.h"

int overlap (struct Enemy enemy, struct Status status, struct Tower* towers) {
	if ((enemy.xPosition == tower.xPosition) && (enemy.yPosition == tower.yPosition)) {
		return 1;
	}
	return 0;
}

void attack (struct Enemy enemy, struct Status status, struct Tower* towers) {
	if (overlap) {
		// towers[x] depends on where enemy xposition is
		towers[0].currentHealth -= enemy.attack;
	}
}
