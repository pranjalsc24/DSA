package sorting;

import java.util.Arrays;

public class bubble {
    
    public static void main(String[] args) {
      int[] arr={5,9,2,4,10};
      bubblesort(arr);
      System.out.println(Arrays.toString(arr));
        
    }

    static void bubblesort(int[] arr){
        for(int i=0; i< arr.length ;i++){
            boolean swap=false;
            for(int j=1; j<arr.length-1;j++){
                if (arr[j-1]>arr[j]){
                    // swap
                    int temp=arr[j];
                    arr[j]=arr[j-1];
                    arr[j-1]=temp;
                    swap=true;
                }


            }
            if (swap==false){
                break;
            }
        }

}

    
}
