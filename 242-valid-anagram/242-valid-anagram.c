

bool isAnagram(char * s, char * t){
    if(strlen(s) != strlen(t)) {
        return false;
    }
    int mask[256] = {0};
    char *c = s;
    while(*c) {
        mask[*c++]++;
    }
    c = t;
    while(*c) {
        if(mask[*c] > 0) {
            mask[*c++]--;
        } else {
            return false;
        }
    }
    return true;
}