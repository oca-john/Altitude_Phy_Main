#include "stdio.h"
#include "sys/time.h"
#include "time.h"
#include "string.h"
// If you are using WSL as a back-end for your data processing during 
// development, this program can help you to obtain timestamps.


int main()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    // printf("Seconds: %d\n", tv.tv_sec);
    // printf("Microseconds: %d\n", tv.tv_usec/1000);
    time_t now;
    struct tm *tm_now;
    char datetime[132];
 
    time(&now);
    tm_now = localtime(&now);
    strftime(datetime, 128, "%Y-%m-%d %H:%M:%S", tm_now);
    printf("%s", datetime);
    printf(".%d\n", tv.tv_usec/1000);

    return 0;
}
