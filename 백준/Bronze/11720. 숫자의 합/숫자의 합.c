#include<stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int number[100] = { 0 };
	for (int i = 0; i < n; i++) {
		scanf("%1d", &number[i]);
	}
	int sum = 0;
	for (int j = 0; j < n; j++) {
		sum += number[j];
	}
	printf("%d", sum);

	return 0;
}