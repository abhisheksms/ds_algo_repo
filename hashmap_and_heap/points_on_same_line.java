public class Solution {
    public int solve(ArrayList<Integer> a, ArrayList<Integer> b) {
        if(a.size() == 0){
            return 0;
        }
        if(a.size() == 1 && b.size() == 1){
            return 1;
        }
        int max = Integer.MIN_VALUE;
        for(int i = 0; i<a.size(); i++) {
            int x1 = a.get(i) ;
            int y1 = b.get(i) ;
            // not global because we want to avoid extra addition.
            HashMap<Double, Integer> map = new HashMap<Double, Integer>();
            int samePoint = 1;
            int infValue = 0; 
            for(int j = i+1; j<a.size(); j++) {
               int x2 = a.get(j) ;
               int y2 = b.get(j) ;
               if((x1 == x2)&&(y1==y2)) {
                   samePoint += 1;
               } else if(x2 - x1 == 0) {
                   infValue++;
               } else {
                   double slope = 0.0;
                   if(y1 != y2) {
                      slope = (double)(y2-y1)/(double)(x2-x1);
                   }
                   //System.out.println("Slope:" + slope);
                   if(map.containsKey(slope)) {
                       map.put(slope, map.get(slope) + 1);
                       int count = map.get(slope);
                       //System.out.println("count:" + count);
                   } else {
                       map.put(slope, 1);
                   }
               }
            }
            if((infValue + samePoint)  > max) {
                //System.out.println("infValue:" + infValue);
                max = infValue+samePoint;
            }
            // for(Double key : map.keySet() ){
            //     System.out.println("key:" + key);
            // }
            for(Integer value : map.values() ){
                //System.out.println("samePoint:" + samePoint);
                //System.out.println("value:" + value);
                max = Math.max(value+samePoint, max);
            }
        }
        return max;
    }
}