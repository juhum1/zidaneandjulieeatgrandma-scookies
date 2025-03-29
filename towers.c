#include <stdio.h>

void attack (struct Tower* towers, struct Enemy enemy) {
	//tower based on xposition
	if (enemy.yPosition <= towers[0].range) {
		enemy.currentHealth -= towers[0].damage;
	}
}
