#include <iostream>
#include <xmmintrin.h>
#include <ctime>
#include<cmath>
#define N 1000000
#define MAX_THREAD 2
#include<pthread.h>
using namespace std ;
 int step_i = 0 ;
 int step_k = 0 ;
__attribute__ ( ( aligned (16) ) )float A[N] = {};
__attribute__ ( ( aligned (16) ) )float B[N] = {};
__attribute__ ( ( aligned (16) ) )float C[N] = {0};
void* THREAD_SIMD_ADD( void* arg ) {
 int core = step_i++;
 for (  int i = core * N / MAX_THREAD; i < ( core + 1) * N /
MAX_THREAD; i +=4){
__m128 a = _mm_load_ps(&A[ i ] ) ;
__m128 b = _mm_load_ps(&B[ i ] ) ;
__m128 c = _mm_add_ps(a , b) ;
_mm_store_ps(&C[ i ] , c ) ;
}
}
void SIMD_ADD(float A[ ] ,float B[ ] ,float C [ ] ) {
 for (  int i =0; i<N; i +=4){
__m128 a = _mm_load_ps(&A[ i ] ) ;
__m128 b = _mm_load_ps(&B[ i ] ) ;
__m128 c = _mm_add_ps(a , b) ;
_mm_store_ps(&C[ i ] , c ) ;
}
}
void Original_add (float A[ ] ,float B[ ] ,float C [ ] ) {
 for (  int i =0; i<N; i++) C[ i ]=A[ i ]+B[ i ] ;
}
void*THREAD_Original_add( void* arg ) {
 int core = step_i++;
 for (  int i = core * N / MAX_THREAD; i < ( core + 1) * N /
MAX_THREAD; i++){
C[ i ]=A[ i ]+B[ i ] ;
}
}
 int main ( )
{
 for (  int i =0; i<N; i++) A[ i ]=rand ( ) %10;
 for (  int i =0; i<N; i++) B[ i ]=rand ( ) %10;
cout << "The  s i z e   of   the   array   i s : " << N << endl ;
cout << "The number  of   thread   i s : " << MAX_THREAD << endl ;
clock_t start=clock ( ) ;
Original_add (A,B,C) ;
cout << "The  cost   of   original_add   i s : " << ( double ) ( clock ( )
-start ) << endl ;
start=clock ( ) ;
SIMD_ADD(A,B,C) ;
cout << "The  cost   of  SIMD_add  i s : " << ( double ) ( clock ( )-
start ) << endl ;
start=clock ( ) ;
pthread_t threads1 [MAX_THREAD] ;
 for (  int i = 0 ; i < MAX_THREAD; i++) {
 int * p ;
pthread_create(&threads1 [ i ] , NULL, THREAD_Original_add
, ( void*) (p) ) ;
}
 for (  int i = 0 ; i < MAX_THREAD; i++)
pthread_join ( threads1 [ i ] , NULL) ;
clock_t end=clock ( ) ;
cout << "The  cost   of  thread_original_add   i s : " << ( double ) (
end-start ) << " s " << endl ;
start=clock ( ) ;
pthread_t threads2 [MAX_THREAD] ;
 for (  int i = 0 ; i < MAX_THREAD; i++) {
 int * p ;
pthread_create(&threads2 [ i ] , NULL, THREAD_SIMD_ADD, (
void*) (p) ) ;
}
 for (  int i = 0 ; i < MAX_THREAD; i++)
pthread_join ( threads2 [ i ] , NULL) ;
end=clock ( ) ;
cout << "The  cost   of  thread_SIMD_add  is : " << ( double ) ( end-
start ) /CLOCKS_PER_SEC << " s " << endl ;
return 0 ;
}