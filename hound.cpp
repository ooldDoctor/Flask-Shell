/* rand example: guess the number */
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>  
#include <cstdlib> 
#include <cstring>  
#include <iostream> 
using namespace std;
      
int A();
int B();
int C();




int main ()
 {

 for(int i = 0; i< 3 ; ++i) {
  switch(rand() % 3) {
    case 0: A(); break;
    case 1: B(); break;
    case 2: C(); break;
  }
 
 }
  return 0;
}
int A()
 {
  system("/home/wiki/ab/app/imgCapture.sh");
  return 0;
}

/*int B(){

cout << "fox";
}

int C(){

cout << "abc";

}
*/




