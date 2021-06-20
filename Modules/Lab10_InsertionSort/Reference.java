
    public static double[] getRandomArray(int N) {
        double[] arr = new double[N];
        Random rand = new Random();
        for (int i = 0; i < N; i++) {
            arr[i] = (double)rand.nextInt(N);
        }
        return arr;
    }
    
    public static boolean arraysEqual(double[] arr1, double[] arr2) {
        boolean equal = true;
        if (arr1.length == arr2.length) {
            for (int i = 0; i < arr1.length && equal; i++) {
                if (arr1[i] != arr2[i]) {
                    equal = false;
                }
            }
        }
        else {
            equal = false;
        }
        return equal;
    }
    
    public static double[] copyArray(double[] arr) {
        double[] res = new double[arr.length];
        for (int i = 0; i < res.length; i++) {
            res[i] = arr[i];
        }
        return res;
    }
    
    public static void swap(double[] arr, int i, int j) {
        double temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    public static void insertionSort(double[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int j = i;
            while (j > 0 && arr[j] < arr[j-1]) {
                swap(arr, j, j-1);
                j--;
            }
        }
    }
    
    public static void printArray(double[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
    
    public static void main(String[] args) {
        double[] arr = getRandomArray(100);
        double[] arr2 = copyArray(arr);
        Arrays.sort(arr);
        insertionSort(arr2);
        printArray(arr2);
        System.out.println(arraysEqual(arr, arr2));
    }
