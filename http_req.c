#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main() {
    // Create a socket
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        printf("Error creating socket");
        return 1;
    }

    // Set up the address struct
    struct sockaddr_in server;
    server.sin_addr.s_addr = inet_addr("127.0.0.1"); // Change to the IP address of the server you want to send the request to
    server.sin_family = AF_INET;
    server.sin_port = htons(80); // Change to the port number of the server you want to send the request to

    // Connect to the server
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        printf("Error connecting to server");
        return 1;
    }

    // Send the HTTP request
    char *message = "GET / HTTP/1.1\r\n\r\n";
    if (send(sock, message, strlen(message), 0) < 0) {
        printf("Error sending message");
        return 1;
    }

    // Receive the response
    char response[4096];
    if (recv(sock, response, 4096, 0) < 0) {
        printf("Error receiving response");
        return 1;
    }

    printf("Response received:\n%s", response);

    // Close the socket
    close(sock);

    return 0;
}
