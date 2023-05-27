#include <iostream>

void spiral(int* center, int odd_size) {
    int spiralArray[odd_size][odd_size];
    
    // Initialize the array with zeros
    for (int i = 0; i < odd_size; i++) {
        for (int j = 0; j < odd_size; j++) {
            spiralArray[i][j] = 0;
        }
    }
    
    int row = odd_size / 2;  // Initial row position
    int col = odd_size / 2;  // Initial column position
    int num = 1;             // Starting number
    
    spiralArray[row][col] = num++;  // Fill the central element
    
    // Start spiral filling
    int sideLength = 1;
    while (sideLength < odd_size) {
        // Move right
        for (int i = 0; i < sideLength; i++) {
            spiralArray[row][++col] = num++;
        }
        
        // Move down
        for (int i = 0; i < sideLength; i++) {
            spiralArray[++row][col] = num++;
        }
        
        sideLength++;
        
        // Move left
        for (int i = 0; i < sideLength; i++) {
            spiralArray[row][--col] = num++;
        }
        
        // Move up
        for (int i = 0; i < sideLength; i++) {
            spiralArray[--row][col] = num++;
        }
        
        sideLength++;
    }
    
    // Print the spiral array
    for (int i = 0; i < odd_size; i++) {
        for (int j = 0; j < odd_size; j++) {
            std::cout << spiralArray[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    int center = 1;
    int odd_size = 5;
    
    spiral(&center, odd_size);
    
    return 0;
}
