/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void merge(int a[],int b[],int low,int high,int mid){
    int i=low;
    int j=mid+1;
    int k=low;
    while(i<=mid && j<=high){
        if(a[i]<=a[j]){
            b[k]=a[i];
            i++;
        }
        else{
            b[k]=a[j];
            j++;
        }
        k++;}
    if(i>mid){
        while(j<=high){
            b[k]=a[j];
            j++;
            k++;
        }}
        else{
         while(i<=mid){
            b[k]=a[i];
            i++;
            k++;
        }   
        }

for(i=low;i<=high;i++){
    a[i]=b[i];
}
}
void mergesort(int a[],int b[],int low,int high){
    if(low<high){
    int mid=low+(high-low)/2;
    mergesort(a,b,low,mid);
    mergesort(a,b,mid+1,high);
    merge(a,b,low,high,mid);
}}
int* sortArray(int* nums, int numsSize, int* returnSize) {
   *returnSize=numsSize;
      *returnSize = numsSize;

    if (numsSize <= 1)
        return nums;

    int *b = malloc(numsSize * sizeof(int));

    if (b == NULL)
    {
        *returnSize = 0;
        return NULL;
    }
   mergesort(nums,b,0,numsSize-1);
   return nums;
}