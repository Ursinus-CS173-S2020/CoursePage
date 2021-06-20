    

    
    public static int[] cloneArrayPart(int[] arr, int i1, int i2) {
        int N = i2 - i1;
        int[] ret = new int[N];
        for (int i = 0; i < N; i++) {
            ret[i] = arr[i1+i];
        }
        return ret;
    }
    
    public static final int MIN_SIZE = 5;
    
    public static int[] mergeSort(int[] arr) {
        int[] result = {};
        if (arr.length < MIN_SIZE) {
            result = cloneArray(arr);
            insertionSort(result);
        }
        else {
            result = new int[arr.length];
            int halfway = arr.length / 2;
            int[] list1 = cloneArrayPart(arr, 0, halfway);
            int[] list2 = cloneArrayPart(arr, halfway, arr.length);
            list1 = mergeSort(list1);
            list2 = mergeSort(list2);
            int i1 = 0;
            int i2 = 0;
            int i = 0;
            while (i1 < list1.length && i2 < list2.length) {
                if (list1[i1] < list2[i2]) {
                    result[i] = list1[i1];
                    i1++;
                }
                else {
                    result[i] = list2[i2];
                    i2++;
                }
                i++;
            }
            while (i1 < list1.length) {
                result[i] = list1[i1];
                i1++;
                i++;
            }
            while (i2 < list2.length) {
                result[i] = list2[i2];
                i2++;
                i++;
            }
        }
        return result;
    }
