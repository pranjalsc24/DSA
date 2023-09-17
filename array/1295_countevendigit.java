//  kunal code+ my code commended is kunal's code

class Solution {
    public int findNumbers(int[] nums) {
        // int count=0;
        // for(int num:nums){
        //     if (iseven(num)){
        //         count++;
        //     }
        // }
        // return count;

       int count=0;
       for(int num:nums){
	        if(count(num)){
	            count+=1;
	        }
	    }
	    return count;

    }

    // boolean iseven(int num){
    //     int countdigits=digits(num);
    //     return countdigits %2==0;
    // }

//    
        boolean count(int n){
		    int count=0;
		    while(n>0){
		        n=n/10;
		        count+=1;
		    }
		  //  return count;
		    if(count%2==0){
		        return true;
		    }
		    return false;
		}
		

}