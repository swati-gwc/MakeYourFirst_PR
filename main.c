#include<stdio.h>
#include<conio.h>
void main()
{
    char str[50];
    int i,countSpaces=0,countAlphabet=0,countDigits=0,countSpecialChar=0;
    printf("\nEnter any string : ");
    fgets(str, 50, stdin);
    for(i=0;str[i];i++)
     if(str[i]>='0' && str[i]<='9')
            countDigits++;
        else if((str[i]>='A' && str[i]<='Z')||(str[i]>='a' && str[i]<='z'))
            countAlphabet++;
        else if(str[i]==' ')
            countSpaces++;
        else
            countSpecialChar++;
    printf("\nDigits: %d \nAlphabets: %d \nSpaces: %d \nSpecial Characters: %d",countDigits,countAlphabet,countSpaces,countSpecialChar);        
}