// C program to determine class, Network , subnet mask
// and Host ID of an IPv4 address 
#include<stdio.h> 
#include<string.h> 

// Function to find out the Class 
char findClass(char str[]) 
{ 
	//complete the function to find the class of the given IPv4 address. Consult README.md to know more about a class of an ip address. 
} 

// Function to separate Network ID as well as 
// Host ID and print them 
void separate(char str[], char ipClass) 
{ 

	//Complete the finction for classes A, B and C to find the network ID and host Id and print the same. Use switch case

	// Class D and E are not divided in Network 
	// and Host ID 
	//provide the case for same and print "cannot be divided"
} 

void subnet(char ipclass){

	//complete the function to find subnet mask 
	// of the given IPv4 address using the class.
}

// main function
int main() 
{ 
	char str[20] ;
	printf("Enter IP address \n");
	fgets(str, 20, stdin); 
	char ipClass = findClass(str); 
	subnet(ipClass)
	printf("Given IP address belongs to Class %c\n", ipClass); 
	separate(str, ipClass); 
	return 0; 
} 
