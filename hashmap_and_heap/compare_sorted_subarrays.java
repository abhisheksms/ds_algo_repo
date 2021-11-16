public class Solution {
    public ArrayList < Integer > solve(ArrayList < Integer > A, ArrayList < ArrayList < Integer >> B) {
        /*
            -Create a random hash for each value
            -How is the hash generated??
            -Prefix sum array of hash values
            -Then check if prefix sum from l1 to r1 is equal to l2 to r2

            TC AND SC : O(n+q)

            Also could have use a hash map mapping
            where key : number
                  value : hashed vlaued of the number
        */
        int n = A.size();
        Random rd = new Random();
        HashMap < Integer, Long > hm = new HashMap < > ();
        HashSet < Long > used = new HashSet < > ();
        long psum[] = new long[n + 1];
        for (int i = 0; i < n; i++) {
            if (!hm.containsKey(A.get(i))) {
                long hash = rd.nextLong();
                while (used.contains(hash)) {
                    hash = rd.nextLong();
                }
                hm.put(A.get(i), hash);
            }
            psum[i + 1] = psum[i] + hm.get(A.get(i));
        }
        ArrayList < Integer > ans = new ArrayList < Integer > ();
        for (ArrayList < Integer > tmp: B) {
            long val1 = psum[tmp.get(1) + 1] - psum[tmp.get(0)];
            long val2 = psum[tmp.get(3) + 1] - psum[tmp.get(2)];
            if (val1 == val2) {
                ans.add(1);
            } else {
                ans.add(0);
            }
        }
        return ans;
    }
}