#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>

#define MAX_INPUT_STRING_SIZE 64

///
/// Checks whether the given string is a palindrome. (case sensitive)
///
bool isPalindrome(const char *string) {
  const size_t length = strlen(string);
  const size_t halfLength = length / 2;
  for (size_t i = 0; i < halfLength; ++i) {
    if (string[i] != string[length - i - 1])
      return false;
  }
  return true;
}

int main() {
  char input[MAX_INPUT_STRING_SIZE];
  printf("Enter a string: ");
  if (!fgets(input, MAX_INPUT_STRING_SIZE, stdin)) {
    printf("\nERROR: Could not read your input.\n");
    return 1;
  }
  input[strcspn(input, "\n")] = 0;
  const bool inputIsPalindrome = isPalindrome(input);
  printf("%s is%sa palindrome.\n", input, inputIsPalindrome ? " " : " not ");
  return 0;
}