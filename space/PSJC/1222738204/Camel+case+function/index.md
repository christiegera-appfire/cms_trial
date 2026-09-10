# Camel case function

Often times you may find yourself in need of generating camel case names. For example, if I wanted to programmatically create custom fields using SIL I could add SIL aliases for those custom fields at the same time. You want to avoid using spaces in alias names so a convention like camel case is an excellent habit to adopt.

```text
function camelCase(string name) {
    string [] words = split(name, " ");
    string cc = toLower(words[0]);
    
    for(int x=1; x<size(words); x++) {
        string nextWord;
        for(int l=0; l<length(words[x]); l++) {
            if(l==0) {
                nextWord = toUpper(words[x][l]);
            } else {
                nextWord += words[x][l];
            }
        }
        cc += nextWord;
    }
    return cc;
}

return camelCase("I love using Power Scripts");

//returns iLoveUsingPowerScripts
```