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
void PreOrderRec(struct TreeNode * root, int *arr ,int *size){
    if(!root) return;
    
    
    arr[*size ] = root->val;
    *size = *size+1;
    PreOrderRec(root->left,arr,size);
    PreOrderRec(root->right,arr,size);
}


int* preorderTraversal(struct TreeNode* root, int* returnSize){
    
    int *arr =(int*)malloc( 100 * sizeof(int));
    *returnSize =0;
    
    PreOrderRec(root,arr,returnSize);
    return arr;
    
}