/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void PostOrderRec(struct TreeNode * root, int *arr ,int *size){
    if(!root) return;
    PostOrderRec(root->left,arr,size);
    PostOrderRec(root->right,arr,size);
    arr[*size ] = root->val;
    *size = *size+1;
}
int* postorderTraversal(struct TreeNode* root, int* returnSize){
    
    int *arr =(int*)malloc( 100 * sizeof(int));
    *returnSize =0;
    PostOrderRec(root,arr,returnSize);
    return arr;
}