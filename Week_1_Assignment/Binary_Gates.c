#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/***************************
BINARY GATE SIMULATION:
This program takes two binary
inputs (0s or 1s) and returns
the result of the gate
operations (AND, OR, XOR)
****************************/
int main(void) {

// The char to hold the gate type
char gate = 'a';

// The binary values that will be our input
int binary1 = 0;
int binary2 = 0;

// Values that are read from the user
char read1 = EOF + 1;
int read2 = EOF + 1;
int read3 = EOF + 1;

printf("Please enter the first letter of one of the following gate operations: \n");
printf("AND: A, OR: O, XOR: X. \n");

// Selecting which gate the input is used on

// Take input from the user
read1 = scanf("%c", &gate);

// Try again if the input is not a correct letter
if (gate != 'A' && gate != 'O' && gate != 'X') {
	printf("Please enter a valid gate operation in capital letters. ('A', 'O', or 'X')\n"); 
	
	while (gate != 'A' && gate != 'O' && gate != 'X') {
		read1 = scanf("%c", &gate); } }


printf("Please enter the binary value of the first input. (0 or 1).\n");

// Gathering 2 binary values to be used as input for the gate

// Take input from the user
read2 = scanf("%d", &binary1);

// Try again if the input is not a binary value
if (binary1 != 0 && binary1 != 1) {
	printf("Please enter a valid binary value of 0 or 1\n"); 
	
	while (binary1 != 0 && binary1 != 1) {
		read2 = scanf("%d", &binary1); } } 

printf("Please enter the binary value of the second input. (0 or 1).\n");

// Take input from the user
read3 = scanf("%d", &binary2);
	
// Try again if the input is not a binary value
if (binary2 != 0 && binary2 != 1) {
	printf("Please enter a valid binary value of 0 or 1\n"); 

	while (binary2 != 0 && binary2 != 1) {
		read3 = scanf("%d", &binary2); } }


printf("-----RESULTS-----\n");


// AND Gate
if (gate == 'A') {
	// AND gates only return true if all inputs are 1
	if (binary1 == 1 && binary2 == 1) { printf("True (1)\n"); }
	
	// Else, they return false
	else {  printf("False (0)\n"); } }

// OR Gate
else if (gate == 'O') {
	// OR gates return true if any of the inputs are 1
	if (binary1 == 1 || binary2 == 1) { printf("True (1)\n"); }
	
	// Else, they return false
	else {  printf("False (0)\n"); } }

//. XOR Gate
else if (gate == 'X') {
	// XOR gates only return true if either of the inputs are 1, but not both
	if ((binary1 == 1 && binary2 == 0) || (binary1 == 0 && binary2 == 1)) { 
	printf("True (1)\n"); }

	// Else, they return false
	else {  printf("False (0)\n"); } }

else { printf("An error occured. Please try again.\n"); }

return 0; }
