#include <stdio.h>
#include <stdlib.h>
#include <libmemcached/memcached.h>
#include <unistd.h>

#define MEMCACHED_SERVER "127.0.0.1"
#define MEMCACHED_PORT 11211
#define OUTPUT_FILE "output.txt"

int main() {
    memcached_st *memc;
    memcached_return rc;

    // Create a new memcached connection
    memc = memcached_create(NULL);

    // Add Memcached server to the connection
    memc = memcached_server_add(memc, MEMCACHED_SERVER, MEMCACHED_PORT);

    // Open the output file for appending
    FILE *output_file = fopen(OUTPUT_FILE, "a");
    if (!output_file) {
        fprintf(stderr, "Error opening file %s\n", OUTPUT_FILE);
        exit(EXIT_FAILURE);
    }

    while (1) {
        // Key for the value you want to retrieve from Memcached
        const char *key = "your_key";

        // Buffer to store the retrieved value
        char value[1024];  // Adjust the size based on your expected value size

        // Get the value from Memcached
        size_t value_length;
        uint32_t flags;
        memcached_return_t ret;
        char* result = memcached_get(memc, key, strlen(key), &value_length, &flags, &ret);

        if (ret == MEMCACHED_SUCCESS) {
            // Append the value to the output file
            fprintf(output_file, "%s\n", result);

            // Free the result
            free(result);
        } else {
            fprintf(stderr, "Failed to get value from Memcached: %s\n", memcached_strerror(memc, ret));
        }

        // Sleep for 10 seconds before the next iteration
        sleep(10);
    }

    // Close the output file
    fclose(output_file);

    // Cleanup the memcached connection
    memcached_free(memc);

    return 0;
}
