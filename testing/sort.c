#include <stdio.h>
#include <stdlib.h>

void sort(int*, int);

int main() {
  int array[] = {2,5,3,9,8,7};
  
  for (int i = 0; i < sizeof(array)/sizeof(array[0]); i++)
    printf("%d ", array[i]);

  sort(array, sizeof(array)/sizeof(array[0]));

  for (int i = 0; i < sizeof(array)/sizeof(array[0]); i++)
    printf("%d ", array[i]);  
}

void sort(int* array, int size) {
  int temp = 0;

  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size - 1; j++) {
      if (array[j] > array[j + 1]) {
        temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
}
