package numbers;

// In this we have to consider if remainder is 0 then when we divide the number with 0 
// it will always come infinity or undefied hence we have to give condition in If block

public class G_countevenlydigits {
    static int evenlyDivides(int N){
        // code here
        int count=0;
        int c=N;
        while(N!=0){
            int remainder=N%10;
            if (remainder!=0 && c%remainder ==0){
                count++;
                
            }
            // else{
            //     count=count;
            // }
            N=N/10;
            
        }
        return count;
    }
    
}
