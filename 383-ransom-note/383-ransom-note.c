

bool canConstruct(char * ransomNote, char * magazine){
    int l=strlen(ransomNote);
    int m=strlen(magazine);
    int countr[26]={0}, countm[26]={0};
    int i;
    for(i=0; i<l; i++) countr[ransomNote[i]-'a']++;
    for(i=0; i<m; i++) countm[magazine[i]-'a']++;
    for(i=0; i<26; i++)
        if(countr[i]>countm[i]) break;
    if(26==i)
        return true;
    return false;
}