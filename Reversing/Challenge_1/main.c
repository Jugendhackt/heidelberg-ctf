#include <stdio.h>
#include <string.h>

char part1[] = "BASE64 String: SkhIREN";
char unused[] = "password: ";
char passwort[] = "PASS6565WORT";
char unused2[] = " ";
char part2[] = "URntsYW";
char error[] = "Falsches Passwort!\r\n";
char part3[] = "93cWt9";

int main(int argc, char* argv[]) {
	if (strcmp(passwort, argv[1]) == 0) {
		printf("%s%s%s\r\n", part1, part2, part3);
		return 0;
	}
	printf(error);
	return 11;
}