/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int dfs(TreeNode root, int depth){
        if(root==null) return depth;

        int left = dfs(root.left, depth+1);
        int right = dfs(root.right, depth+1);

        return Integer.max(left, right); 
    }
    public int maxDepth(TreeNode root) {
       return dfs(root, 0);
    }

    public boolean isBalanced(TreeNode root) {
        if(root==null){
            return true;
        }

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);

        if(Math.abs(left-right)>1) return false;
        return isBalanced(root.left) && isBalanced(root.right);
    }
}