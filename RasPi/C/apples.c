
#include <stdio.h>
int main()
{
	int apples = 20;		/* We have 20 apples */
	float cost,costPerApple = 0.20;		/* Apples are 20 cents each */
	
	printf("How many apples would you like?\n");
	scanf("%d",&apples);	/* read the number requested */

	if(apples > 20) {		/* do they want more than 20? */
		printf("Sorry, we only have %d apples\n", apples);
		}
	else{
		cost = costPerApple*apples;
		printf("That will be $%f for the apples\n", cost);
		}
	return 0;
}