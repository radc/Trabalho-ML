#ifndef PREV_BLOCK_SIZE_H
#define PREV_BLOCK_SIZE_H

typedef struct cu_size {
  int width;
  int height;
} cu_size_t;

cu_size_t prevBlockSize[1000][1000];

#endif
