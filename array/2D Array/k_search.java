// Q.)  search element if matrix is sorted row wise and col wise



import java.util.Arrays;

public class k_search {

    public static void main(String[] args) {

        int[][] arr = {
                {10, 20, 30, 40},
                {15, 25, 35, 45},
                {28, 29, 37, 49},
                {33, 34, 38, 50}
        };

        System.out.println(Arrays.toString(search(arr, 49)));
        
    }

    static int[] search(int[][] matrix, int target){
        int row=0;
        int col=matrix.length-1;

        while (row < matrix.length && col >= 0){
        if (target==matrix[row][col]){
            return new int[]{row,col};
        }
        else if(target>matrix[row][col]){
            row++;

        }
        else{
            col--;

        }
      
        
    }
    return new int[]{-1,-1};
   }
    
}
