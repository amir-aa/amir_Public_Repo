#include <iostream>

void shift(int array[], int length, int offset) {
    // Adjust the offset to ensure it's within the array length
    offset %= length;
    
    // If offset is negative, convert it to positive
    if (offset < 0) {
        offset += length;
    }
    
    // Create a temporary array to store the shifted elements
    int temp[length];
    
    // Copy the elements to the temporary array with the shifted positions
    for (int i = 0; i < length; i++) {
        int shiftedIndex = (i + offset) % length;
        temp[i] = array[shiftedIndex];
    }
    
    // Copy the elements from the temporary array back to the original array
    for (int i = 0; i < length; i++) {
        array[i] = temp[i];
    }
}

int main() {
    int a[] = {1, 2, 3, 4, 5};
    int length = sizeof(a) / sizeof(a[0]);
    int offset = 2;
    
    shift(a, length, offset);
    
    // Print the shifted array
    for (int i = 0; i < length; i++) {
        std::cout << a[i] << " ";
    }
    
    return 0;
}
