#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int h = 720;
    int w = 1280;
    char aux[25];
    int frameCount = 0;
    int numFrames = 600;

    if (argc != 2)
    {
        printf("Usage: ./converter <number>\n");
        return 1;
    }

    FILE *fptr, *dest;
    fptr = fopen("../Sequences/vidyo4_720p_60fps.y4m", "r");
    dest = fopen("../Sequences/vidyo4_720p_60fps.yuv", "w");

    

    char c = '\0';

    while(c != '\n')
    {
        fscanf(fptr, "%c", &c);
    }   
    
    while (frameCount < numFrames){
        fgets(aux,25,fptr); //Capture FRAME String 
        printf("%s",aux); //Print FRAME String   
        long counter = 0;
        while (counter < w*h + (w*h)/2)
        {
            fscanf(fptr, "%c", &c);
            fprintf(dest, "%c", c);
            counter++;
        }
        frameCount++;
    }
    
    fclose(fptr);
    fclose(dest);

}