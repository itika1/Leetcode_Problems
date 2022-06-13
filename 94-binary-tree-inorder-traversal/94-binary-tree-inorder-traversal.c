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
void travel(struct TreeNode* root,int*ret,int*size){
    if(root==NULL)
        return 0 ;
    travel(root->left,ret,size);
    ret[(*size)++]=root->val;
    travel(root->right,ret,size);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize){
    *returnSize=0;
    int *ret=malloc(sizeof(int)*100);
    travel(root,ret,returnSize);
        return ret;

}